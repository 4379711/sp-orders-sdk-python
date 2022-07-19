# coding: utf-8
from __future__ import absolute_import

import io
import json
import re
import ssl
import hashlib
from datetime import datetime
from collections import OrderedDict

import urllib3
import hmac
from threading import Lock
from urllib.parse import urlparse, quote, urlencode
from boto3.session import Session as botSession
from geeker import retry
from my_client.configuration import Configuration

# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
urllib3.disable_warnings()
# <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):
    AWS_LOCK = Lock()

    def __init__(self, configuration):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        self.configuration = configuration
        self.default_timeout = urllib3.Timeout(total=configuration.request_timeout)

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        ca_certs = configuration.ssl_ca_cert

        addition_pool_args = configuration.addition_pool_args
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        """
        retries: https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.Retry
                Only retry DNS resolution errors, link errors, link timeouts
                Read timeout, write timeout, HTTP protocol error, etc. will not be retried by default
                Set to False, you can disable retry
        """
        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=configuration.pools_size,
                maxsize=configuration.maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                retries=False,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=configuration.pools_size,
                maxsize=configuration.maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                retries=False,
                **addition_pool_args
            )
        self._client = botSession().client(service_name='sts',
                                           aws_access_key_id=self.configuration.aws_access_key,
                                           aws_secret_access_key=self.configuration.aws_secret_key)

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None, **kwargs):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _skip_auth: skip auth .
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        if _request_timeout:
            if isinstance(_request_timeout, int):
                timeout = urllib3.Timeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = urllib3.Timeout(connect=_request_timeout[0], read=_request_timeout[1])
            else:
                raise ValueError('value of _request_timeout must be int or tuple !')
        else:
            timeout = self.default_timeout

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json;charset=UTF-8'
        query_params = [(k, v) for k, v in query_params if v is not None] if query_params else None
        if not kwargs.get("_skip_auth"):
            auth = self._get_access_token()
            headers.update(auth)
            if 'role' not in Configuration.role_cache:
                with RESTClientObject.AWS_LOCK:
                    if 'role' not in Configuration.role_cache:
                        role = self._client.assume_role(
                            RoleArn=self.configuration.role_arn,
                            RoleSessionName='guid').get('Credentials')
                        Configuration.role_cache['role'] = role
            role = Configuration.role_cache['role']
            signed_header = self.sign(url,
                                      method,
                                      json.dumps(body) if body else None,
                                      dict(query_params) if query_params else None,
                                      role.get('AccessKeyId'),
                                      role.get('SecretAccessKey'),
                                      self.configuration.aws_region,
                                      role.get('SessionToken'))
            headers.update(signed_header)

        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if query_params:
                url += '?' + urlencode(query_params)
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                request_body = None
                if body is not None:
                    request_body = json.dumps(body)
                r = self.pool_manager.request(
                    method, url,
                    body=request_body,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            elif headers['Content-Type'].lower().startswith('application/x-www-form-urlencoded'):  # noqa: E501
                r = self.pool_manager.request(
                    method, url,
                    fields=post_params,
                    encode_multipart=False,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            elif headers['Content-Type'].lower().startswith('multipart/form-data'):
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by urllib3 will be
                # overwritten.
                del headers['Content-Type']
                r = self.pool_manager.request(
                    method, url,
                    fields=post_params,
                    encode_multipart=True,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            # Pass a `string` parameter directly in the body to support
            # other content types than Json when `body` argument is
            # provided in serialized form
            elif isinstance(body, str):
                request_body = body
                r = self.pool_manager.request(
                    method, url,
                    body=request_body,
                    preload_content=_preload_content,
                    timeout=timeout,
                    headers=headers)
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)
        # For `GET`, `HEAD`
        else:
            r = self.pool_manager.request(method, url,
                                          fields=query_params,
                                          preload_content=_preload_content,
                                          timeout=timeout,
                                          headers=headers)
        if _preload_content:
            r = RESTResponse(r)
            r.data = r.data.decode('utf-8')

        if r.status == 429:
            raise RateLimitException(status=429)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None, **kwargs):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params, **kwargs)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None, **kwargs):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params, **kwargs)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None, **kwargs):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body, **kwargs)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None, **kwargs):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body, **kwargs)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None, **kwargs):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body, **kwargs)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None, **kwargs):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body, **kwargs)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None, **kwargs):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body, **kwargs)

    @retry(retry_times=3)
    def _get_access_token(self):
        if self.configuration.refresh_token not in Configuration.access_token_cache:
            data = {
                'grant_type': 'refresh_token',
                'client_id': self.configuration.client_id,
                'client_secret': self.configuration.client_secret,
                'refresh_token': self.configuration.refresh_token,
            }

            response = self.pool_manager.request(
                'POST',
                'https://api.amazon.com/auth/o2/token',
                body=json.dumps(data),
                encode_multipart=False,
                timeout=self.configuration.request_timeout
            )

            result = response.data.decode('utf-8')
            if response.status != 200:
                raise RuntimeError("get access_token failed:{}".format(result))
            access_token = json.loads(result).get('access_token')
            if not access_token:
                raise RuntimeError("get access_token failed:{}".format(result))
            Configuration.access_token_cache[self.configuration.refresh_token] = access_token

        parsed_headers = {
            'host': self.configuration.host[8:],
            'x-amz-access-token': Configuration.access_token_cache[self.configuration.refresh_token],
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'Content-Type': 'application/json;charset=UTF-8'}
        return parsed_headers

    def get_auth_header(self):
        if 'role' not in Configuration.role_cache:
            role = self._client.assume_role(RoleArn=self.configuration.role_arn,
                                            RoleSessionName='guid').get('Credentials')
            Configuration.role_cache['role'] = role
        access_header = self._get_access_token()
        return access_header

    @staticmethod
    def sign_msg(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

    def sign(self, url, method, body, params, aws_access_key_id, aws_secret_access_key, region, aws_session_token):
        # Create a date for headers and the credential string
        now = datetime.utcnow()
        amz_date = now.strftime('%Y%m%dT%H%M%SZ')
        datestamp = now.strftime('%Y%m%d')
        # Parse request to get URL parts
        p = urlparse(url)
        host = p.hostname
        uri = quote(p.path)
        if len(p.query) > 0:
            qs = dict(map(lambda i: i.split('='), p.query.split('&')))
        else:
            qs = dict()
        if params:
            qs.update(params)

        canonical_querystring = urlencode(sorted(qs.items()))

        headers_to_sign = {'host': host, 'x-amz-date': amz_date}
        if aws_session_token is not None:
            headers_to_sign['x-amz-security-token'] = aws_session_token

        ordered_headers = OrderedDict(sorted(headers_to_sign.items(), key=lambda t: t[0]))
        canonical_headers = ''.join(map(lambda h: ":".join(h) + '\n', ordered_headers.items()))
        signed_headers = ';'.join(ordered_headers.keys())
        if method == 'GET':
            payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
        else:
            body = body if body else ""
            payload_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
        canonical_request = '\n'.join(
            [method, uri, canonical_querystring, canonical_headers, signed_headers, payload_hash])
        credential_scope = '/'.join([datestamp, region, "execute-api", 'aws4_request'])
        string_to_sign = '\n'.join(['AWS4-HMAC-SHA256', amz_date, credential_scope,
                                    hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()])

        k_date = self.sign_msg(('AWS4' + aws_secret_access_key).encode('utf-8'), datestamp)
        k_region = self.sign_msg(k_date, region)
        k_service = self.sign_msg(k_region, "execute-api")
        k_signing = self.sign_msg(k_service, 'aws4_request')
        signature = hmac.new(k_signing, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = "AWS4-HMAC-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(
            aws_access_key_id, credential_scope, signed_headers, signature)

        return {
            'host': host,
            'x-amz-date': amz_date,
            'Authorization': authorization_header,
            'x-amz-security-token': aws_session_token
        }


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class RateLimitException(ApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        super(RateLimitException, self).__init__(status=status, reason=reason, http_resp=http_resp)

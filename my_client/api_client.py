# coding: utf-8
from __future__ import absolute_import

import datetime
import mimetypes
import os

import six
from six.moves.urllib.parse import quote

from my_client import rest


class ApiClient(object):
    """
    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self, configuration, header_name=None, header_value=None, cookie=None):

        self.configuration = configuration
        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'myclient/1.0.0/python'
        self.client_side_validation = configuration.client_side_validation

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
            self, resource_path, method, path_params=None,
            query_params=None, header_params=None, body=None, post_params=None,
            files=None, _return_http_data_only=None, collection_formats=None,
            _preload_content=True, _request_timeout=None):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params, collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self.configuration.host + resource_path

        # perform request and return response
        response_data = self.request(
            method, url, query_params=query_params, headers=header_params,
            post_params=post_params, body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout)

        if _return_http_data_only:
            return response_data.data
        else:
            return (response_data.data, response_data.status,
                    response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True, _request_timeout=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params: dict Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param files: dict key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            return the response directly.
        """
        return self.__call_api(resource_path, method,
                               path_params, query_params, header_params,
                               body, post_params, files,
                               _return_http_data_only, collection_formats,
                               _preload_content, _request_timeout)

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    @staticmethod
    def parameters_to_tuples(params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    @staticmethod
    def prepare_post_parameters(post_params=None, files=None):
        """Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in six.iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (mimetypes.guess_type(filename)[0] or
                                    'application/octet-stream')
                        params.append(
                            tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    @staticmethod
    def select_header_accept(accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    @staticmethod
    def select_header_content_type(content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

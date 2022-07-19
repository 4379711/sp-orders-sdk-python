# coding: utf-8
from __future__ import absolute_import

from enum import Enum
from cachetools import TTLCache
import ssl


class MarketplaceRegion(Enum):
    US = ('https://sellingpartnerapi-na.amazon.com', 'us-east-1', "ATVPDKIKX0DER")
    CA = ('https://sellingpartnerapi-na.amazon.com', 'us-east-1', "A2EUQ1WTGCTBG2")
    MX = ('https://sellingpartnerapi-na.amazon.com', 'us-east-1', "A1AM78C64UM0Y8")
    BR = ('https://sellingpartnerapi-na.amazon.com', 'us-east-1', "A2Q3Y263D00KWC")

    JP = ('https://sellingpartnerapi-fe.amazon.com', 'us-west-2', "A1VC38T7YXB528")
    AU = ('https://sellingpartnerapi-fe.amazon.com', 'us-west-2', "A39IBJ37TRP1C6")
    SG = ('https://sellingpartnerapi-fe.amazon.com', 'us-west-2', "A19VAU5U5O7RUS")

    UK = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A1F83G8C2ARO7P")
    GB = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A1F83G8C2ARO7P")
    NL = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A1805IZSGTT6HS")
    FR = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A13V1IB3VIYZZH")
    IT = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "APJ6JRA9NG5V4")
    ES = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A1RKKUPIHCS9HS")
    SE = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A2NODRKZP88ZB9")
    TR = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A33AVAJ2PDY3EV")
    DE = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A1PA6795UKMFR9")
    AE = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A2VIGQ35RCS4UG")
    IN = ('https://sellingpartnerapi-eu.amazon.com', 'eu-west-1', "A21TJRUUN4KGV")

    def __init__(self, host, aws_region, marketplace):
        self.host = host
        self.aws_region = aws_region
        self.marketplace = marketplace


class Configuration(object):

    role_cache = TTLCache(maxsize=1000, ttl=3000)
    access_token_cache = TTLCache(maxsize=1000, ttl=3000)

    def __init__(self, **kwargs):
        self.role_arn = kwargs.get('role_arn')
        self.refresh_token = kwargs.get('refresh_token')
        self.aws_access_key = kwargs.get('aws_access_key')
        self.aws_secret_key = kwargs.get('aws_secret_key')
        self.aws_region = MarketplaceRegion[kwargs.get('region', 'US')].aws_region
        self.client_id = kwargs.get('client_id')
        self.client_secret = kwargs.get('client_secret')
        self.marketplace = MarketplaceRegion[kwargs.get('region', 'US')].marketplace
        self.host = MarketplaceRegion[kwargs.get('region', 'US')].host
        # Temp file folder for downloading files
        self.temp_folder_path = None
        # request timeout (seconds)
        self.request_timeout = 180

        # PoolManager size
        # Number of connection pools to cache before discarding the least recently used pool.
        self.pools_size = 2
        self.maxsize = 2

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = False
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = False

        # Set poolManager keywords args
        self.addition_pool_args = {
            'ssl_version': ssl.PROTOCOL_TLSv1_2
        }

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

        # Disable client side validation
        self.client_side_validation = True

        # deserialize response to model
        self.deserialize = True

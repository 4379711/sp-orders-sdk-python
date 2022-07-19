# coding: utf-8
from __future__ import absolute_import

import datetime
import json
import re
import tempfile
import os
import six
from my_client import rest

try:
    import my_client.models
except ImportError:
    pass


class DeSerialize:
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
    remove_ioss = re.compile(r'"DeemedResellerCategory": (.*)')

    def __init__(self, configuration):
        self._configuration = configuration

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(my_client.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def deserialize(self, data, response_type: str):
        """Deserializes response into an object.

        :param data: (response_data,) /(response_data, response_data.status, response_data.getheaders())
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        return_http_data_only = False if (isinstance(data, tuple) and len(data) == 3) else True

        if return_http_data_only:
            if response_type == "file":
                return self.__deserialize_file(data)
            try:
                # todo 20210702 16:15 暂时把DeemedResellerCategory的值置为空,以后要删除这个
                data = self.remove_ioss.sub('"DeemedResellerCategory": ""', data)
                tmp = json.loads(data)
            except ValueError:
                tmp = data
            return self.__deserialize(tmp, response_type)
        else:
            if response_type == "file":
                return self.__deserialize_file(data[0]), data[1], data[2]
            try:
                tmp = json.loads(data[0])
            except ValueError:
                tmp = data[0]
            return self.__deserialize(tmp, response_type), data[1], data[2]

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self._configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                                 content_disposition).group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "w") as f:
            f.write(response.data)

        return path

    def __hasattr(self, object, name):
        return name in object.__class__.__dict__

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                        .format(string)
                )
            )

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if (not klass.swagger_types and
                not self.__hasattr(klass, 'get_real_child_model')):
            return data
        # pass configuration to model 20210602 12:09
        kwargs = {"_configuration": self._configuration}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if (isinstance(instance, dict) and
                klass.swagger_types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance


class OrdersV0Api(object):

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_order(self, order_id, **kwargs):  # noqa: E501
        """get_order  # noqa: E501

        Returns the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_order_with_http_info(order_id, **kwargs)
        return data

    def __get_order_with_http_info(self, order_id, **kwargs):
        """get_order  # noqa: E501

        Returns the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderResponse
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order_id` when calling `get_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders/{orderId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrderResponse')
        return data

    def get_order_address(self, order_id, **kwargs):  # noqa: E501
        """get_order_address  # noqa: E501

        Returns the shipping address for the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param str order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderAddressResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_order_address_with_http_info(order_id, **kwargs)
        return data

    def __get_order_address_with_http_info(self, order_id, **kwargs):
        """get_order_address  # noqa: E501

        Returns the shipping address for the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param str order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderAddressResponse
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders/{orderId}/address', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrderAddressResponse')
        return data

    def get_order_buyer_info(self, order_id, **kwargs):  # noqa: E501
        """get_order_buyer_info  # noqa: E501

        Returns buyer information for the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param str order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderBuyerInfoResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_order_buyer_info_with_http_info(order_id, **kwargs)
        return data

    def __get_order_buyer_info_with_http_info(self, order_id, **kwargs):
        """get_order_buyer_info  # noqa: E501

        Returns buyer information for the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param str order_id: An orderId is an Amazon-defined order identifier, in 3-7-7 format. (required)
        :return: GetOrderBuyerInfoResponse
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_buyer_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `order_id` when calling `get_order_buyer_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders/{orderId}/buyerInfo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrderBuyerInfoResponse')
        return data

    def get_order_items(self, order_id, **kwargs):  # noqa: E501
        """get_order_items  # noqa: E501

        Returns detailed order item information for the order indicated by the specified order ID. If NextToken is provided, it's used to retrieve the next page of order items.  Note: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :param str next_token: A string token returned in the response of your previous request.
        :return: GetOrderItemsResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_order_items_with_http_info(order_id, **kwargs)
        return data

    def __get_order_items_with_http_info(self, order_id, **kwargs):
        """get_order_items  # noqa: E501

        Returns detailed order item information for the order indicated by the specified order ID. If NextToken is provided, it's used to retrieve the next page of order items.  Note: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :param str next_token: A string token returned in the response of your previous request.
        :return: GetOrderItemsResponse
        """

        all_params = ['order_id', 'next_token']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []
        if 'next_token' in params:
            query_params.append(('NextToken', params['next_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders/{orderId}/orderItems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrderItemsResponse')
        return data

    def get_order_items_buyer_info(self, order_id, **kwargs):  # noqa: E501
        """get_order_items_buyer_info  # noqa: E501

        Returns buyer information in the order items of the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :param str next_token: A string token returned in the response of your previous request.
        :return: GetOrderItemsBuyerInfoResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_order_items_buyer_info_with_http_info(order_id, **kwargs)
        return data

    def __get_order_items_buyer_info_with_http_info(self, order_id, **kwargs):
        """get_order_items_buyer_info  # noqa: E501

        Returns buyer information in the order items of the order indicated by the specified order ID.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param str order_id: An Amazon-defined order identifier, in 3-7-7 format. (required)
        :param str next_token: A string token returned in the response of your previous request.
        :return: GetOrderItemsBuyerInfoResponse
        """

        all_params = ['order_id', 'next_token']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_items_buyer_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if self.api_client.client_side_validation and ('order_id' not in params or
                                                       params['order_id'] is None):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `order_id` when calling `get_order_items_buyer_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']  # noqa: E501

        query_params = []
        if 'next_token' in params:
            query_params.append(('NextToken', params['next_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders/{orderId}/orderItems/buyerInfo', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrderItemsBuyerInfoResponse')
        return data

    def get_orders(self, marketplace_ids, **kwargs):  # noqa: E501
        """get_orders  # noqa: E501

        Returns orders created or updated during the time frame indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be used to retrieve the orders instead of other criteria.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501

        :param list[str] marketplace_ids: A list of MarketplaceId values. Used to select orders that were placed in the specified marketplaces. (required)
        :param str created_after: A date used for selecting orders created after (or at) a specified time. Only orders placed after the specified time are returned. Either the CreatedAfter parameter or the LastUpdatedAfter parameter is required. Both cannot be empty. The date must be in ISO 8601 format.
        :param str created_before: A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in ISO 8601 format.
        :param str last_updated_after: A date used for selecting orders that were last updated after (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
        :param str last_updated_before: A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
        :param list[str] order_statuses: A list of OrderStatus values used to filter the results. Possible values: PendingAvailability (This status is available for pre-orders only. The order has been placed, payment has not been authorized, and the release date of the item is in the future.); Pending (The order has been placed but payment has not been authorized); Unshipped (Payment has been authorized and the order is ready for shipment, but no items in the order have been shipped); PartiallyShipped (One or more, but not all, items in the order have been shipped); Shipped (All items in the order have been shipped); InvoiceUnconfirmed (All items in the order have been shipped. The seller has not yet given confirmation to Amazon that the invoice has been shipped to the buyer.); Canceled (The order has been canceled); and Unfulfillable (The order cannot be fulfilled. This state applies only to Multi-Channel Fulfillment orders.).
        :param list[str] fulfillment_channels: A list that indicates how an order was fulfilled. Filters the results by fulfillment channel. Possible values: FBA (Fulfillment by Amazon); SellerFulfilled (Fulfilled by the seller).
        :param list[str] payment_methods: A list of payment method values. Used to select orders paid using the specified payment methods. Possible values: COD (Cash on delivery); CVS (Convenience store payment); Other (Any payment method other than COD or CVS).
        :param str buyer_email: The email address of a buyer. Used to select orders that contain the specified email address.
        :param str seller_order_id: An order identifier that is specified by the seller. Used to select only the orders that match the order identifier. If SellerOrderId is specified, then FulfillmentChannels, OrderStatuses, PaymentMethod, LastUpdatedAfter, LastUpdatedBefore, and BuyerEmail cannot be specified.
        :param int max_results_per_page: A number that indicates the maximum number of orders that can be returned per page. Value must be 1 - 100. Default 100.
        :param list[str] easy_ship_shipment_statuses: A list of EasyShipShipmentStatus values. Used to select Easy Ship orders with statuses that match the specified  values. If EasyShipShipmentStatus is specified, only Amazon Easy Ship orders are returned.Possible values: PendingPickUp (Amazon has not yet picked up the package from the seller). LabelCanceled (The seller canceled the pickup). PickedUp (Amazon has picked up the package from the seller). AtOriginFC (The packaged is at the origin fulfillment center). AtDestinationFC (The package is at the destination fulfillment center). OutForDelivery (The package is out for delivery). Damaged (The package was damaged by the carrier). Delivered (The package has been delivered to the buyer). RejectedByBuyer (The package has been rejected by the buyer). Undeliverable (The package cannot be delivered). ReturnedToSeller (The package was not delivered to the buyer and was returned to the seller). ReturningToSeller (The package was not delivered to the buyer and is being returned to the seller).
        :param str next_token: A string token returned in the response of your previous request.
        :param list[str] amazon_order_ids: A list of AmazonOrderId values. An AmazonOrderId is an Amazon-defined order identifier, in 3-7-7 format.
        :param str actual_fulfillment_supply_source_id: Denotes the recommended sourceId where the order should be fulfilled from.
        :param bool is_ispu: When true, this order is marked to be picked up from a store rather than delivered.
        :param str store_chain_store_id: The store chain store identifier. Linked to a specific store in a store chain.
        :return: GetOrdersResponse
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        data = self.__get_orders_with_http_info(marketplace_ids, **kwargs)
        return data

    def __get_orders_with_http_info(self, marketplace_ids, **kwargs):
        """get_orders  # noqa: E501

        Returns orders created or updated during the time frame indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned. If NextToken is present, that will be used to retrieve the orders instead of other criteria.  **Usage Plans:**  | Plan type | Rate (requests per second) | Burst | | ---- | ---- | ---- | |Default| 0.0055 | 20 | |Selling partner specific| Variable | Variable |  The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        :param list[str] marketplace_ids: A list of MarketplaceId values. Used to select orders that were placed in the specified marketplaces. (required)
        :param str created_after: A date used for selecting orders created after (or at) a specified time. Only orders placed after the specified time are returned. Either the CreatedAfter parameter or the LastUpdatedAfter parameter is required. Both cannot be empty. The date must be in ISO 8601 format.
        :param str created_before: A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in ISO 8601 format.
        :param str last_updated_after: A date used for selecting orders that were last updated after (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
        :param str last_updated_before: A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in ISO 8601 format.
        :param list[str] order_statuses: A list of OrderStatus values used to filter the results. Possible values: PendingAvailability (This status is available for pre-orders only. The order has been placed, payment has not been authorized, and the release date of the item is in the future.); Pending (The order has been placed but payment has not been authorized); Unshipped (Payment has been authorized and the order is ready for shipment, but no items in the order have been shipped); PartiallyShipped (One or more, but not all, items in the order have been shipped); Shipped (All items in the order have been shipped); InvoiceUnconfirmed (All items in the order have been shipped. The seller has not yet given confirmation to Amazon that the invoice has been shipped to the buyer.); Canceled (The order has been canceled); and Unfulfillable (The order cannot be fulfilled. This state applies only to Multi-Channel Fulfillment orders.).
        :param list[str] fulfillment_channels: A list that indicates how an order was fulfilled. Filters the results by fulfillment channel. Possible values: FBA (Fulfillment by Amazon); SellerFulfilled (Fulfilled by the seller).
        :param list[str] payment_methods: A list of payment method values. Used to select orders paid using the specified payment methods. Possible values: COD (Cash on delivery); CVS (Convenience store payment); Other (Any payment method other than COD or CVS).
        :param str buyer_email: The email address of a buyer. Used to select orders that contain the specified email address.
        :param str seller_order_id: An order identifier that is specified by the seller. Used to select only the orders that match the order identifier. If SellerOrderId is specified, then FulfillmentChannels, OrderStatuses, PaymentMethod, LastUpdatedAfter, LastUpdatedBefore, and BuyerEmail cannot be specified.
        :param int max_results_per_page: A number that indicates the maximum number of orders that can be returned per page. Value must be 1 - 100. Default 100.
        :param list[str] easy_ship_shipment_statuses: A list of EasyShipShipmentStatus values. Used to select Easy Ship orders with statuses that match the specified  values. If EasyShipShipmentStatus is specified, only Amazon Easy Ship orders are returned.Possible values: PendingPickUp (Amazon has not yet picked up the package from the seller). LabelCanceled (The seller canceled the pickup). PickedUp (Amazon has picked up the package from the seller). AtOriginFC (The packaged is at the origin fulfillment center). AtDestinationFC (The package is at the destination fulfillment center). OutForDelivery (The package is out for delivery). Damaged (The package was damaged by the carrier). Delivered (The package has been delivered to the buyer). RejectedByBuyer (The package has been rejected by the buyer). Undeliverable (The package cannot be delivered). ReturnedToSeller (The package was not delivered to the buyer and was returned to the seller). ReturningToSeller (The package was not delivered to the buyer and is being returned to the seller).
        :param str next_token: A string token returned in the response of your previous request.
        :param list[str] amazon_order_ids: A list of AmazonOrderId values. An AmazonOrderId is an Amazon-defined order identifier, in 3-7-7 format.
        :param str actual_fulfillment_supply_source_id: Denotes the recommended sourceId where the order should be fulfilled from.
        :param bool is_ispu: When true, this order is marked to be picked up from a store rather than delivered.
        :param str store_chain_store_id: The store chain store identifier. Linked to a specific store in a store chain.
        :return: GetOrdersResponse
        """

        all_params = ['marketplace_ids', 'created_after', 'created_before', 'last_updated_after', 'last_updated_before',
                      'order_statuses', 'fulfillment_channels', 'payment_methods', 'buyer_email', 'seller_order_id',
                      'max_results_per_page', 'easy_ship_shipment_statuses', 'next_token', 'amazon_order_ids',
                      'actual_fulfillment_supply_source_id', 'is_ispu', 'store_chain_store_id']  # noqa: E501
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'marketplace_ids' is set
        if self.api_client.client_side_validation and ('marketplace_ids' not in params or
                                                       params['marketplace_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `marketplace_ids` when calling `get_orders`")  # noqa: E501

        if self.api_client.client_side_validation and ('marketplace_ids' in params and
                                                       len(params['marketplace_ids']) > 50):
            raise ValueError(
                "Invalid value for parameter `marketplace_ids` when calling `get_orders`, number of items must be less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and ('amazon_order_ids' in params and
                                                       len(params['amazon_order_ids']) > 50):
            raise ValueError(
                "Invalid value for parameter `amazon_order_ids` when calling `get_orders`, number of items must be less than or equal to `50`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_after' in params:
            query_params.append(('CreatedAfter', params['created_after']))  # noqa: E501
        if 'created_before' in params:
            query_params.append(('CreatedBefore', params['created_before']))  # noqa: E501
        if 'last_updated_after' in params:
            query_params.append(('LastUpdatedAfter', params['last_updated_after']))  # noqa: E501
        if 'last_updated_before' in params:
            query_params.append(('LastUpdatedBefore', params['last_updated_before']))  # noqa: E501
        if 'order_statuses' in params:
            query_params.append(('OrderStatuses', params['order_statuses']))  # noqa: E501
            collection_formats['OrderStatuses'] = 'csv'  # noqa: E501
        if 'marketplace_ids' in params:
            query_params.append(('MarketplaceIds', params['marketplace_ids']))  # noqa: E501
            collection_formats['MarketplaceIds'] = 'csv'  # noqa: E501
        if 'fulfillment_channels' in params:
            query_params.append(('FulfillmentChannels', params['fulfillment_channels']))  # noqa: E501
            collection_formats['FulfillmentChannels'] = 'csv'  # noqa: E501
        if 'payment_methods' in params:
            query_params.append(('PaymentMethods', params['payment_methods']))  # noqa: E501
            collection_formats['PaymentMethods'] = 'csv'  # noqa: E501
        if 'buyer_email' in params:
            query_params.append(('BuyerEmail', params['buyer_email']))  # noqa: E501
        if 'seller_order_id' in params:
            query_params.append(('SellerOrderId', params['seller_order_id']))  # noqa: E501
        if 'max_results_per_page' in params:
            query_params.append(('MaxResultsPerPage', params['max_results_per_page']))  # noqa: E501
        if 'easy_ship_shipment_statuses' in params:
            query_params.append(('EasyShipShipmentStatuses', params['easy_ship_shipment_statuses']))  # noqa: E501
            collection_formats['EasyShipShipmentStatuses'] = 'csv'  # noqa: E501
        if 'next_token' in params:
            query_params.append(('NextToken', params['next_token']))  # noqa: E501
        if 'amazon_order_ids' in params:
            query_params.append(('AmazonOrderIds', params['amazon_order_ids']))  # noqa: E501
            collection_formats['AmazonOrderIds'] = 'csv'  # noqa: E501
        if 'actual_fulfillment_supply_source_id' in params:
            query_params.append(
                ('ActualFulfillmentSupplySourceId', params['actual_fulfillment_supply_source_id']))  # noqa: E501
        if 'is_ispu' in params:
            query_params.append(('IsISPU', params['is_ispu']))  # noqa: E501
        if 'store_chain_store_id' in params:
            query_params.append(('StoreChainStoreId', params['store_chain_store_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        data = self.api_client.call_api(
            '/orders/v0/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

        if self.api_client.configuration.deserialize:
            tmp_instance = DeSerialize(self.api_client.configuration)
            data = tmp_instance.deserialize(data, 'GetOrdersResponse')
        return data

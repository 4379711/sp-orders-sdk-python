# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class GetOrderAddressResponse(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payload': 'OrderAddress',
        'errors': 'ErrorList'
    }

    attribute_map = {
        'payload': 'payload',
        'errors': 'errors'
    }

    def __init__(self, payload=None, errors=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payload = None
        self._errors = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload
        if errors is not None:
            self.errors = errors

    @property
    def payload(self):
        """Gets the payload of this GetOrderAddressResponse.  # noqa: E501

        The payload for the getOrderAddress operations.  # noqa: E501

        :return: The payload of this GetOrderAddressResponse.  # noqa: E501
        :rtype: OrderAddress
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this GetOrderAddressResponse.

        The payload for the getOrderAddress operations.  # noqa: E501

        :param payload: The payload of this GetOrderAddressResponse.  # noqa: E501
        :type: OrderAddress
        """

        self._payload = payload

    @property
    def errors(self):
        """Gets the errors of this GetOrderAddressResponse.  # noqa: E501

        One or more unexpected errors occurred during the getOrderAddress operation.  # noqa: E501

        :return: The errors of this GetOrderAddressResponse.  # noqa: E501
        :rtype: ErrorList
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this GetOrderAddressResponse.

        One or more unexpected errors occurred during the getOrderAddress operation.  # noqa: E501

        :param errors: The errors of this GetOrderAddressResponse.  # noqa: E501
        :type: ErrorList
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetOrderAddressResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetOrderAddressResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetOrderAddressResponse):
            return True

        return self.to_dict() != other.to_dict()

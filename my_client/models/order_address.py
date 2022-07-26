# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class OrderAddress(object):
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
        'amazon_order_id': 'str',
        'shipping_address': 'Address'
    }

    attribute_map = {
        'amazon_order_id': 'AmazonOrderId',
        'shipping_address': 'ShippingAddress'
    }

    def __init__(self, amazon_order_id=None, shipping_address=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amazon_order_id = None
        self._shipping_address = None
        self.discriminator = None

        self.amazon_order_id = amazon_order_id
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def amazon_order_id(self):
        """Gets the amazon_order_id of this OrderAddress.  # noqa: E501

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :return: The amazon_order_id of this OrderAddress.  # noqa: E501
        :rtype: str
        """
        return self._amazon_order_id

    @amazon_order_id.setter
    def amazon_order_id(self, amazon_order_id):
        """Sets the amazon_order_id of this OrderAddress.

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :param amazon_order_id: The amazon_order_id of this OrderAddress.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and amazon_order_id is None:
            raise ValueError("Invalid value for `amazon_order_id`, must not be `None`")  # noqa: E501

        self._amazon_order_id = amazon_order_id

    @property
    def shipping_address(self):
        """Gets the shipping_address of this OrderAddress.  # noqa: E501


        :return: The shipping_address of this OrderAddress.  # noqa: E501
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this OrderAddress.


        :param shipping_address: The shipping_address of this OrderAddress.  # noqa: E501
        :type: Address
        """

        self._shipping_address = shipping_address

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
        if issubclass(OrderAddress, dict):
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
        if not isinstance(other, OrderAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderAddress):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class ProductInfoDetail(object):
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
        'number_of_items': 'int'
    }

    attribute_map = {
        'number_of_items': 'NumberOfItems'
    }

    def __init__(self, number_of_items=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number_of_items = None
        self.discriminator = None

        if number_of_items is not None:
            self.number_of_items = number_of_items

    @property
    def number_of_items(self):
        """Gets the number_of_items of this ProductInfoDetail.  # noqa: E501

        The total number of items that are included in the ASIN.  # noqa: E501

        :return: The number_of_items of this ProductInfoDetail.  # noqa: E501
        :rtype: int
        """
        return self._number_of_items

    @number_of_items.setter
    def number_of_items(self, number_of_items):
        """Sets the number_of_items of this ProductInfoDetail.

        The total number of items that are included in the ASIN.  # noqa: E501

        :param number_of_items: The number_of_items of this ProductInfoDetail.  # noqa: E501
        :type: int
        """

        self._number_of_items = number_of_items

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
        if issubclass(ProductInfoDetail, dict):
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
        if not isinstance(other, ProductInfoDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductInfoDetail):
            return True

        return self.to_dict() != other.to_dict()

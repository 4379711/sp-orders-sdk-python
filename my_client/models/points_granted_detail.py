# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class PointsGrantedDetail(object):
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
        'points_number': 'int',
        'points_monetary_value': 'Money'
    }

    attribute_map = {
        'points_number': 'PointsNumber',
        'points_monetary_value': 'PointsMonetaryValue'
    }

    def __init__(self, points_number=None, points_monetary_value=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._points_number = None
        self._points_monetary_value = None
        self.discriminator = None

        if points_number is not None:
            self.points_number = points_number
        if points_monetary_value is not None:
            self.points_monetary_value = points_monetary_value

    @property
    def points_number(self):
        """Gets the points_number of this PointsGrantedDetail.  # noqa: E501

        The number of Amazon Points granted with the purchase of an item.  # noqa: E501

        :return: The points_number of this PointsGrantedDetail.  # noqa: E501
        :rtype: int
        """
        return self._points_number

    @points_number.setter
    def points_number(self, points_number):
        """Sets the points_number of this PointsGrantedDetail.

        The number of Amazon Points granted with the purchase of an item.  # noqa: E501

        :param points_number: The points_number of this PointsGrantedDetail.  # noqa: E501
        :type: int
        """

        self._points_number = points_number

    @property
    def points_monetary_value(self):
        """Gets the points_monetary_value of this PointsGrantedDetail.  # noqa: E501

        The monetary value of the Amazon Points granted.  # noqa: E501

        :return: The points_monetary_value of this PointsGrantedDetail.  # noqa: E501
        :rtype: Money
        """
        return self._points_monetary_value

    @points_monetary_value.setter
    def points_monetary_value(self, points_monetary_value):
        """Sets the points_monetary_value of this PointsGrantedDetail.

        The monetary value of the Amazon Points granted.  # noqa: E501

        :param points_monetary_value: The points_monetary_value of this PointsGrantedDetail.  # noqa: E501
        :type: Money
        """

        self._points_monetary_value = points_monetary_value

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
        if issubclass(PointsGrantedDetail, dict):
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
        if not isinstance(other, PointsGrantedDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PointsGrantedDetail):
            return True

        return self.to_dict() != other.to_dict()

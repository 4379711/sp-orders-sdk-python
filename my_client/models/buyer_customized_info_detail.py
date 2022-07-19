# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class BuyerCustomizedInfoDetail(object):
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
        'customized_url': 'str'
    }

    attribute_map = {
        'customized_url': 'CustomizedURL'
    }

    def __init__(self, customized_url=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customized_url = None
        self.discriminator = None

        if customized_url is not None:
            self.customized_url = customized_url

    @property
    def customized_url(self):
        """Gets the customized_url of this BuyerCustomizedInfoDetail.  # noqa: E501

        The location of a zip file containing Amazon Custom data.  # noqa: E501

        :return: The customized_url of this BuyerCustomizedInfoDetail.  # noqa: E501
        :rtype: str
        """
        return self._customized_url

    @customized_url.setter
    def customized_url(self, customized_url):
        """Sets the customized_url of this BuyerCustomizedInfoDetail.

        The location of a zip file containing Amazon Custom data.  # noqa: E501

        :param customized_url: The customized_url of this BuyerCustomizedInfoDetail.  # noqa: E501
        :type: str
        """

        self._customized_url = customized_url

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
        if issubclass(BuyerCustomizedInfoDetail, dict):
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
        if not isinstance(other, BuyerCustomizedInfoDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyerCustomizedInfoDetail):
            return True

        return self.to_dict() != other.to_dict()

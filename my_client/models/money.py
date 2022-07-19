# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class Money(object):
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
        'currency_code': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'currency_code': 'CurrencyCode',
        'amount': 'Amount'
    }

    def __init__(self, currency_code=None, amount=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._currency_code = None
        self._amount = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if amount is not None:
            self.amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this Money.  # noqa: E501

        The three-digit currency code. In ISO 4217 format.  # noqa: E501

        :return: The currency_code of this Money.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this Money.

        The three-digit currency code. In ISO 4217 format.  # noqa: E501

        :param currency_code: The currency_code of this Money.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def amount(self):
        """Gets the amount of this Money.  # noqa: E501

        The currency amount.  # noqa: E501

        :return: The amount of this Money.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Money.

        The currency amount.  # noqa: E501

        :param amount: The amount of this Money.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if issubclass(Money, dict):
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
        if not isinstance(other, Money):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Money):
            return True

        return self.to_dict() != other.to_dict()

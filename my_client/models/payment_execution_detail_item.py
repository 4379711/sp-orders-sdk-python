# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class PaymentExecutionDetailItem(object):
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
        'payment': 'Money',
        'payment_method': 'str'
    }

    attribute_map = {
        'payment': 'Payment',
        'payment_method': 'PaymentMethod'
    }

    def __init__(self, payment=None, payment_method=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._payment = None
        self._payment_method = None
        self.discriminator = None

        self.payment = payment
        self.payment_method = payment_method

    @property
    def payment(self):
        """Gets the payment of this PaymentExecutionDetailItem.  # noqa: E501


        :return: The payment of this PaymentExecutionDetailItem.  # noqa: E501
        :rtype: Money
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this PaymentExecutionDetailItem.


        :param payment: The payment of this PaymentExecutionDetailItem.  # noqa: E501
        :type: Money
        """
        if self._configuration.client_side_validation and payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentExecutionDetailItem.  # noqa: E501

        A sub-payment method for a COD order.  Possible values:  * COD - Cash On Delivery.  * GC - Gift Card.  * PointsAccount - Amazon Points.  # noqa: E501

        :return: The payment_method of this PaymentExecutionDetailItem.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentExecutionDetailItem.

        A sub-payment method for a COD order.  Possible values:  * COD - Cash On Delivery.  * GC - Gift Card.  * PointsAccount - Amazon Points.  # noqa: E501

        :param payment_method: The payment_method of this PaymentExecutionDetailItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

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
        if issubclass(PaymentExecutionDetailItem, dict):
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
        if not isinstance(other, PaymentExecutionDetailItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentExecutionDetailItem):
            return True

        return self.to_dict() != other.to_dict()

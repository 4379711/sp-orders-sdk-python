# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class OrdersList(object):
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
        'orders': 'OrderList',
        'next_token': 'str',
        'last_updated_before': 'str',
        'created_before': 'str'
    }

    attribute_map = {
        'orders': 'Orders',
        'next_token': 'NextToken',
        'last_updated_before': 'LastUpdatedBefore',
        'created_before': 'CreatedBefore'
    }

    def __init__(self, orders=None, next_token=None, last_updated_before=None, created_before=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._orders = None
        self._next_token = None
        self._last_updated_before = None
        self._created_before = None
        self.discriminator = None

        self.orders = orders
        if next_token is not None:
            self.next_token = next_token
        if last_updated_before is not None:
            self.last_updated_before = last_updated_before
        if created_before is not None:
            self.created_before = created_before

    @property
    def orders(self):
        """Gets the orders of this OrdersList.  # noqa: E501


        :return: The orders of this OrdersList.  # noqa: E501
        :rtype: OrderList
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this OrdersList.


        :param orders: The orders of this OrdersList.  # noqa: E501
        :type: OrderList
        """
        if self._configuration.client_side_validation and orders is None:
            raise ValueError("Invalid value for `orders`, must not be `None`")  # noqa: E501

        self._orders = orders

    @property
    def next_token(self):
        """Gets the next_token of this OrdersList.  # noqa: E501

        When present and not empty, pass this string token in the next request to return the next response page.  # noqa: E501

        :return: The next_token of this OrdersList.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this OrdersList.

        When present and not empty, pass this string token in the next request to return the next response page.  # noqa: E501

        :param next_token: The next_token of this OrdersList.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def last_updated_before(self):
        """Gets the last_updated_before of this OrdersList.  # noqa: E501

        A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. All dates must be in ISO 8601 format.  # noqa: E501

        :return: The last_updated_before of this OrdersList.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_before

    @last_updated_before.setter
    def last_updated_before(self, last_updated_before):
        """Sets the last_updated_before of this OrdersList.

        A date used for selecting orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. All dates must be in ISO 8601 format.  # noqa: E501

        :param last_updated_before: The last_updated_before of this OrdersList.  # noqa: E501
        :type: str
        """

        self._last_updated_before = last_updated_before

    @property
    def created_before(self):
        """Gets the created_before of this OrdersList.  # noqa: E501

        A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in ISO 8601 format.  # noqa: E501

        :return: The created_before of this OrdersList.  # noqa: E501
        :rtype: str
        """
        return self._created_before

    @created_before.setter
    def created_before(self, created_before):
        """Sets the created_before of this OrdersList.

        A date used for selecting orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in ISO 8601 format.  # noqa: E501

        :param created_before: The created_before of this OrdersList.  # noqa: E501
        :type: str
        """

        self._created_before = created_before

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
        if issubclass(OrdersList, dict):
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
        if not isinstance(other, OrdersList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrdersList):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class OrderItemBuyerInfo(object):
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
        'order_item_id': 'str',
        'buyer_customized_info': 'BuyerCustomizedInfoDetail',
        'gift_wrap_price': 'Money',
        'gift_wrap_tax': 'Money',
        'gift_message_text': 'str',
        'gift_wrap_level': 'str'
    }

    attribute_map = {
        'order_item_id': 'OrderItemId',
        'buyer_customized_info': 'BuyerCustomizedInfo',
        'gift_wrap_price': 'GiftWrapPrice',
        'gift_wrap_tax': 'GiftWrapTax',
        'gift_message_text': 'GiftMessageText',
        'gift_wrap_level': 'GiftWrapLevel'
    }

    def __init__(self, order_item_id=None, buyer_customized_info=None, gift_wrap_price=None, gift_wrap_tax=None, gift_message_text=None, gift_wrap_level=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._order_item_id = None
        self._buyer_customized_info = None
        self._gift_wrap_price = None
        self._gift_wrap_tax = None
        self._gift_message_text = None
        self._gift_wrap_level = None
        self.discriminator = None

        self.order_item_id = order_item_id
        if buyer_customized_info is not None:
            self.buyer_customized_info = buyer_customized_info
        if gift_wrap_price is not None:
            self.gift_wrap_price = gift_wrap_price
        if gift_wrap_tax is not None:
            self.gift_wrap_tax = gift_wrap_tax
        if gift_message_text is not None:
            self.gift_message_text = gift_message_text
        if gift_wrap_level is not None:
            self.gift_wrap_level = gift_wrap_level

    @property
    def order_item_id(self):
        """Gets the order_item_id of this OrderItemBuyerInfo.  # noqa: E501

        An Amazon-defined order item identifier.  # noqa: E501

        :return: The order_item_id of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """Sets the order_item_id of this OrderItemBuyerInfo.

        An Amazon-defined order item identifier.  # noqa: E501

        :param order_item_id: The order_item_id of this OrderItemBuyerInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and order_item_id is None:
            raise ValueError("Invalid value for `order_item_id`, must not be `None`")  # noqa: E501

        self._order_item_id = order_item_id

    @property
    def buyer_customized_info(self):
        """Gets the buyer_customized_info of this OrderItemBuyerInfo.  # noqa: E501

        Buyer information for custom orders from the Amazon Custom program.  # noqa: E501

        :return: The buyer_customized_info of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: BuyerCustomizedInfoDetail
        """
        return self._buyer_customized_info

    @buyer_customized_info.setter
    def buyer_customized_info(self, buyer_customized_info):
        """Sets the buyer_customized_info of this OrderItemBuyerInfo.

        Buyer information for custom orders from the Amazon Custom program.  # noqa: E501

        :param buyer_customized_info: The buyer_customized_info of this OrderItemBuyerInfo.  # noqa: E501
        :type: BuyerCustomizedInfoDetail
        """

        self._buyer_customized_info = buyer_customized_info

    @property
    def gift_wrap_price(self):
        """Gets the gift_wrap_price of this OrderItemBuyerInfo.  # noqa: E501

        The gift wrap price of the item.  # noqa: E501

        :return: The gift_wrap_price of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: Money
        """
        return self._gift_wrap_price

    @gift_wrap_price.setter
    def gift_wrap_price(self, gift_wrap_price):
        """Sets the gift_wrap_price of this OrderItemBuyerInfo.

        The gift wrap price of the item.  # noqa: E501

        :param gift_wrap_price: The gift_wrap_price of this OrderItemBuyerInfo.  # noqa: E501
        :type: Money
        """

        self._gift_wrap_price = gift_wrap_price

    @property
    def gift_wrap_tax(self):
        """Gets the gift_wrap_tax of this OrderItemBuyerInfo.  # noqa: E501

        The tax on the gift wrap price.  # noqa: E501

        :return: The gift_wrap_tax of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: Money
        """
        return self._gift_wrap_tax

    @gift_wrap_tax.setter
    def gift_wrap_tax(self, gift_wrap_tax):
        """Sets the gift_wrap_tax of this OrderItemBuyerInfo.

        The tax on the gift wrap price.  # noqa: E501

        :param gift_wrap_tax: The gift_wrap_tax of this OrderItemBuyerInfo.  # noqa: E501
        :type: Money
        """

        self._gift_wrap_tax = gift_wrap_tax

    @property
    def gift_message_text(self):
        """Gets the gift_message_text of this OrderItemBuyerInfo.  # noqa: E501

        A gift message provided by the buyer.  # noqa: E501

        :return: The gift_message_text of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._gift_message_text

    @gift_message_text.setter
    def gift_message_text(self, gift_message_text):
        """Sets the gift_message_text of this OrderItemBuyerInfo.

        A gift message provided by the buyer.  # noqa: E501

        :param gift_message_text: The gift_message_text of this OrderItemBuyerInfo.  # noqa: E501
        :type: str
        """

        self._gift_message_text = gift_message_text

    @property
    def gift_wrap_level(self):
        """Gets the gift_wrap_level of this OrderItemBuyerInfo.  # noqa: E501

        The gift wrap level specified by the buyer.  # noqa: E501

        :return: The gift_wrap_level of this OrderItemBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._gift_wrap_level

    @gift_wrap_level.setter
    def gift_wrap_level(self, gift_wrap_level):
        """Sets the gift_wrap_level of this OrderItemBuyerInfo.

        The gift wrap level specified by the buyer.  # noqa: E501

        :param gift_wrap_level: The gift_wrap_level of this OrderItemBuyerInfo.  # noqa: E501
        :type: str
        """

        self._gift_wrap_level = gift_wrap_level

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
        if issubclass(OrderItemBuyerInfo, dict):
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
        if not isinstance(other, OrderItemBuyerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderItemBuyerInfo):
            return True

        return self.to_dict() != other.to_dict()

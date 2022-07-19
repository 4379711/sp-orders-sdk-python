# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class OrderBuyerInfo(object):
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
        'buyer_email': 'str',
        'buyer_name': 'str',
        'buyer_county': 'str',
        'buyer_tax_info': 'BuyerTaxInfo',
        'purchase_order_number': 'str'
    }

    attribute_map = {
        'amazon_order_id': 'AmazonOrderId',
        'buyer_email': 'BuyerEmail',
        'buyer_name': 'BuyerName',
        'buyer_county': 'BuyerCounty',
        'buyer_tax_info': 'BuyerTaxInfo',
        'purchase_order_number': 'PurchaseOrderNumber'
    }

    def __init__(self, amazon_order_id=None, buyer_email=None, buyer_name=None, buyer_county=None, buyer_tax_info=None, purchase_order_number=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amazon_order_id = None
        self._buyer_email = None
        self._buyer_name = None
        self._buyer_county = None
        self._buyer_tax_info = None
        self._purchase_order_number = None
        self.discriminator = None

        self.amazon_order_id = amazon_order_id
        if buyer_email is not None:
            self.buyer_email = buyer_email
        if buyer_name is not None:
            self.buyer_name = buyer_name
        if buyer_county is not None:
            self.buyer_county = buyer_county
        if buyer_tax_info is not None:
            self.buyer_tax_info = buyer_tax_info
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number

    @property
    def amazon_order_id(self):
        """Gets the amazon_order_id of this OrderBuyerInfo.  # noqa: E501

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :return: The amazon_order_id of this OrderBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._amazon_order_id

    @amazon_order_id.setter
    def amazon_order_id(self, amazon_order_id):
        """Sets the amazon_order_id of this OrderBuyerInfo.

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :param amazon_order_id: The amazon_order_id of this OrderBuyerInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and amazon_order_id is None:
            raise ValueError("Invalid value for `amazon_order_id`, must not be `None`")  # noqa: E501

        self._amazon_order_id = amazon_order_id

    @property
    def buyer_email(self):
        """Gets the buyer_email of this OrderBuyerInfo.  # noqa: E501

        The anonymized email address of the buyer.  # noqa: E501

        :return: The buyer_email of this OrderBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._buyer_email

    @buyer_email.setter
    def buyer_email(self, buyer_email):
        """Sets the buyer_email of this OrderBuyerInfo.

        The anonymized email address of the buyer.  # noqa: E501

        :param buyer_email: The buyer_email of this OrderBuyerInfo.  # noqa: E501
        :type: str
        """

        self._buyer_email = buyer_email

    @property
    def buyer_name(self):
        """Gets the buyer_name of this OrderBuyerInfo.  # noqa: E501

        The name of the buyer.  # noqa: E501

        :return: The buyer_name of this OrderBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        """Sets the buyer_name of this OrderBuyerInfo.

        The name of the buyer.  # noqa: E501

        :param buyer_name: The buyer_name of this OrderBuyerInfo.  # noqa: E501
        :type: str
        """

        self._buyer_name = buyer_name

    @property
    def buyer_county(self):
        """Gets the buyer_county of this OrderBuyerInfo.  # noqa: E501

        The county of the buyer.  # noqa: E501

        :return: The buyer_county of this OrderBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._buyer_county

    @buyer_county.setter
    def buyer_county(self, buyer_county):
        """Sets the buyer_county of this OrderBuyerInfo.

        The county of the buyer.  # noqa: E501

        :param buyer_county: The buyer_county of this OrderBuyerInfo.  # noqa: E501
        :type: str
        """

        self._buyer_county = buyer_county

    @property
    def buyer_tax_info(self):
        """Gets the buyer_tax_info of this OrderBuyerInfo.  # noqa: E501

        Tax information about the buyer.  # noqa: E501

        :return: The buyer_tax_info of this OrderBuyerInfo.  # noqa: E501
        :rtype: BuyerTaxInfo
        """
        return self._buyer_tax_info

    @buyer_tax_info.setter
    def buyer_tax_info(self, buyer_tax_info):
        """Sets the buyer_tax_info of this OrderBuyerInfo.

        Tax information about the buyer.  # noqa: E501

        :param buyer_tax_info: The buyer_tax_info of this OrderBuyerInfo.  # noqa: E501
        :type: BuyerTaxInfo
        """

        self._buyer_tax_info = buyer_tax_info

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this OrderBuyerInfo.  # noqa: E501

        The purchase order (PO) number entered by the buyer at checkout. Returned only for orders where the buyer entered a PO number at checkout.  # noqa: E501

        :return: The purchase_order_number of this OrderBuyerInfo.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this OrderBuyerInfo.

        The purchase order (PO) number entered by the buyer at checkout. Returned only for orders where the buyer entered a PO number at checkout.  # noqa: E501

        :param purchase_order_number: The purchase_order_number of this OrderBuyerInfo.  # noqa: E501
        :type: str
        """

        self._purchase_order_number = purchase_order_number

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
        if issubclass(OrderBuyerInfo, dict):
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
        if not isinstance(other, OrderBuyerInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderBuyerInfo):
            return True

        return self.to_dict() != other.to_dict()

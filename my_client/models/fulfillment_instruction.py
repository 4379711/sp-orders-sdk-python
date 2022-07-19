# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class FulfillmentInstruction(object):
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
        'fulfillment_supply_source_id': 'str'
    }

    attribute_map = {
        'fulfillment_supply_source_id': 'FulfillmentSupplySourceId'
    }

    def __init__(self, fulfillment_supply_source_id=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fulfillment_supply_source_id = None
        self.discriminator = None

        if fulfillment_supply_source_id is not None:
            self.fulfillment_supply_source_id = fulfillment_supply_source_id

    @property
    def fulfillment_supply_source_id(self):
        """Gets the fulfillment_supply_source_id of this FulfillmentInstruction.  # noqa: E501

        Denotes the recommended sourceId where the order should be fulfilled from.  # noqa: E501

        :return: The fulfillment_supply_source_id of this FulfillmentInstruction.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_supply_source_id

    @fulfillment_supply_source_id.setter
    def fulfillment_supply_source_id(self, fulfillment_supply_source_id):
        """Sets the fulfillment_supply_source_id of this FulfillmentInstruction.

        Denotes the recommended sourceId where the order should be fulfilled from.  # noqa: E501

        :param fulfillment_supply_source_id: The fulfillment_supply_source_id of this FulfillmentInstruction.  # noqa: E501
        :type: str
        """

        self._fulfillment_supply_source_id = fulfillment_supply_source_id

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
        if issubclass(FulfillmentInstruction, dict):
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
        if not isinstance(other, FulfillmentInstruction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FulfillmentInstruction):
            return True

        return self.to_dict() != other.to_dict()

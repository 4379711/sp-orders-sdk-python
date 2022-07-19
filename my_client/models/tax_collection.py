# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class TaxCollection(object):
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
        'model': 'str',
        'responsible_party': 'str'
    }

    attribute_map = {
        'model': 'Model',
        'responsible_party': 'ResponsibleParty'
    }

    def __init__(self, model=None, responsible_party=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model = None
        self._responsible_party = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if responsible_party is not None:
            self.responsible_party = responsible_party

    @property
    def model(self):
        """Gets the model of this TaxCollection.  # noqa: E501

        The tax collection model applied to the item.  # noqa: E501

        :return: The model of this TaxCollection.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this TaxCollection.

        The tax collection model applied to the item.  # noqa: E501

        :param model: The model of this TaxCollection.  # noqa: E501
        :type: str
        """
        allowed_values = ["MarketplaceFacilitator"]  # noqa: E501
        if (self._configuration.client_side_validation and
                model not in allowed_values):
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"  # noqa: E501
                .format(model, allowed_values)
            )

        self._model = model

    @property
    def responsible_party(self):
        """Gets the responsible_party of this TaxCollection.  # noqa: E501

        The party responsible for withholding the taxes and remitting them to the taxing authority.  # noqa: E501

        :return: The responsible_party of this TaxCollection.  # noqa: E501
        :rtype: str
        """
        return self._responsible_party

    @responsible_party.setter
    def responsible_party(self, responsible_party):
        """Sets the responsible_party of this TaxCollection.

        The party responsible for withholding the taxes and remitting them to the taxing authority.  # noqa: E501

        :param responsible_party: The responsible_party of this TaxCollection.  # noqa: E501
        :type: str
        """
        allowed_values = ["Amazon Services, Inc."]  # noqa: E501
        if (self._configuration.client_side_validation and
                responsible_party not in allowed_values):
            raise ValueError(
                "Invalid value for `responsible_party` ({0}), must be one of {1}"  # noqa: E501
                .format(responsible_party, allowed_values)
            )

        self._responsible_party = responsible_party

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
        if issubclass(TaxCollection, dict):
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
        if not isinstance(other, TaxCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaxCollection):
            return True

        return self.to_dict() != other.to_dict()

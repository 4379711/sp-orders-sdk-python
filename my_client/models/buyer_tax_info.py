# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class BuyerTaxInfo(object):
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
        'company_legal_name': 'str',
        'taxing_region': 'str',
        'tax_classifications': 'list[TaxClassification]'
    }

    attribute_map = {
        'company_legal_name': 'CompanyLegalName',
        'taxing_region': 'TaxingRegion',
        'tax_classifications': 'TaxClassifications'
    }

    def __init__(self, company_legal_name=None, taxing_region=None, tax_classifications=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._company_legal_name = None
        self._taxing_region = None
        self._tax_classifications = None
        self.discriminator = None

        if company_legal_name is not None:
            self.company_legal_name = company_legal_name
        if taxing_region is not None:
            self.taxing_region = taxing_region
        if tax_classifications is not None:
            self.tax_classifications = tax_classifications

    @property
    def company_legal_name(self):
        """Gets the company_legal_name of this BuyerTaxInfo.  # noqa: E501

        The legal name of the company.  # noqa: E501

        :return: The company_legal_name of this BuyerTaxInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_legal_name

    @company_legal_name.setter
    def company_legal_name(self, company_legal_name):
        """Sets the company_legal_name of this BuyerTaxInfo.

        The legal name of the company.  # noqa: E501

        :param company_legal_name: The company_legal_name of this BuyerTaxInfo.  # noqa: E501
        :type: str
        """

        self._company_legal_name = company_legal_name

    @property
    def taxing_region(self):
        """Gets the taxing_region of this BuyerTaxInfo.  # noqa: E501

        The country or region imposing the tax.  # noqa: E501

        :return: The taxing_region of this BuyerTaxInfo.  # noqa: E501
        :rtype: str
        """
        return self._taxing_region

    @taxing_region.setter
    def taxing_region(self, taxing_region):
        """Sets the taxing_region of this BuyerTaxInfo.

        The country or region imposing the tax.  # noqa: E501

        :param taxing_region: The taxing_region of this BuyerTaxInfo.  # noqa: E501
        :type: str
        """

        self._taxing_region = taxing_region

    @property
    def tax_classifications(self):
        """Gets the tax_classifications of this BuyerTaxInfo.  # noqa: E501

        A list of tax classifications that apply to the order.  # noqa: E501

        :return: The tax_classifications of this BuyerTaxInfo.  # noqa: E501
        :rtype: list[TaxClassification]
        """
        return self._tax_classifications

    @tax_classifications.setter
    def tax_classifications(self, tax_classifications):
        """Sets the tax_classifications of this BuyerTaxInfo.

        A list of tax classifications that apply to the order.  # noqa: E501

        :param tax_classifications: The tax_classifications of this BuyerTaxInfo.  # noqa: E501
        :type: list[TaxClassification]
        """

        self._tax_classifications = tax_classifications

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
        if issubclass(BuyerTaxInfo, dict):
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
        if not isinstance(other, BuyerTaxInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuyerTaxInfo):
            return True

        return self.to_dict() != other.to_dict()

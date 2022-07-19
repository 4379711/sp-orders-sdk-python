# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class Address(object):
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
        'name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'city': 'str',
        'county': 'str',
        'district': 'str',
        'state_or_region': 'str',
        'municipality': 'str',
        'postal_code': 'str',
        'country_code': 'str',
        'phone': 'str',
        'address_type': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'address_line1': 'AddressLine1',
        'address_line2': 'AddressLine2',
        'address_line3': 'AddressLine3',
        'city': 'City',
        'county': 'County',
        'district': 'District',
        'state_or_region': 'StateOrRegion',
        'municipality': 'Municipality',
        'postal_code': 'PostalCode',
        'country_code': 'CountryCode',
        'phone': 'Phone',
        'address_type': 'AddressType'
    }

    def __init__(self, name=None, address_line1=None, address_line2=None, address_line3=None, city=None, county=None, district=None, state_or_region=None, municipality=None, postal_code=None, country_code=None, phone=None, address_type=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._city = None
        self._county = None
        self._district = None
        self._state_or_region = None
        self._municipality = None
        self._postal_code = None
        self._country_code = None
        self._phone = None
        self._address_type = None
        self.discriminator = None

        self.name = name
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if city is not None:
            self.city = city
        if county is not None:
            self.county = county
        if district is not None:
            self.district = district
        if state_or_region is not None:
            self.state_or_region = state_or_region
        if municipality is not None:
            self.municipality = municipality
        if postal_code is not None:
            self.postal_code = postal_code
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone
        if address_type is not None:
            self.address_type = address_type

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        The name.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        The name.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        The street address.  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        The street address.  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        Additional street address information, if required.  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        Additional street address information, if required.  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this Address.  # noqa: E501

        Additional street address information, if required.  # noqa: E501

        :return: The address_line3 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this Address.

        Additional street address information, if required.  # noqa: E501

        :param address_line3: The address_line3 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line3 = address_line3

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        The city   # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        The city   # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def county(self):
        """Gets the county of this Address.  # noqa: E501

        The county.  # noqa: E501

        :return: The county of this Address.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this Address.

        The county.  # noqa: E501

        :param county: The county of this Address.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def district(self):
        """Gets the district of this Address.  # noqa: E501

        The district.  # noqa: E501

        :return: The district of this Address.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this Address.

        The district.  # noqa: E501

        :param district: The district of this Address.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def state_or_region(self):
        """Gets the state_or_region of this Address.  # noqa: E501

        The state or region.  # noqa: E501

        :return: The state_or_region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state_or_region

    @state_or_region.setter
    def state_or_region(self, state_or_region):
        """Sets the state_or_region of this Address.

        The state or region.  # noqa: E501

        :param state_or_region: The state_or_region of this Address.  # noqa: E501
        :type: str
        """

        self._state_or_region = state_or_region

    @property
    def municipality(self):
        """Gets the municipality of this Address.  # noqa: E501

        The municipality.  # noqa: E501

        :return: The municipality of this Address.  # noqa: E501
        :rtype: str
        """
        return self._municipality

    @municipality.setter
    def municipality(self, municipality):
        """Sets the municipality of this Address.

        The municipality.  # noqa: E501

        :param municipality: The municipality of this Address.  # noqa: E501
        :type: str
        """

        self._municipality = municipality

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        The postal code.  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        The postal code.  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this Address.  # noqa: E501

        The country code. A two-character country code, in ISO 3166-1 alpha-2 format.  # noqa: E501

        :return: The country_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Address.

        The country code. A two-character country code, in ISO 3166-1 alpha-2 format.  # noqa: E501

        :param country_code: The country_code of this Address.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def phone(self):
        """Gets the phone of this Address.  # noqa: E501

        The phone number. Not returned for Fulfillment by Amazon (FBA) orders.  # noqa: E501

        :return: The phone of this Address.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Address.

        The phone number. Not returned for Fulfillment by Amazon (FBA) orders.  # noqa: E501

        :param phone: The phone of this Address.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address_type(self):
        """Gets the address_type of this Address.  # noqa: E501

        The address type of the shipping address.  # noqa: E501

        :return: The address_type of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Address.

        The address type of the shipping address.  # noqa: E501

        :param address_type: The address_type of this Address.  # noqa: E501
        :type: str
        """
        allowed_values = ["Residential", "Commercial"]  # noqa: E501
        if (self._configuration.client_side_validation and
                address_type not in allowed_values):
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
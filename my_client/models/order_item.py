# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class OrderItem(object):
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
        'asin': 'str',
        'seller_sku': 'str',
        'order_item_id': 'str',
        'title': 'str',
        'quantity_ordered': 'int',
        'quantity_shipped': 'int',
        'product_info': 'ProductInfoDetail',
        'points_granted': 'PointsGrantedDetail',
        'item_price': 'Money',
        'shipping_price': 'Money',
        'item_tax': 'Money',
        'shipping_tax': 'Money',
        'shipping_discount': 'Money',
        'shipping_discount_tax': 'Money',
        'promotion_discount': 'Money',
        'promotion_discount_tax': 'Money',
        'promotion_ids': 'PromotionIdList',
        'cod_fee': 'Money',
        'cod_fee_discount': 'Money',
        'is_gift': 'bool',
        'condition_note': 'str',
        'condition_id': 'str',
        'condition_subtype_id': 'str',
        'scheduled_delivery_start_date': 'str',
        'scheduled_delivery_end_date': 'str',
        'price_designation': 'str',
        'tax_collection': 'TaxCollection',
        'serial_number_required': 'bool',
        'is_transparency': 'bool',
        'ioss_number': 'str',
        'store_chain_store_id': 'str',
        'deemed_reseller_category': 'str'
    }

    attribute_map = {
        'asin': 'ASIN',
        'seller_sku': 'SellerSKU',
        'order_item_id': 'OrderItemId',
        'title': 'Title',
        'quantity_ordered': 'QuantityOrdered',
        'quantity_shipped': 'QuantityShipped',
        'product_info': 'ProductInfo',
        'points_granted': 'PointsGranted',
        'item_price': 'ItemPrice',
        'shipping_price': 'ShippingPrice',
        'item_tax': 'ItemTax',
        'shipping_tax': 'ShippingTax',
        'shipping_discount': 'ShippingDiscount',
        'shipping_discount_tax': 'ShippingDiscountTax',
        'promotion_discount': 'PromotionDiscount',
        'promotion_discount_tax': 'PromotionDiscountTax',
        'promotion_ids': 'PromotionIds',
        'cod_fee': 'CODFee',
        'cod_fee_discount': 'CODFeeDiscount',
        'is_gift': 'IsGift',
        'condition_note': 'ConditionNote',
        'condition_id': 'ConditionId',
        'condition_subtype_id': 'ConditionSubtypeId',
        'scheduled_delivery_start_date': 'ScheduledDeliveryStartDate',
        'scheduled_delivery_end_date': 'ScheduledDeliveryEndDate',
        'price_designation': 'PriceDesignation',
        'tax_collection': 'TaxCollection',
        'serial_number_required': 'SerialNumberRequired',
        'is_transparency': 'IsTransparency',
        'ioss_number': 'IossNumber',
        'store_chain_store_id': 'StoreChainStoreId',
        'deemed_reseller_category': 'DeemedResellerCategory'
    }

    def __init__(self, asin=None, seller_sku=None, order_item_id=None, title=None, quantity_ordered=None, quantity_shipped=None, product_info=None, points_granted=None, item_price=None, shipping_price=None, item_tax=None, shipping_tax=None, shipping_discount=None, shipping_discount_tax=None, promotion_discount=None, promotion_discount_tax=None, promotion_ids=None, cod_fee=None, cod_fee_discount=None, is_gift=None, condition_note=None, condition_id=None, condition_subtype_id=None, scheduled_delivery_start_date=None, scheduled_delivery_end_date=None, price_designation=None, tax_collection=None, serial_number_required=None, is_transparency=None, ioss_number=None, store_chain_store_id=None, deemed_reseller_category=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asin = None
        self._seller_sku = None
        self._order_item_id = None
        self._title = None
        self._quantity_ordered = None
        self._quantity_shipped = None
        self._product_info = None
        self._points_granted = None
        self._item_price = None
        self._shipping_price = None
        self._item_tax = None
        self._shipping_tax = None
        self._shipping_discount = None
        self._shipping_discount_tax = None
        self._promotion_discount = None
        self._promotion_discount_tax = None
        self._promotion_ids = None
        self._cod_fee = None
        self._cod_fee_discount = None
        self._is_gift = None
        self._condition_note = None
        self._condition_id = None
        self._condition_subtype_id = None
        self._scheduled_delivery_start_date = None
        self._scheduled_delivery_end_date = None
        self._price_designation = None
        self._tax_collection = None
        self._serial_number_required = None
        self._is_transparency = None
        self._ioss_number = None
        self._store_chain_store_id = None
        self._deemed_reseller_category = None
        self.discriminator = None

        self.asin = asin
        if seller_sku is not None:
            self.seller_sku = seller_sku
        self.order_item_id = order_item_id
        if title is not None:
            self.title = title
        self.quantity_ordered = quantity_ordered
        if quantity_shipped is not None:
            self.quantity_shipped = quantity_shipped
        if product_info is not None:
            self.product_info = product_info
        if points_granted is not None:
            self.points_granted = points_granted
        if item_price is not None:
            self.item_price = item_price
        if shipping_price is not None:
            self.shipping_price = shipping_price
        if item_tax is not None:
            self.item_tax = item_tax
        if shipping_tax is not None:
            self.shipping_tax = shipping_tax
        if shipping_discount is not None:
            self.shipping_discount = shipping_discount
        if shipping_discount_tax is not None:
            self.shipping_discount_tax = shipping_discount_tax
        if promotion_discount is not None:
            self.promotion_discount = promotion_discount
        if promotion_discount_tax is not None:
            self.promotion_discount_tax = promotion_discount_tax
        if promotion_ids is not None:
            self.promotion_ids = promotion_ids
        if cod_fee is not None:
            self.cod_fee = cod_fee
        if cod_fee_discount is not None:
            self.cod_fee_discount = cod_fee_discount
        if is_gift is not None:
            self.is_gift = is_gift
        if condition_note is not None:
            self.condition_note = condition_note
        if condition_id is not None:
            self.condition_id = condition_id
        if condition_subtype_id is not None:
            self.condition_subtype_id = condition_subtype_id
        if scheduled_delivery_start_date is not None:
            self.scheduled_delivery_start_date = scheduled_delivery_start_date
        if scheduled_delivery_end_date is not None:
            self.scheduled_delivery_end_date = scheduled_delivery_end_date
        if price_designation is not None:
            self.price_designation = price_designation
        if tax_collection is not None:
            self.tax_collection = tax_collection
        if serial_number_required is not None:
            self.serial_number_required = serial_number_required
        if is_transparency is not None:
            self.is_transparency = is_transparency
        if ioss_number is not None:
            self.ioss_number = ioss_number
        if store_chain_store_id is not None:
            self.store_chain_store_id = store_chain_store_id
        if deemed_reseller_category is not None:
            self.deemed_reseller_category = deemed_reseller_category

    @property
    def asin(self):
        """Gets the asin of this OrderItem.  # noqa: E501

        The Amazon Standard Identification Number (ASIN) of the item.  # noqa: E501

        :return: The asin of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._asin

    @asin.setter
    def asin(self, asin):
        """Sets the asin of this OrderItem.

        The Amazon Standard Identification Number (ASIN) of the item.  # noqa: E501

        :param asin: The asin of this OrderItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and asin is None:
            raise ValueError("Invalid value for `asin`, must not be `None`")  # noqa: E501

        self._asin = asin

    @property
    def seller_sku(self):
        """Gets the seller_sku of this OrderItem.  # noqa: E501

        The seller stock keeping unit (SKU) of the item.  # noqa: E501

        :return: The seller_sku of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._seller_sku

    @seller_sku.setter
    def seller_sku(self, seller_sku):
        """Sets the seller_sku of this OrderItem.

        The seller stock keeping unit (SKU) of the item.  # noqa: E501

        :param seller_sku: The seller_sku of this OrderItem.  # noqa: E501
        :type: str
        """

        self._seller_sku = seller_sku

    @property
    def order_item_id(self):
        """Gets the order_item_id of this OrderItem.  # noqa: E501

        An Amazon-defined order item identifier.  # noqa: E501

        :return: The order_item_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """Sets the order_item_id of this OrderItem.

        An Amazon-defined order item identifier.  # noqa: E501

        :param order_item_id: The order_item_id of this OrderItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and order_item_id is None:
            raise ValueError("Invalid value for `order_item_id`, must not be `None`")  # noqa: E501

        self._order_item_id = order_item_id

    @property
    def title(self):
        """Gets the title of this OrderItem.  # noqa: E501

        The name of the item.  # noqa: E501

        :return: The title of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OrderItem.

        The name of the item.  # noqa: E501

        :param title: The title of this OrderItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def quantity_ordered(self):
        """Gets the quantity_ordered of this OrderItem.  # noqa: E501

        The number of items in the order.   # noqa: E501

        :return: The quantity_ordered of this OrderItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity_ordered

    @quantity_ordered.setter
    def quantity_ordered(self, quantity_ordered):
        """Sets the quantity_ordered of this OrderItem.

        The number of items in the order.   # noqa: E501

        :param quantity_ordered: The quantity_ordered of this OrderItem.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and quantity_ordered is None:
            raise ValueError("Invalid value for `quantity_ordered`, must not be `None`")  # noqa: E501

        self._quantity_ordered = quantity_ordered

    @property
    def quantity_shipped(self):
        """Gets the quantity_shipped of this OrderItem.  # noqa: E501

        The number of items shipped.  # noqa: E501

        :return: The quantity_shipped of this OrderItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity_shipped

    @quantity_shipped.setter
    def quantity_shipped(self, quantity_shipped):
        """Sets the quantity_shipped of this OrderItem.

        The number of items shipped.  # noqa: E501

        :param quantity_shipped: The quantity_shipped of this OrderItem.  # noqa: E501
        :type: int
        """

        self._quantity_shipped = quantity_shipped

    @property
    def product_info(self):
        """Gets the product_info of this OrderItem.  # noqa: E501

        Product information for the item.  # noqa: E501

        :return: The product_info of this OrderItem.  # noqa: E501
        :rtype: ProductInfoDetail
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this OrderItem.

        Product information for the item.  # noqa: E501

        :param product_info: The product_info of this OrderItem.  # noqa: E501
        :type: ProductInfoDetail
        """

        self._product_info = product_info

    @property
    def points_granted(self):
        """Gets the points_granted of this OrderItem.  # noqa: E501

        The number and value of Amazon Points granted with the purchase of an item.  # noqa: E501

        :return: The points_granted of this OrderItem.  # noqa: E501
        :rtype: PointsGrantedDetail
        """
        return self._points_granted

    @points_granted.setter
    def points_granted(self, points_granted):
        """Sets the points_granted of this OrderItem.

        The number and value of Amazon Points granted with the purchase of an item.  # noqa: E501

        :param points_granted: The points_granted of this OrderItem.  # noqa: E501
        :type: PointsGrantedDetail
        """

        self._points_granted = points_granted

    @property
    def item_price(self):
        """Gets the item_price of this OrderItem.  # noqa: E501

        The selling price of the order item. Note that an order item is an item and a quantity. This means that the value of ItemPrice is equal to the selling price of the item multiplied by the quantity ordered. Note that ItemPrice excludes ShippingPrice and GiftWrapPrice.  # noqa: E501

        :return: The item_price of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        """Sets the item_price of this OrderItem.

        The selling price of the order item. Note that an order item is an item and a quantity. This means that the value of ItemPrice is equal to the selling price of the item multiplied by the quantity ordered. Note that ItemPrice excludes ShippingPrice and GiftWrapPrice.  # noqa: E501

        :param item_price: The item_price of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._item_price = item_price

    @property
    def shipping_price(self):
        """Gets the shipping_price of this OrderItem.  # noqa: E501

        The shipping price of the item.  # noqa: E501

        :return: The shipping_price of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._shipping_price

    @shipping_price.setter
    def shipping_price(self, shipping_price):
        """Sets the shipping_price of this OrderItem.

        The shipping price of the item.  # noqa: E501

        :param shipping_price: The shipping_price of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._shipping_price = shipping_price

    @property
    def item_tax(self):
        """Gets the item_tax of this OrderItem.  # noqa: E501

        The tax on the item price.  # noqa: E501

        :return: The item_tax of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._item_tax

    @item_tax.setter
    def item_tax(self, item_tax):
        """Sets the item_tax of this OrderItem.

        The tax on the item price.  # noqa: E501

        :param item_tax: The item_tax of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._item_tax = item_tax

    @property
    def shipping_tax(self):
        """Gets the shipping_tax of this OrderItem.  # noqa: E501

        The tax on the shipping price.  # noqa: E501

        :return: The shipping_tax of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._shipping_tax

    @shipping_tax.setter
    def shipping_tax(self, shipping_tax):
        """Sets the shipping_tax of this OrderItem.

        The tax on the shipping price.  # noqa: E501

        :param shipping_tax: The shipping_tax of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._shipping_tax = shipping_tax

    @property
    def shipping_discount(self):
        """Gets the shipping_discount of this OrderItem.  # noqa: E501

        The discount on the shipping price.  # noqa: E501

        :return: The shipping_discount of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._shipping_discount

    @shipping_discount.setter
    def shipping_discount(self, shipping_discount):
        """Sets the shipping_discount of this OrderItem.

        The discount on the shipping price.  # noqa: E501

        :param shipping_discount: The shipping_discount of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._shipping_discount = shipping_discount

    @property
    def shipping_discount_tax(self):
        """Gets the shipping_discount_tax of this OrderItem.  # noqa: E501

        The tax on the discount on the shipping price.  # noqa: E501

        :return: The shipping_discount_tax of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._shipping_discount_tax

    @shipping_discount_tax.setter
    def shipping_discount_tax(self, shipping_discount_tax):
        """Sets the shipping_discount_tax of this OrderItem.

        The tax on the discount on the shipping price.  # noqa: E501

        :param shipping_discount_tax: The shipping_discount_tax of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._shipping_discount_tax = shipping_discount_tax

    @property
    def promotion_discount(self):
        """Gets the promotion_discount of this OrderItem.  # noqa: E501

        The total of all promotional discounts in the offer.  # noqa: E501

        :return: The promotion_discount of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._promotion_discount

    @promotion_discount.setter
    def promotion_discount(self, promotion_discount):
        """Sets the promotion_discount of this OrderItem.

        The total of all promotional discounts in the offer.  # noqa: E501

        :param promotion_discount: The promotion_discount of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._promotion_discount = promotion_discount

    @property
    def promotion_discount_tax(self):
        """Gets the promotion_discount_tax of this OrderItem.  # noqa: E501

        The tax on the total of all promotional discounts in the offer.  # noqa: E501

        :return: The promotion_discount_tax of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._promotion_discount_tax

    @promotion_discount_tax.setter
    def promotion_discount_tax(self, promotion_discount_tax):
        """Sets the promotion_discount_tax of this OrderItem.

        The tax on the total of all promotional discounts in the offer.  # noqa: E501

        :param promotion_discount_tax: The promotion_discount_tax of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._promotion_discount_tax = promotion_discount_tax

    @property
    def promotion_ids(self):
        """Gets the promotion_ids of this OrderItem.  # noqa: E501


        :return: The promotion_ids of this OrderItem.  # noqa: E501
        :rtype: PromotionIdList
        """
        return self._promotion_ids

    @promotion_ids.setter
    def promotion_ids(self, promotion_ids):
        """Sets the promotion_ids of this OrderItem.


        :param promotion_ids: The promotion_ids of this OrderItem.  # noqa: E501
        :type: PromotionIdList
        """

        self._promotion_ids = promotion_ids

    @property
    def cod_fee(self):
        """Gets the cod_fee of this OrderItem.  # noqa: E501

        The fee charged for COD service.  # noqa: E501

        :return: The cod_fee of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._cod_fee

    @cod_fee.setter
    def cod_fee(self, cod_fee):
        """Sets the cod_fee of this OrderItem.

        The fee charged for COD service.  # noqa: E501

        :param cod_fee: The cod_fee of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._cod_fee = cod_fee

    @property
    def cod_fee_discount(self):
        """Gets the cod_fee_discount of this OrderItem.  # noqa: E501

        The discount on the COD fee.  # noqa: E501

        :return: The cod_fee_discount of this OrderItem.  # noqa: E501
        :rtype: Money
        """
        return self._cod_fee_discount

    @cod_fee_discount.setter
    def cod_fee_discount(self, cod_fee_discount):
        """Sets the cod_fee_discount of this OrderItem.

        The discount on the COD fee.  # noqa: E501

        :param cod_fee_discount: The cod_fee_discount of this OrderItem.  # noqa: E501
        :type: Money
        """

        self._cod_fee_discount = cod_fee_discount

    @property
    def is_gift(self):
        """Gets the is_gift of this OrderItem.  # noqa: E501

        When true, the item is a gift.  # noqa: E501

        :return: The is_gift of this OrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_gift

    @is_gift.setter
    def is_gift(self, is_gift):
        """Sets the is_gift of this OrderItem.

        When true, the item is a gift.  # noqa: E501

        :param is_gift: The is_gift of this OrderItem.  # noqa: E501
        :type: bool
        """

        self._is_gift = is_gift

    @property
    def condition_note(self):
        """Gets the condition_note of this OrderItem.  # noqa: E501

        The condition of the item as described by the seller.  # noqa: E501

        :return: The condition_note of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._condition_note

    @condition_note.setter
    def condition_note(self, condition_note):
        """Sets the condition_note of this OrderItem.

        The condition of the item as described by the seller.  # noqa: E501

        :param condition_note: The condition_note of this OrderItem.  # noqa: E501
        :type: str
        """

        self._condition_note = condition_note

    @property
    def condition_id(self):
        """Gets the condition_id of this OrderItem.  # noqa: E501

        The condition of the item.  Possible values: New, Used, Collectible, Refurbished, Preorder, Club.  # noqa: E501

        :return: The condition_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this OrderItem.

        The condition of the item.  Possible values: New, Used, Collectible, Refurbished, Preorder, Club.  # noqa: E501

        :param condition_id: The condition_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

    @property
    def condition_subtype_id(self):
        """Gets the condition_subtype_id of this OrderItem.  # noqa: E501

        The subcondition of the item.  Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, Any, Other.  # noqa: E501

        :return: The condition_subtype_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._condition_subtype_id

    @condition_subtype_id.setter
    def condition_subtype_id(self, condition_subtype_id):
        """Sets the condition_subtype_id of this OrderItem.

        The subcondition of the item.  Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, Any, Other.  # noqa: E501

        :param condition_subtype_id: The condition_subtype_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._condition_subtype_id = condition_subtype_id

    @property
    def scheduled_delivery_start_date(self):
        """Gets the scheduled_delivery_start_date of this OrderItem.  # noqa: E501

        The start date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format.  # noqa: E501

        :return: The scheduled_delivery_start_date of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_delivery_start_date

    @scheduled_delivery_start_date.setter
    def scheduled_delivery_start_date(self, scheduled_delivery_start_date):
        """Sets the scheduled_delivery_start_date of this OrderItem.

        The start date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format.  # noqa: E501

        :param scheduled_delivery_start_date: The scheduled_delivery_start_date of this OrderItem.  # noqa: E501
        :type: str
        """

        self._scheduled_delivery_start_date = scheduled_delivery_start_date

    @property
    def scheduled_delivery_end_date(self):
        """Gets the scheduled_delivery_end_date of this OrderItem.  # noqa: E501

        The end date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format.  # noqa: E501

        :return: The scheduled_delivery_end_date of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_delivery_end_date

    @scheduled_delivery_end_date.setter
    def scheduled_delivery_end_date(self, scheduled_delivery_end_date):
        """Sets the scheduled_delivery_end_date of this OrderItem.

        The end date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format.  # noqa: E501

        :param scheduled_delivery_end_date: The scheduled_delivery_end_date of this OrderItem.  # noqa: E501
        :type: str
        """

        self._scheduled_delivery_end_date = scheduled_delivery_end_date

    @property
    def price_designation(self):
        """Gets the price_designation of this OrderItem.  # noqa: E501

        Indicates that the selling price is a special price that is available only for Amazon Business orders. For more information about the Amazon Business Seller Program, see the [Amazon Business website](https://www.amazon.com/b2b/info/amazon-business).   Possible values: BusinessPrice - A special price that is available only for Amazon Business orders.  # noqa: E501

        :return: The price_designation of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._price_designation

    @price_designation.setter
    def price_designation(self, price_designation):
        """Sets the price_designation of this OrderItem.

        Indicates that the selling price is a special price that is available only for Amazon Business orders. For more information about the Amazon Business Seller Program, see the [Amazon Business website](https://www.amazon.com/b2b/info/amazon-business).   Possible values: BusinessPrice - A special price that is available only for Amazon Business orders.  # noqa: E501

        :param price_designation: The price_designation of this OrderItem.  # noqa: E501
        :type: str
        """

        self._price_designation = price_designation

    @property
    def tax_collection(self):
        """Gets the tax_collection of this OrderItem.  # noqa: E501

        Information about withheld taxes.  # noqa: E501

        :return: The tax_collection of this OrderItem.  # noqa: E501
        :rtype: TaxCollection
        """
        return self._tax_collection

    @tax_collection.setter
    def tax_collection(self, tax_collection):
        """Sets the tax_collection of this OrderItem.

        Information about withheld taxes.  # noqa: E501

        :param tax_collection: The tax_collection of this OrderItem.  # noqa: E501
        :type: TaxCollection
        """

        self._tax_collection = tax_collection

    @property
    def serial_number_required(self):
        """Gets the serial_number_required of this OrderItem.  # noqa: E501

        When true, the product type for this item has a serial number.  Returned only for Amazon Easy Ship orders.  # noqa: E501

        :return: The serial_number_required of this OrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._serial_number_required

    @serial_number_required.setter
    def serial_number_required(self, serial_number_required):
        """Sets the serial_number_required of this OrderItem.

        When true, the product type for this item has a serial number.  Returned only for Amazon Easy Ship orders.  # noqa: E501

        :param serial_number_required: The serial_number_required of this OrderItem.  # noqa: E501
        :type: bool
        """

        self._serial_number_required = serial_number_required

    @property
    def is_transparency(self):
        """Gets the is_transparency of this OrderItem.  # noqa: E501

        When true, transparency codes are required.  # noqa: E501

        :return: The is_transparency of this OrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_transparency

    @is_transparency.setter
    def is_transparency(self, is_transparency):
        """Sets the is_transparency of this OrderItem.

        When true, transparency codes are required.  # noqa: E501

        :param is_transparency: The is_transparency of this OrderItem.  # noqa: E501
        :type: bool
        """

        self._is_transparency = is_transparency

    @property
    def ioss_number(self):
        """Gets the ioss_number of this OrderItem.  # noqa: E501

        The IOSS number of the seller. Sellers selling in the EU will be assigned a unique IOSS number that must be listed on all packages sent to the EU.  # noqa: E501

        :return: The ioss_number of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._ioss_number

    @ioss_number.setter
    def ioss_number(self, ioss_number):
        """Sets the ioss_number of this OrderItem.

        The IOSS number of the seller. Sellers selling in the EU will be assigned a unique IOSS number that must be listed on all packages sent to the EU.  # noqa: E501

        :param ioss_number: The ioss_number of this OrderItem.  # noqa: E501
        :type: str
        """

        self._ioss_number = ioss_number

    @property
    def store_chain_store_id(self):
        """Gets the store_chain_store_id of this OrderItem.  # noqa: E501

        The store chain store identifier. Linked to a specific store in a store chain.  # noqa: E501

        :return: The store_chain_store_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._store_chain_store_id

    @store_chain_store_id.setter
    def store_chain_store_id(self, store_chain_store_id):
        """Sets the store_chain_store_id of this OrderItem.

        The store chain store identifier. Linked to a specific store in a store chain.  # noqa: E501

        :param store_chain_store_id: The store_chain_store_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._store_chain_store_id = store_chain_store_id

    @property
    def deemed_reseller_category(self):
        """Gets the deemed_reseller_category of this OrderItem.  # noqa: E501

        The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller tax laws in the EU and UK.  # noqa: E501

        :return: The deemed_reseller_category of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._deemed_reseller_category

    @deemed_reseller_category.setter
    def deemed_reseller_category(self, deemed_reseller_category):
        """Sets the deemed_reseller_category of this OrderItem.

        The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller tax laws in the EU and UK.  # noqa: E501

        :param deemed_reseller_category: The deemed_reseller_category of this OrderItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["IOSS", "UOSS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deemed_reseller_category not in allowed_values):
            raise ValueError(
                "Invalid value for `deemed_reseller_category` ({0}), must be one of {1}"  # noqa: E501
                .format(deemed_reseller_category, allowed_values)
            )

        self._deemed_reseller_category = deemed_reseller_category

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
        if issubclass(OrderItem, dict):
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
        if not isinstance(other, OrderItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderItem):
            return True

        return self.to_dict() != other.to_dict()

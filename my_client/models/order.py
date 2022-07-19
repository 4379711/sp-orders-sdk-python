# coding: utf-8

import pprint
import re  # noqa: F401

import six

from my_client.configuration import Configuration


class Order(object):
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
        'seller_order_id': 'str',
        'purchase_date': 'str',
        'last_update_date': 'str',
        'order_status': 'str',
        'fulfillment_channel': 'str',
        'sales_channel': 'str',
        'order_channel': 'str',
        'ship_service_level': 'str',
        'order_total': 'Money',
        'number_of_items_shipped': 'int',
        'number_of_items_unshipped': 'int',
        'payment_execution_detail': 'PaymentExecutionDetailItemList',
        'payment_method': 'str',
        'payment_method_details': 'PaymentMethodDetailItemList',
        'marketplace_id': 'str',
        'shipment_service_level_category': 'str',
        'easy_ship_shipment_status': 'str',
        'cba_displayable_shipping_label': 'str',
        'order_type': 'str',
        'earliest_ship_date': 'str',
        'latest_ship_date': 'str',
        'earliest_delivery_date': 'str',
        'latest_delivery_date': 'str',
        'is_business_order': 'bool',
        'is_prime': 'bool',
        'is_premium_order': 'bool',
        'is_global_express_enabled': 'bool',
        'replaced_order_id': 'str',
        'is_replacement_order': 'bool',
        'promise_response_due_date': 'str',
        'is_estimated_ship_date_set': 'bool',
        'is_sold_by_ab': 'bool',
        'default_ship_from_location_address': 'Address',
        'fulfillment_instruction': 'FulfillmentInstruction',
        'is_ispu': 'bool'
    }

    attribute_map = {
        'amazon_order_id': 'AmazonOrderId',
        'seller_order_id': 'SellerOrderId',
        'purchase_date': 'PurchaseDate',
        'last_update_date': 'LastUpdateDate',
        'order_status': 'OrderStatus',
        'fulfillment_channel': 'FulfillmentChannel',
        'sales_channel': 'SalesChannel',
        'order_channel': 'OrderChannel',
        'ship_service_level': 'ShipServiceLevel',
        'order_total': 'OrderTotal',
        'number_of_items_shipped': 'NumberOfItemsShipped',
        'number_of_items_unshipped': 'NumberOfItemsUnshipped',
        'payment_execution_detail': 'PaymentExecutionDetail',
        'payment_method': 'PaymentMethod',
        'payment_method_details': 'PaymentMethodDetails',
        'marketplace_id': 'MarketplaceId',
        'shipment_service_level_category': 'ShipmentServiceLevelCategory',
        'easy_ship_shipment_status': 'EasyShipShipmentStatus',
        'cba_displayable_shipping_label': 'CbaDisplayableShippingLabel',
        'order_type': 'OrderType',
        'earliest_ship_date': 'EarliestShipDate',
        'latest_ship_date': 'LatestShipDate',
        'earliest_delivery_date': 'EarliestDeliveryDate',
        'latest_delivery_date': 'LatestDeliveryDate',
        'is_business_order': 'IsBusinessOrder',
        'is_prime': 'IsPrime',
        'is_premium_order': 'IsPremiumOrder',
        'is_global_express_enabled': 'IsGlobalExpressEnabled',
        'replaced_order_id': 'ReplacedOrderId',
        'is_replacement_order': 'IsReplacementOrder',
        'promise_response_due_date': 'PromiseResponseDueDate',
        'is_estimated_ship_date_set': 'IsEstimatedShipDateSet',
        'is_sold_by_ab': 'IsSoldByAB',
        'default_ship_from_location_address': 'DefaultShipFromLocationAddress',
        'fulfillment_instruction': 'FulfillmentInstruction',
        'is_ispu': 'IsISPU'
    }

    def __init__(self, amazon_order_id=None, seller_order_id=None, purchase_date=None, last_update_date=None, order_status=None, fulfillment_channel=None, sales_channel=None, order_channel=None, ship_service_level=None, order_total=None, number_of_items_shipped=None, number_of_items_unshipped=None, payment_execution_detail=None, payment_method=None, payment_method_details=None, marketplace_id=None, shipment_service_level_category=None, easy_ship_shipment_status=None, cba_displayable_shipping_label=None, order_type=None, earliest_ship_date=None, latest_ship_date=None, earliest_delivery_date=None, latest_delivery_date=None, is_business_order=None, is_prime=None, is_premium_order=None, is_global_express_enabled=None, replaced_order_id=None, is_replacement_order=None, promise_response_due_date=None, is_estimated_ship_date_set=None, is_sold_by_ab=None, default_ship_from_location_address=None, fulfillment_instruction=None, is_ispu=None, _configuration=None):  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amazon_order_id = None
        self._seller_order_id = None
        self._purchase_date = None
        self._last_update_date = None
        self._order_status = None
        self._fulfillment_channel = None
        self._sales_channel = None
        self._order_channel = None
        self._ship_service_level = None
        self._order_total = None
        self._number_of_items_shipped = None
        self._number_of_items_unshipped = None
        self._payment_execution_detail = None
        self._payment_method = None
        self._payment_method_details = None
        self._marketplace_id = None
        self._shipment_service_level_category = None
        self._easy_ship_shipment_status = None
        self._cba_displayable_shipping_label = None
        self._order_type = None
        self._earliest_ship_date = None
        self._latest_ship_date = None
        self._earliest_delivery_date = None
        self._latest_delivery_date = None
        self._is_business_order = None
        self._is_prime = None
        self._is_premium_order = None
        self._is_global_express_enabled = None
        self._replaced_order_id = None
        self._is_replacement_order = None
        self._promise_response_due_date = None
        self._is_estimated_ship_date_set = None
        self._is_sold_by_ab = None
        self._default_ship_from_location_address = None
        self._fulfillment_instruction = None
        self._is_ispu = None
        self.discriminator = None

        self.amazon_order_id = amazon_order_id
        if seller_order_id is not None:
            self.seller_order_id = seller_order_id
        self.purchase_date = purchase_date
        self.last_update_date = last_update_date
        self.order_status = order_status
        if fulfillment_channel is not None:
            self.fulfillment_channel = fulfillment_channel
        if sales_channel is not None:
            self.sales_channel = sales_channel
        if order_channel is not None:
            self.order_channel = order_channel
        if ship_service_level is not None:
            self.ship_service_level = ship_service_level
        if order_total is not None:
            self.order_total = order_total
        if number_of_items_shipped is not None:
            self.number_of_items_shipped = number_of_items_shipped
        if number_of_items_unshipped is not None:
            self.number_of_items_unshipped = number_of_items_unshipped
        if payment_execution_detail is not None:
            self.payment_execution_detail = payment_execution_detail
        if payment_method is not None:
            self.payment_method = payment_method
        if payment_method_details is not None:
            self.payment_method_details = payment_method_details
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if shipment_service_level_category is not None:
            self.shipment_service_level_category = shipment_service_level_category
        if easy_ship_shipment_status is not None:
            self.easy_ship_shipment_status = easy_ship_shipment_status
        if cba_displayable_shipping_label is not None:
            self.cba_displayable_shipping_label = cba_displayable_shipping_label
        if order_type is not None:
            self.order_type = order_type
        if earliest_ship_date is not None:
            self.earliest_ship_date = earliest_ship_date
        if latest_ship_date is not None:
            self.latest_ship_date = latest_ship_date
        if earliest_delivery_date is not None:
            self.earliest_delivery_date = earliest_delivery_date
        if latest_delivery_date is not None:
            self.latest_delivery_date = latest_delivery_date
        if is_business_order is not None:
            self.is_business_order = is_business_order
        if is_prime is not None:
            self.is_prime = is_prime
        if is_premium_order is not None:
            self.is_premium_order = is_premium_order
        if is_global_express_enabled is not None:
            self.is_global_express_enabled = is_global_express_enabled
        if replaced_order_id is not None:
            self.replaced_order_id = replaced_order_id
        if is_replacement_order is not None:
            self.is_replacement_order = is_replacement_order
        if promise_response_due_date is not None:
            self.promise_response_due_date = promise_response_due_date
        if is_estimated_ship_date_set is not None:
            self.is_estimated_ship_date_set = is_estimated_ship_date_set
        if is_sold_by_ab is not None:
            self.is_sold_by_ab = is_sold_by_ab
        if default_ship_from_location_address is not None:
            self.default_ship_from_location_address = default_ship_from_location_address
        if fulfillment_instruction is not None:
            self.fulfillment_instruction = fulfillment_instruction
        if is_ispu is not None:
            self.is_ispu = is_ispu

    @property
    def amazon_order_id(self):
        """Gets the amazon_order_id of this Order.  # noqa: E501

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :return: The amazon_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._amazon_order_id

    @amazon_order_id.setter
    def amazon_order_id(self, amazon_order_id):
        """Sets the amazon_order_id of this Order.

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :param amazon_order_id: The amazon_order_id of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and amazon_order_id is None:
            raise ValueError("Invalid value for `amazon_order_id`, must not be `None`")  # noqa: E501

        self._amazon_order_id = amazon_order_id

    @property
    def seller_order_id(self):
        """Gets the seller_order_id of this Order.  # noqa: E501

        A seller-defined order identifier.  # noqa: E501

        :return: The seller_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._seller_order_id

    @seller_order_id.setter
    def seller_order_id(self, seller_order_id):
        """Sets the seller_order_id of this Order.

        A seller-defined order identifier.  # noqa: E501

        :param seller_order_id: The seller_order_id of this Order.  # noqa: E501
        :type: str
        """

        self._seller_order_id = seller_order_id

    @property
    def purchase_date(self):
        """Gets the purchase_date of this Order.  # noqa: E501

        The date when the order was created.  # noqa: E501

        :return: The purchase_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """Sets the purchase_date of this Order.

        The date when the order was created.  # noqa: E501

        :param purchase_date: The purchase_date of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and purchase_date is None:
            raise ValueError("Invalid value for `purchase_date`, must not be `None`")  # noqa: E501

        self._purchase_date = purchase_date

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Order.  # noqa: E501

        The date when the order was last updated.  Note: LastUpdateDate is returned with an incorrect date for orders that were last updated before 2009-04-01.  # noqa: E501

        :return: The last_update_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Order.

        The date when the order was last updated.  Note: LastUpdateDate is returned with an incorrect date for orders that were last updated before 2009-04-01.  # noqa: E501

        :param last_update_date: The last_update_date of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def order_status(self):
        """Gets the order_status of this Order.  # noqa: E501

        The current order status.  # noqa: E501

        :return: The order_status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this Order.

        The current order status.  # noqa: E501

        :param order_status: The order_status of this Order.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and order_status is None:
            raise ValueError("Invalid value for `order_status`, must not be `None`")  # noqa: E501
        allowed_values = ["Pending", "Unshipped", "PartiallyShipped", "Shipped", "Canceled", "Unfulfillable", "InvoiceUnconfirmed", "PendingAvailability"]  # noqa: E501
        if (self._configuration.client_side_validation and
                order_status not in allowed_values):
            raise ValueError(
                "Invalid value for `order_status` ({0}), must be one of {1}"  # noqa: E501
                .format(order_status, allowed_values)
            )

        self._order_status = order_status

    @property
    def fulfillment_channel(self):
        """Gets the fulfillment_channel of this Order.  # noqa: E501

        Whether the order was fulfilled by Amazon (AFN) or by the seller (MFN).  # noqa: E501

        :return: The fulfillment_channel of this Order.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_channel

    @fulfillment_channel.setter
    def fulfillment_channel(self, fulfillment_channel):
        """Sets the fulfillment_channel of this Order.

        Whether the order was fulfilled by Amazon (AFN) or by the seller (MFN).  # noqa: E501

        :param fulfillment_channel: The fulfillment_channel of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["MFN", "AFN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                fulfillment_channel not in allowed_values):
            raise ValueError(
                "Invalid value for `fulfillment_channel` ({0}), must be one of {1}"  # noqa: E501
                .format(fulfillment_channel, allowed_values)
            )

        self._fulfillment_channel = fulfillment_channel

    @property
    def sales_channel(self):
        """Gets the sales_channel of this Order.  # noqa: E501

        The sales channel of the first item in the order.  # noqa: E501

        :return: The sales_channel of this Order.  # noqa: E501
        :rtype: str
        """
        return self._sales_channel

    @sales_channel.setter
    def sales_channel(self, sales_channel):
        """Sets the sales_channel of this Order.

        The sales channel of the first item in the order.  # noqa: E501

        :param sales_channel: The sales_channel of this Order.  # noqa: E501
        :type: str
        """

        self._sales_channel = sales_channel

    @property
    def order_channel(self):
        """Gets the order_channel of this Order.  # noqa: E501

        The order channel of the first item in the order.  # noqa: E501

        :return: The order_channel of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_channel

    @order_channel.setter
    def order_channel(self, order_channel):
        """Sets the order_channel of this Order.

        The order channel of the first item in the order.  # noqa: E501

        :param order_channel: The order_channel of this Order.  # noqa: E501
        :type: str
        """

        self._order_channel = order_channel

    @property
    def ship_service_level(self):
        """Gets the ship_service_level of this Order.  # noqa: E501

        The shipment service level of the order.  # noqa: E501

        :return: The ship_service_level of this Order.  # noqa: E501
        :rtype: str
        """
        return self._ship_service_level

    @ship_service_level.setter
    def ship_service_level(self, ship_service_level):
        """Sets the ship_service_level of this Order.

        The shipment service level of the order.  # noqa: E501

        :param ship_service_level: The ship_service_level of this Order.  # noqa: E501
        :type: str
        """

        self._ship_service_level = ship_service_level

    @property
    def order_total(self):
        """Gets the order_total of this Order.  # noqa: E501

        The total charge for this order.  # noqa: E501

        :return: The order_total of this Order.  # noqa: E501
        :rtype: Money
        """
        return self._order_total

    @order_total.setter
    def order_total(self, order_total):
        """Sets the order_total of this Order.

        The total charge for this order.  # noqa: E501

        :param order_total: The order_total of this Order.  # noqa: E501
        :type: Money
        """

        self._order_total = order_total

    @property
    def number_of_items_shipped(self):
        """Gets the number_of_items_shipped of this Order.  # noqa: E501

        The number of items shipped.  # noqa: E501

        :return: The number_of_items_shipped of this Order.  # noqa: E501
        :rtype: int
        """
        return self._number_of_items_shipped

    @number_of_items_shipped.setter
    def number_of_items_shipped(self, number_of_items_shipped):
        """Sets the number_of_items_shipped of this Order.

        The number of items shipped.  # noqa: E501

        :param number_of_items_shipped: The number_of_items_shipped of this Order.  # noqa: E501
        :type: int
        """

        self._number_of_items_shipped = number_of_items_shipped

    @property
    def number_of_items_unshipped(self):
        """Gets the number_of_items_unshipped of this Order.  # noqa: E501

        The number of items unshipped.  # noqa: E501

        :return: The number_of_items_unshipped of this Order.  # noqa: E501
        :rtype: int
        """
        return self._number_of_items_unshipped

    @number_of_items_unshipped.setter
    def number_of_items_unshipped(self, number_of_items_unshipped):
        """Sets the number_of_items_unshipped of this Order.

        The number of items unshipped.  # noqa: E501

        :param number_of_items_unshipped: The number_of_items_unshipped of this Order.  # noqa: E501
        :type: int
        """

        self._number_of_items_unshipped = number_of_items_unshipped

    @property
    def payment_execution_detail(self):
        """Gets the payment_execution_detail of this Order.  # noqa: E501

        Information about sub-payment methods for a Cash On Delivery (COD) order.  Note: For a COD order that is paid for using one sub-payment method, one PaymentExecutionDetailItem object is returned, with PaymentExecutionDetailItem/PaymentMethod = COD. For a COD order that is paid for using multiple sub-payment methods, two or more PaymentExecutionDetailItem objects are returned.  # noqa: E501

        :return: The payment_execution_detail of this Order.  # noqa: E501
        :rtype: PaymentExecutionDetailItemList
        """
        return self._payment_execution_detail

    @payment_execution_detail.setter
    def payment_execution_detail(self, payment_execution_detail):
        """Sets the payment_execution_detail of this Order.

        Information about sub-payment methods for a Cash On Delivery (COD) order.  Note: For a COD order that is paid for using one sub-payment method, one PaymentExecutionDetailItem object is returned, with PaymentExecutionDetailItem/PaymentMethod = COD. For a COD order that is paid for using multiple sub-payment methods, two or more PaymentExecutionDetailItem objects are returned.  # noqa: E501

        :param payment_execution_detail: The payment_execution_detail of this Order.  # noqa: E501
        :type: PaymentExecutionDetailItemList
        """

        self._payment_execution_detail = payment_execution_detail

    @property
    def payment_method(self):
        """Gets the payment_method of this Order.  # noqa: E501

        The payment method for the order. This property is limited to Cash On Delivery (COD) and Convenience Store (CVS) payment methods. Unless you need the specific COD payment information provided by the PaymentExecutionDetailItem object, we recommend using the PaymentMethodDetails property to get payment method information.  # noqa: E501

        :return: The payment_method of this Order.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Order.

        The payment method for the order. This property is limited to Cash On Delivery (COD) and Convenience Store (CVS) payment methods. Unless you need the specific COD payment information provided by the PaymentExecutionDetailItem object, we recommend using the PaymentMethodDetails property to get payment method information.  # noqa: E501

        :param payment_method: The payment_method of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["COD", "CVS", "Other"]  # noqa: E501
        if (self._configuration.client_side_validation and
                payment_method not in allowed_values):
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def payment_method_details(self):
        """Gets the payment_method_details of this Order.  # noqa: E501

        A list of payment methods for the order.  # noqa: E501

        :return: The payment_method_details of this Order.  # noqa: E501
        :rtype: PaymentMethodDetailItemList
        """
        return self._payment_method_details

    @payment_method_details.setter
    def payment_method_details(self, payment_method_details):
        """Sets the payment_method_details of this Order.

        A list of payment methods for the order.  # noqa: E501

        :param payment_method_details: The payment_method_details of this Order.  # noqa: E501
        :type: PaymentMethodDetailItemList
        """

        self._payment_method_details = payment_method_details

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this Order.  # noqa: E501

        The identifier for the marketplace where the order was placed.  # noqa: E501

        :return: The marketplace_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this Order.

        The identifier for the marketplace where the order was placed.  # noqa: E501

        :param marketplace_id: The marketplace_id of this Order.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def shipment_service_level_category(self):
        """Gets the shipment_service_level_category of this Order.  # noqa: E501

        The shipment service level category of the order.  Possible values: Expedited, FreeEconomy, NextDay, SameDay, SecondDay, Scheduled, Standard.  # noqa: E501

        :return: The shipment_service_level_category of this Order.  # noqa: E501
        :rtype: str
        """
        return self._shipment_service_level_category

    @shipment_service_level_category.setter
    def shipment_service_level_category(self, shipment_service_level_category):
        """Sets the shipment_service_level_category of this Order.

        The shipment service level category of the order.  Possible values: Expedited, FreeEconomy, NextDay, SameDay, SecondDay, Scheduled, Standard.  # noqa: E501

        :param shipment_service_level_category: The shipment_service_level_category of this Order.  # noqa: E501
        :type: str
        """

        self._shipment_service_level_category = shipment_service_level_category

    @property
    def easy_ship_shipment_status(self):
        """Gets the easy_ship_shipment_status of this Order.  # noqa: E501

        The status of the Amazon Easy Ship order. This property is included only for Amazon Easy Ship orders.  Possible values: PendingPickUp, LabelCanceled, PickedUp, OutForDelivery, Damaged, Delivered, RejectedByBuyer, Undeliverable, ReturnedToSeller, ReturningToSeller.  # noqa: E501

        :return: The easy_ship_shipment_status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._easy_ship_shipment_status

    @easy_ship_shipment_status.setter
    def easy_ship_shipment_status(self, easy_ship_shipment_status):
        """Sets the easy_ship_shipment_status of this Order.

        The status of the Amazon Easy Ship order. This property is included only for Amazon Easy Ship orders.  Possible values: PendingPickUp, LabelCanceled, PickedUp, OutForDelivery, Damaged, Delivered, RejectedByBuyer, Undeliverable, ReturnedToSeller, ReturningToSeller.  # noqa: E501

        :param easy_ship_shipment_status: The easy_ship_shipment_status of this Order.  # noqa: E501
        :type: str
        """

        self._easy_ship_shipment_status = easy_ship_shipment_status

    @property
    def cba_displayable_shipping_label(self):
        """Gets the cba_displayable_shipping_label of this Order.  # noqa: E501

        Custom ship label for Checkout by Amazon (CBA).  # noqa: E501

        :return: The cba_displayable_shipping_label of this Order.  # noqa: E501
        :rtype: str
        """
        return self._cba_displayable_shipping_label

    @cba_displayable_shipping_label.setter
    def cba_displayable_shipping_label(self, cba_displayable_shipping_label):
        """Sets the cba_displayable_shipping_label of this Order.

        Custom ship label for Checkout by Amazon (CBA).  # noqa: E501

        :param cba_displayable_shipping_label: The cba_displayable_shipping_label of this Order.  # noqa: E501
        :type: str
        """

        self._cba_displayable_shipping_label = cba_displayable_shipping_label

    @property
    def order_type(self):
        """Gets the order_type of this Order.  # noqa: E501

        The type of the order.  # noqa: E501

        :return: The order_type of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this Order.

        The type of the order.  # noqa: E501

        :param order_type: The order_type of this Order.  # noqa: E501
        :type: str
        """
        allowed_values = ["StandardOrder", "LongLeadTimeOrder", "Preorder", "BackOrder", "SourcingOnDemandOrder"]  # noqa: E501
        if (self._configuration.client_side_validation and
                order_type not in allowed_values):
            raise ValueError(
                "Invalid value for `order_type` ({0}), must be one of {1}"  # noqa: E501
                .format(order_type, allowed_values)
            )

        self._order_type = order_type

    @property
    def earliest_ship_date(self):
        """Gets the earliest_ship_date of this Order.  # noqa: E501

        The start of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: EarliestShipDate might not be returned for orders placed before February 1, 2013.  # noqa: E501

        :return: The earliest_ship_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._earliest_ship_date

    @earliest_ship_date.setter
    def earliest_ship_date(self, earliest_ship_date):
        """Sets the earliest_ship_date of this Order.

        The start of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: EarliestShipDate might not be returned for orders placed before February 1, 2013.  # noqa: E501

        :param earliest_ship_date: The earliest_ship_date of this Order.  # noqa: E501
        :type: str
        """

        self._earliest_ship_date = earliest_ship_date

    @property
    def latest_ship_date(self):
        """Gets the latest_ship_date of this Order.  # noqa: E501

        The end of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: LatestShipDate might not be returned for orders placed before February 1, 2013.  # noqa: E501

        :return: The latest_ship_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._latest_ship_date

    @latest_ship_date.setter
    def latest_ship_date(self, latest_ship_date):
        """Sets the latest_ship_date of this Order.

        The end of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: LatestShipDate might not be returned for orders placed before February 1, 2013.  # noqa: E501

        :param latest_ship_date: The latest_ship_date of this Order.  # noqa: E501
        :type: str
        """

        self._latest_ship_date = latest_ship_date

    @property
    def earliest_delivery_date(self):
        """Gets the earliest_delivery_date of this Order.  # noqa: E501

        The start of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  # noqa: E501

        :return: The earliest_delivery_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._earliest_delivery_date

    @earliest_delivery_date.setter
    def earliest_delivery_date(self, earliest_delivery_date):
        """Sets the earliest_delivery_date of this Order.

        The start of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  # noqa: E501

        :param earliest_delivery_date: The earliest_delivery_date of this Order.  # noqa: E501
        :type: str
        """

        self._earliest_delivery_date = earliest_delivery_date

    @property
    def latest_delivery_date(self):
        """Gets the latest_delivery_date of this Order.  # noqa: E501

        The end of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders that do not have a PendingAvailability, Pending, or Canceled status.  # noqa: E501

        :return: The latest_delivery_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._latest_delivery_date

    @latest_delivery_date.setter
    def latest_delivery_date(self, latest_delivery_date):
        """Sets the latest_delivery_date of this Order.

        The end of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders that do not have a PendingAvailability, Pending, or Canceled status.  # noqa: E501

        :param latest_delivery_date: The latest_delivery_date of this Order.  # noqa: E501
        :type: str
        """

        self._latest_delivery_date = latest_delivery_date

    @property
    def is_business_order(self):
        """Gets the is_business_order of this Order.  # noqa: E501

        When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified Business Buyer.  # noqa: E501

        :return: The is_business_order of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_business_order

    @is_business_order.setter
    def is_business_order(self, is_business_order):
        """Sets the is_business_order of this Order.

        When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified Business Buyer.  # noqa: E501

        :param is_business_order: The is_business_order of this Order.  # noqa: E501
        :type: bool
        """

        self._is_business_order = is_business_order

    @property
    def is_prime(self):
        """Gets the is_prime of this Order.  # noqa: E501

        When true, the order is a seller-fulfilled Amazon Prime order.  # noqa: E501

        :return: The is_prime of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_prime

    @is_prime.setter
    def is_prime(self, is_prime):
        """Sets the is_prime of this Order.

        When true, the order is a seller-fulfilled Amazon Prime order.  # noqa: E501

        :param is_prime: The is_prime of this Order.  # noqa: E501
        :type: bool
        """

        self._is_prime = is_prime

    @property
    def is_premium_order(self):
        """Gets the is_premium_order of this Order.  # noqa: E501

        When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping orders, see \"Premium Shipping Options\" in the Seller Central Help for your marketplace.  # noqa: E501

        :return: The is_premium_order of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_premium_order

    @is_premium_order.setter
    def is_premium_order(self, is_premium_order):
        """Sets the is_premium_order of this Order.

        When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping orders, see \"Premium Shipping Options\" in the Seller Central Help for your marketplace.  # noqa: E501

        :param is_premium_order: The is_premium_order of this Order.  # noqa: E501
        :type: bool
        """

        self._is_premium_order = is_premium_order

    @property
    def is_global_express_enabled(self):
        """Gets the is_global_express_enabled of this Order.  # noqa: E501

        When true, the order is a GlobalExpress order.  # noqa: E501

        :return: The is_global_express_enabled of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_global_express_enabled

    @is_global_express_enabled.setter
    def is_global_express_enabled(self, is_global_express_enabled):
        """Sets the is_global_express_enabled of this Order.

        When true, the order is a GlobalExpress order.  # noqa: E501

        :param is_global_express_enabled: The is_global_express_enabled of this Order.  # noqa: E501
        :type: bool
        """

        self._is_global_express_enabled = is_global_express_enabled

    @property
    def replaced_order_id(self):
        """Gets the replaced_order_id of this Order.  # noqa: E501

        The order ID value for the order that is being replaced. Returned only if IsReplacementOrder = true.  # noqa: E501

        :return: The replaced_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._replaced_order_id

    @replaced_order_id.setter
    def replaced_order_id(self, replaced_order_id):
        """Sets the replaced_order_id of this Order.

        The order ID value for the order that is being replaced. Returned only if IsReplacementOrder = true.  # noqa: E501

        :param replaced_order_id: The replaced_order_id of this Order.  # noqa: E501
        :type: str
        """

        self._replaced_order_id = replaced_order_id

    @property
    def is_replacement_order(self):
        """Gets the is_replacement_order of this Order.  # noqa: E501

        When true, this is a replacement order.  # noqa: E501

        :return: The is_replacement_order of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_replacement_order

    @is_replacement_order.setter
    def is_replacement_order(self, is_replacement_order):
        """Sets the is_replacement_order of this Order.

        When true, this is a replacement order.  # noqa: E501

        :param is_replacement_order: The is_replacement_order of this Order.  # noqa: E501
        :type: bool
        """

        self._is_replacement_order = is_replacement_order

    @property
    def promise_response_due_date(self):
        """Gets the promise_response_due_date of this Order.  # noqa: E501

        Indicates the date by which the seller must respond to the buyer with an estimated ship date. Returned only for Sourcing on Demand orders.  # noqa: E501

        :return: The promise_response_due_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._promise_response_due_date

    @promise_response_due_date.setter
    def promise_response_due_date(self, promise_response_due_date):
        """Sets the promise_response_due_date of this Order.

        Indicates the date by which the seller must respond to the buyer with an estimated ship date. Returned only for Sourcing on Demand orders.  # noqa: E501

        :param promise_response_due_date: The promise_response_due_date of this Order.  # noqa: E501
        :type: str
        """

        self._promise_response_due_date = promise_response_due_date

    @property
    def is_estimated_ship_date_set(self):
        """Gets the is_estimated_ship_date_set of this Order.  # noqa: E501

        When true, the estimated ship date is set for the order. Returned only for Sourcing on Demand orders.  # noqa: E501

        :return: The is_estimated_ship_date_set of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_estimated_ship_date_set

    @is_estimated_ship_date_set.setter
    def is_estimated_ship_date_set(self, is_estimated_ship_date_set):
        """Sets the is_estimated_ship_date_set of this Order.

        When true, the estimated ship date is set for the order. Returned only for Sourcing on Demand orders.  # noqa: E501

        :param is_estimated_ship_date_set: The is_estimated_ship_date_set of this Order.  # noqa: E501
        :type: bool
        """

        self._is_estimated_ship_date_set = is_estimated_ship_date_set

    @property
    def is_sold_by_ab(self):
        """Gets the is_sold_by_ab of this Order.  # noqa: E501

        When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.  # noqa: E501

        :return: The is_sold_by_ab of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_sold_by_ab

    @is_sold_by_ab.setter
    def is_sold_by_ab(self, is_sold_by_ab):
        """Sets the is_sold_by_ab of this Order.

        When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.  # noqa: E501

        :param is_sold_by_ab: The is_sold_by_ab of this Order.  # noqa: E501
        :type: bool
        """

        self._is_sold_by_ab = is_sold_by_ab

    @property
    def default_ship_from_location_address(self):
        """Gets the default_ship_from_location_address of this Order.  # noqa: E501

        The recommended location for the seller to ship the items from. It is calculated at checkout. The seller may or may not choose to ship from this location.  # noqa: E501

        :return: The default_ship_from_location_address of this Order.  # noqa: E501
        :rtype: Address
        """
        return self._default_ship_from_location_address

    @default_ship_from_location_address.setter
    def default_ship_from_location_address(self, default_ship_from_location_address):
        """Sets the default_ship_from_location_address of this Order.

        The recommended location for the seller to ship the items from. It is calculated at checkout. The seller may or may not choose to ship from this location.  # noqa: E501

        :param default_ship_from_location_address: The default_ship_from_location_address of this Order.  # noqa: E501
        :type: Address
        """

        self._default_ship_from_location_address = default_ship_from_location_address

    @property
    def fulfillment_instruction(self):
        """Gets the fulfillment_instruction of this Order.  # noqa: E501

        Contains the instructions about the fulfillment like where should it be fulfilled from.  # noqa: E501

        :return: The fulfillment_instruction of this Order.  # noqa: E501
        :rtype: FulfillmentInstruction
        """
        return self._fulfillment_instruction

    @fulfillment_instruction.setter
    def fulfillment_instruction(self, fulfillment_instruction):
        """Sets the fulfillment_instruction of this Order.

        Contains the instructions about the fulfillment like where should it be fulfilled from.  # noqa: E501

        :param fulfillment_instruction: The fulfillment_instruction of this Order.  # noqa: E501
        :type: FulfillmentInstruction
        """

        self._fulfillment_instruction = fulfillment_instruction

    @property
    def is_ispu(self):
        """Gets the is_ispu of this Order.  # noqa: E501

        When true, this order is marked to be picked up from a store rather than delivered.  # noqa: E501

        :return: The is_ispu of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._is_ispu

    @is_ispu.setter
    def is_ispu(self, is_ispu):
        """Sets the is_ispu of this Order.

        When true, this order is marked to be picked up from a store rather than delivered.  # noqa: E501

        :param is_ispu: The is_ispu of this Order.  # noqa: E501
        :type: bool
        """

        self._is_ispu = is_ispu

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Order):
            return True

        return self.to_dict() != other.to_dict()

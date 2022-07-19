# my-client
The Selling Partner API for Orders helps you programmatically retrieve order information. These APIs let you develop fast, flexible, custom applications in areas like order synchronization, order research, and demand-based decision support tools.

- API version: v0
- Package version: 1.0.0
- Build date: 2021-06-18T18:35:52.676+08:00
- Build auth: yaLong

## Requirements.

- Python 3.6+
- Openssl 1.0.2+
```sh
python -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

## Installation & Usage
### pip install

```sh
pip install -r requirements.txt
```

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python

from my_client import OrdersV0Api, ApiClient, Configuration, MarketplaceRegion

refresh_token = "Atzr|xxx"
role_arn = "arn:aws:iam::00xxxxx:role/xxx"
aws_access_key = "xxx"
aws_secret_key = "xxx"
client_id = "amzn1.application1xxx"
client_secret = "xxx"
marketplace_ids = [MarketplaceRegion.US.marketplace]
_config = Configuration(role_arn=role_arn,
                        refresh_token=refresh_token,
                        aws_access_key=aws_access_key,
                        aws_secret_key=aws_secret_key,
                        client_id=client_id,
                        client_secret=client_secret,
                        region="US")
api_client = ApiClient(configuration=_config)
api_instance = OrdersV0Api(api_client)

api_response = api_instance.get_order(order_id)
print(api_response)

```

## Documentation for API Endpoints

All URIs are relative to *https://sellingpartnerapi-na.amazon.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrdersV0Api* | [**get_order**](docs/OrdersV0Api.md#get_order) | **GET** /orders/v0/orders/{orderId} | 
*OrdersV0Api* | [**get_order_address**](docs/OrdersV0Api.md#get_order_address) | **GET** /orders/v0/orders/{orderId}/address | 
*OrdersV0Api* | [**get_order_buyer_info**](docs/OrdersV0Api.md#get_order_buyer_info) | **GET** /orders/v0/orders/{orderId}/buyerInfo | 
*OrdersV0Api* | [**get_order_items**](docs/OrdersV0Api.md#get_order_items) | **GET** /orders/v0/orders/{orderId}/orderItems | 
*OrdersV0Api* | [**get_order_items_buyer_info**](docs/OrdersV0Api.md#get_order_items_buyer_info) | **GET** /orders/v0/orders/{orderId}/orderItems/buyerInfo | 
*OrdersV0Api* | [**get_orders**](docs/OrdersV0Api.md#get_orders) | **GET** /orders/v0/orders | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [BuyerCustomizedInfoDetail](docs/BuyerCustomizedInfoDetail.md)
 - [BuyerTaxInfo](docs/BuyerTaxInfo.md)
 - [Error](docs/Error.md)
 - [ErrorList](docs/ErrorList.md)
 - [FulfillmentInstruction](docs/FulfillmentInstruction.md)
 - [GetOrderAddressResponse](docs/GetOrderAddressResponse.md)
 - [GetOrderBuyerInfoResponse](docs/GetOrderBuyerInfoResponse.md)
 - [GetOrderItemsBuyerInfoResponse](docs/GetOrderItemsBuyerInfoResponse.md)
 - [GetOrderItemsResponse](docs/GetOrderItemsResponse.md)
 - [GetOrderResponse](docs/GetOrderResponse.md)
 - [GetOrdersResponse](docs/GetOrdersResponse.md)
 - [Money](docs/Money.md)
 - [Order](docs/Order.md)
 - [OrderAddress](docs/OrderAddress.md)
 - [OrderBuyerInfo](docs/OrderBuyerInfo.md)
 - [OrderItem](docs/OrderItem.md)
 - [OrderItemBuyerInfo](docs/OrderItemBuyerInfo.md)
 - [OrderItemBuyerInfoList](docs/OrderItemBuyerInfoList.md)
 - [OrderItemList](docs/OrderItemList.md)
 - [OrderItemsBuyerInfoList](docs/OrderItemsBuyerInfoList.md)
 - [OrderItemsList](docs/OrderItemsList.md)
 - [OrderList](docs/OrderList.md)
 - [OrdersList](docs/OrdersList.md)
 - [PaymentExecutionDetailItem](docs/PaymentExecutionDetailItem.md)
 - [PaymentExecutionDetailItemList](docs/PaymentExecutionDetailItemList.md)
 - [PaymentMethodDetailItemList](docs/PaymentMethodDetailItemList.md)
 - [PointsGrantedDetail](docs/PointsGrantedDetail.md)
 - [ProductInfoDetail](docs/ProductInfoDetail.md)
 - [PromotionIdList](docs/PromotionIdList.md)
 - [TaxClassification](docs/TaxClassification.md)
 - [TaxCollection](docs/TaxCollection.md)


# OrderResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The order identifier | 
**block_number** | **float** | The block number when the order was created | 
**timestamp** | **datetime** | The timestamp when the order was created | 
**trader_address** | **str** | The trader address (hex format) | 
**order_address** | **str** | The order address (hex format) | 
**creation_transaction_hash** | **str** | The transaction hash of the order creation | 
**order_class_hash** | **str** | The order class hash | 
**sell_token_address** | **str** | The sell token address (hex format) | 
**sell_amount** | **str** | The total amount you want to invest (hex format) | 
**sell_amount_per_cycle** | **str** | The amount that will be sold at each iteration (hex format) | 
**buy_token_address** | **str** | The buy token address (hex format) | 
**start_date** | **datetime** | The start date of the order | 
**end_date** | **datetime** | The end date of the order | 
**close_date** | **datetime** | The close date of the order | [optional] 
**frequency** | [**OrderResponseDtoFrequency**](OrderResponseDtoFrequency.md) |  | 
**iterations** | **int** | The number of iterations | 
**status** | **str** | The order status | 
**pricing_strategy** | [**PricingStrategy**](PricingStrategy.md) |  | [optional] 
**amount_sold** | **str** | The amount already sold | 
**amount_bought** | **str** | The amount already bought | 
**average_amount_bought** | **str** | The average amount sold | 
**executed_trades_count** | **int** | The number of executed trades | 
**cancelled_trades_count** | **int** | The number of cancelled trades | 
**pending_trades_count** | **int** | The number of pending trades | 
**trades** | [**List[TradeResponseDto]**](TradeResponseDto.md) | The trades | 

## Example

```python
from avnu_python_client.models.order_response_dto import OrderResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseDto from a JSON string
order_response_dto_instance = OrderResponseDto.from_json(json)
# print the JSON string representation of the object
print(OrderResponseDto.to_json())

# convert the object into a dict
order_response_dto_dict = order_response_dto_instance.to_dict()
# create an instance of OrderResponseDto from a dict
order_response_dto_from_dict = OrderResponseDto.from_dict(order_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



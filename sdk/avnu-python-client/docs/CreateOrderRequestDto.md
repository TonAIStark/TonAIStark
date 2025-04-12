# CreateOrderRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trader_address** | **str** | The trader address (hex format) | 
**sell_token_address** | **str** | The sell token address (hex format) | 
**sell_amount** | **str** | The total amount you want to invest (hex format) | 
**sell_amount_per_cycle** | **str** | The amount that will be sold at each iteration (hex format) | 
**buy_token_address** | **str** | The sell token address (hex format) | 
**frequency** | [**CreateOrderRequestDtoFrequency**](CreateOrderRequestDtoFrequency.md) |  | 
**start_date** | **datetime** | You can choose when you want the order to start. By default, it starts immediately | [optional] 
**pricing_strategy** | [**PricingStrategy**](PricingStrategy.md) |  | 

## Example

```python
from avnu_python_client.models.create_order_request_dto import CreateOrderRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequestDto from a JSON string
create_order_request_dto_instance = CreateOrderRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequestDto.to_json())

# convert the object into a dict
create_order_request_dto_dict = create_order_request_dto_instance.to_dict()
# create an instance of CreateOrderRequestDto from a dict
create_order_request_dto_from_dict = CreateOrderRequestDto.from_dict(create_order_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



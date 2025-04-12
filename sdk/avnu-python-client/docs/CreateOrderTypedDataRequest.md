# CreateOrderTypedDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trader_address** | **str** | The user&#39;s address | 
**sell_token_address** | **str** |  | 
**sell_amount** | **str** |  | 
**sell_amount_per_cycle** | **str** |  | 
**buy_token_address** | **str** |  | 
**frequency** | [**CreateOrderTypedDataRequestFrequency**](CreateOrderTypedDataRequestFrequency.md) |  | 
**start_date** | **datetime** |  | [optional] 
**pricing_strategy** | [**PricingStrategy**](PricingStrategy.md) |  | 
**gas_token_address** | **str** | The gas token&#39;s address the user wants to spend to execute the tx. | 
**max_gas_token_amount** | **str** |  | [optional] 

## Example

```python
from avnu_python_client.models.create_order_typed_data_request import CreateOrderTypedDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderTypedDataRequest from a JSON string
create_order_typed_data_request_instance = CreateOrderTypedDataRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderTypedDataRequest.to_json())

# convert the object into a dict
create_order_typed_data_request_dict = create_order_typed_data_request_instance.to_dict()
# create an instance of CreateOrderTypedDataRequest from a dict
create_order_typed_data_request_from_dict = CreateOrderTypedDataRequest.from_dict(create_order_typed_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



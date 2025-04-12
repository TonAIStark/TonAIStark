# CancelOrderTypedDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trader_address** | **str** | The user&#39;s address | 
**gas_token_address** | **str** | The gas token&#39;s address the user wants to spend to execute the tx. | 
**max_gas_token_amount** | **str** |  | [optional] 

## Example

```python
from avnu_python_client.models.cancel_order_typed_data_request import CancelOrderTypedDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderTypedDataRequest from a JSON string
cancel_order_typed_data_request_instance = CancelOrderTypedDataRequest.from_json(json)
# print the JSON string representation of the object
print(CancelOrderTypedDataRequest.to_json())

# convert the object into a dict
cancel_order_typed_data_request_dict = cancel_order_typed_data_request_instance.to_dict()
# create an instance of CancelOrderTypedDataRequest from a dict
cancel_order_typed_data_request_from_dict = CancelOrderTypedDataRequest.from_dict(cancel_order_typed_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



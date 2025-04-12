# BuildSwapTypedDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | The unique id of the quote | 
**taker_address** | **str** | The address which will fill the quote. Not required if then taker address was provided during the quote request | [optional] 
**slippage** | **float** | The maximum acceptable slippage of the buyAmount amount. Default value is 1%. This value is ignored if slippage is not applicable to the selected quote.Min value for gasless transaction is 0.5% | 
**include_approve** | **bool** | If true, the typed data will contains the approve call | 
**gas_token_address** | **str** | The gas token&#39;s address the user wants to spend to execute the tx. | 
**max_gas_token_amount** | **str** |  | [optional] 

## Example

```python
from avnu_python_client.models.build_swap_typed_data_request import BuildSwapTypedDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildSwapTypedDataRequest from a JSON string
build_swap_typed_data_request_instance = BuildSwapTypedDataRequest.from_json(json)
# print the JSON string representation of the object
print(BuildSwapTypedDataRequest.to_json())

# convert the object into a dict
build_swap_typed_data_request_dict = build_swap_typed_data_request_instance.to_dict()
# create an instance of BuildSwapTypedDataRequest from a dict
build_swap_typed_data_request_from_dict = BuildSwapTypedDataRequest.from_dict(build_swap_typed_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



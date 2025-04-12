# ExecuteSwapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** | The hash of the transaction | 
**gas_token_address** | **str** | The address of the gas token used to pay gas fees | [optional] 
**gas_token_amount** | **str** | The amount of gas token used to pay gas fees | [optional] 

## Example

```python
from avnu_python_client.models.execute_swap_response import ExecuteSwapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteSwapResponse from a JSON string
execute_swap_response_instance = ExecuteSwapResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteSwapResponse.to_json())

# convert the object into a dict
execute_swap_response_dict = execute_swap_response_instance.to_dict()
# create an instance of ExecuteSwapResponse from a dict
execute_swap_response_from_dict = ExecuteSwapResponse.from_dict(execute_swap_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



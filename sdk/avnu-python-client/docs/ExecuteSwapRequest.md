# ExecuteSwapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | The unique id of the quote | 
**signature** | **List[str]** |  | 

## Example

```python
from avnu_python_client.models.execute_swap_request import ExecuteSwapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteSwapRequest from a JSON string
execute_swap_request_instance = ExecuteSwapRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteSwapRequest.to_json())

# convert the object into a dict
execute_swap_request_dict = execute_swap_request_instance.to_dict()
# create an instance of ExecuteSwapRequest from a dict
execute_swap_request_from_dict = ExecuteSwapRequest.from_dict(execute_swap_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



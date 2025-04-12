# ExecuteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_hash** | **str** | The hash of the transaction | 

## Example

```python
from avnu_python_client.models.execute_response import ExecuteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteResponse from a JSON string
execute_response_instance = ExecuteResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteResponse.to_json())

# convert the object into a dict
execute_response_dict = execute_response_instance.to_dict()
# create an instance of ExecuteResponse from a dict
execute_response_from_dict = ExecuteResponse.from_dict(execute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



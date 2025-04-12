# ExecuteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_address** | **str** | The user&#39;s address | 
**typed_data** | **str** | The typed data that the user signed | 
**signature** | **List[str]** | The user&#39;s typed data signature | 
**deployment_data** | [**DeploymentDataDto**](DeploymentDataDto.md) |  | [optional] 

## Example

```python
from avnu_python_client.models.execute_request import ExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteRequest from a JSON string
execute_request_instance = ExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteRequest.to_json())

# convert the object into a dict
execute_request_dict = execute_request_instance.to_dict()
# create an instance of ExecuteRequest from a dict
execute_request_from_dict = ExecuteRequest.from_dict(execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



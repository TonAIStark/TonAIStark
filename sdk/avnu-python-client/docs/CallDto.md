# CallDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | The address of the contract to send call data to | 
**entrypoint** | **str** | The entrypoint | 
**calldata** | **List[str]** | The call data required to be sent to the to contract address | 

## Example

```python
from avnu_python_client.models.call_dto import CallDto

# TODO update the JSON string below
json = "{}"
# create an instance of CallDto from a JSON string
call_dto_instance = CallDto.from_json(json)
# print the JSON string representation of the object
print(CallDto.to_json())

# convert the object into a dict
call_dto_dict = call_dto_instance.to_dict()
# create an instance of CallDto from a dict
call_dto_from_dict = CallDto.from_dict(call_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Call

The list of calls that will be executed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | Contract&#39;s address | 
**entrypoint** | **str** | Entrypoint (can be in text format or the selector in hex format) | 
**calldata** | **List[str]** | calldata (list of felt) | 

## Example

```python
from avnu_python_client.models.call import Call

# TODO update the JSON string below
json = "{}"
# create an instance of Call from a JSON string
call_instance = Call.from_json(json)
# print the JSON string representation of the object
print(Call.to_json())

# convert the object into a dict
call_dict = call_instance.to_dict()
# create an instance of Call from a dict
call_from_dict = Call.from_dict(call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



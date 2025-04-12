# TypedDataMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Dict[str, object]** |  | [optional] 
**values** | **List[object]** |  | 
**is_empty** | **bool** |  | 
**size** | **int** |  | 
**entries** | [**List[TypedDataMessageEntriesInner]**](TypedDataMessageEntriesInner.md) |  | 
**keys** | **List[str]** |  | 

## Example

```python
from avnu_python_client.models.typed_data_message import TypedDataMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TypedDataMessage from a JSON string
typed_data_message_instance = TypedDataMessage.from_json(json)
# print the JSON string representation of the object
print(TypedDataMessage.to_json())

# convert the object into a dict
typed_data_message_dict = typed_data_message_instance.to_dict()
# create an instance of TypedDataMessage from a dict
typed_data_message_from_dict = TypedDataMessage.from_dict(typed_data_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TypedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **Dict[str, List[Type]]** |  | 
**primary_type** | **str** |  | 
**domain** | [**Domain**](Domain.md) |  | 
**message** | [**TypedDataMessage**](TypedDataMessage.md) |  | 

## Example

```python
from avnu_python_client.models.typed_data import TypedData

# TODO update the JSON string below
json = "{}"
# create an instance of TypedData from a JSON string
typed_data_instance = TypedData.from_json(json)
# print the JSON string representation of the object
print(TypedData.to_json())

# convert the object into a dict
typed_data_dict = typed_data_instance.to_dict()
# create an instance of TypedData from a dict
typed_data_from_dict = TypedData.from_dict(typed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# JsonPrimitive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**is_string** | **bool** |  | 

## Example

```python
from avnu_python_client.models.json_primitive import JsonPrimitive

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPrimitive from a JSON string
json_primitive_instance = JsonPrimitive.from_json(json)
# print the JSON string representation of the object
print(JsonPrimitive.to_json())

# convert the object into a dict
json_primitive_dict = json_primitive_instance.to_dict()
# create an instance of JsonPrimitive from a dict
json_primitive_from_dict = JsonPrimitive.from_dict(json_primitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



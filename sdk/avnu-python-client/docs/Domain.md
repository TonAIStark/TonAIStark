# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**JsonPrimitive**](JsonPrimitive.md) |  | 
**version** | [**JsonPrimitive**](JsonPrimitive.md) |  | 
**chain_id** | [**JsonPrimitive**](JsonPrimitive.md) |  | 
**revision** | [**JsonPrimitive**](JsonPrimitive.md) |  | [optional] 
**resolved_revision** | **str** |  | 
**separator_namelib** | **str** |  | 

## Example

```python
from avnu_python_client.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



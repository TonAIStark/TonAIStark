# Pageable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**sort** | **List[str]** |  | [optional] 

## Example

```python
from avnu_python_client.models.pageable import Pageable

# TODO update the JSON string below
json = "{}"
# create an instance of Pageable from a JSON string
pageable_instance = Pageable.from_json(json)
# print the JSON string representation of the object
print(Pageable.to_json())

# convert the object into a dict
pageable_dict = pageable_instance.to_dict()
# create an instance of Pageable from a dict
pageable_from_dict = Pageable.from_dict(pageable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



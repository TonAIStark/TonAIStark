# PageActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ActionDto]**](ActionDto.md) |  | 
**size** | **int** |  | 
**number** | **int** |  | 
**total_elements** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from avnu_python_client.models.page_action_dto import PageActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageActionDto from a JSON string
page_action_dto_instance = PageActionDto.from_json(json)
# print the JSON string representation of the object
print(PageActionDto.to_json())

# convert the object into a dict
page_action_dto_dict = page_action_dto_instance.to_dict()
# create an instance of PageActionDto from a dict
page_action_dto_from_dict = PageActionDto.from_dict(page_action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PageTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[TokenDto]**](TokenDto.md) |  | 
**size** | **int** |  | 
**number** | **int** |  | 
**total_elements** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from avnu_python_client.models.page_token_dto import PageTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of PageTokenDto from a JSON string
page_token_dto_instance = PageTokenDto.from_json(json)
# print the JSON string representation of the object
print(PageTokenDto.to_json())

# convert the object into a dict
page_token_dto_dict = page_token_dto_instance.to_dict()
# create an instance of PageTokenDto from a dict
page_token_dto_from_dict = PageTokenDto.from_dict(page_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



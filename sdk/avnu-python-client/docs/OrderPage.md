# OrderPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[OrderResponseDto]**](OrderResponseDto.md) |  | 
**size** | **int** |  | 
**number** | **int** |  | 
**total_elements** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from avnu_python_client.models.order_page import OrderPage

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPage from a JSON string
order_page_instance = OrderPage.from_json(json)
# print the JSON string representation of the object
print(OrderPage.to_json())

# convert the object into a dict
order_page_dict = order_page_instance.to_dict()
# create an instance of OrderPage from a dict
order_page_from_dict = OrderPage.from_dict(order_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



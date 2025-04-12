# Route


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the source | 
**address** | **str** | The address of the source | 
**percent** | **float** | The percentage distribution of sellToken. 1 is 100% | 
**sell_token_address** | **str** | The token address user wants to sell | 
**buy_token_address** | **str** | The token address user wants to buy | 

## Example

```python
from avnu_python_client.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print(Route.to_json())

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_from_dict = Route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



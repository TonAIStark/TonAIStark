# Gasless


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | If true, the quote can be executed using gasless | 
**gas_token_prices** | [**List[GasTokenPriceDto]**](GasTokenPriceDto.md) |  | 

## Example

```python
from avnu_python_client.models.gasless import Gasless

# TODO update the JSON string below
json = "{}"
# create an instance of Gasless from a JSON string
gasless_instance = Gasless.from_json(json)
# print the JSON string representation of the object
print(Gasless.to_json())

# convert the object into a dict
gasless_dict = gasless_instance.to_dict()
# create an instance of Gasless from a dict
gasless_from_dict = Gasless.from_dict(gasless_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



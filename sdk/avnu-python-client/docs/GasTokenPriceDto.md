# GasTokenPriceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_address** | **str** | The address of the gas token | 
**gas_fees_in_gas_token** | **str** | The estimated amount of gas token to pay the gas fees | 
**gas_fees_in_usd** | **float** | The estimated amount of gas token to pay the gas fees in usd | 

## Example

```python
from avnu_python_client.models.gas_token_price_dto import GasTokenPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of GasTokenPriceDto from a JSON string
gas_token_price_dto_instance = GasTokenPriceDto.from_json(json)
# print the JSON string representation of the object
print(GasTokenPriceDto.to_json())

# convert the object into a dict
gas_token_price_dto_dict = gas_token_price_dto_instance.to_dict()
# create an instance of GasTokenPriceDto from a dict
gas_token_price_dto_from_dict = GasTokenPriceDto.from_dict(gas_token_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



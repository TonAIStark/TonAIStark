# GasFeeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_fee_amount** | **str** |  | [optional] 
**gas_fee_amount_usd** | **float** |  | [optional] 
**gas_fee_token_address** | **str** |  | [optional] 

## Example

```python
from avnu_python_client.models.gas_fee_info import GasFeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GasFeeInfo from a JSON string
gas_fee_info_instance = GasFeeInfo.from_json(json)
# print the JSON string representation of the object
print(GasFeeInfo.to_json())

# convert the object into a dict
gas_fee_info_dict = gas_fee_info_instance.to_dict()
# create an instance of GasFeeInfo from a dict
gas_fee_info_from_dict = GasFeeInfo.from_dict(gas_fee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



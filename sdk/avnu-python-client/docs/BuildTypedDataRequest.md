# BuildTypedDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_address** | **str** | The user&#39;s address | 
**calls** | [**List[Call]**](Call.md) | The list of calls that will be executed | 
**gas_token_address** | **str** | Gas token address.If null, there is two options:1. the user must have a reward compatible with the calls. In this case, the reward&#39;s sponsor will pay the gas fees in ETH.2. the api-key header must be field. The api-key&#39;s owner will be charged for the consumed gas fees in ETH | [optional] 
**max_gas_token_amount** | **str** | Max gas token amountIf null, there is two options:1. the user must have a reward compatible with the calls. In this case, the reward&#39;s sponsor will pay the gas fees in ETH.2. the api-key header must be field. The api-key&#39;s owner will be charged for the consumed gas fees in ETH | [optional] 
**account_class_hash** | **str** | Only set this field when the account is not deployed. When the accountClassHash is defined, the API will not check the gasless compatibility by calling the supportsInterface entrypoint but will instead look into an internal map. If the classHash is not supported by the API, please contact us so we can quickly add support. | [optional] 

## Example

```python
from avnu_python_client.models.build_typed_data_request import BuildTypedDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildTypedDataRequest from a JSON string
build_typed_data_request_instance = BuildTypedDataRequest.from_json(json)
# print the JSON string representation of the object
print(BuildTypedDataRequest.to_json())

# convert the object into a dict
build_typed_data_request_dict = build_typed_data_request_instance.to_dict()
# create an instance of BuildTypedDataRequest from a dict
build_typed_data_request_from_dict = BuildTypedDataRequest.from_dict(build_typed_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



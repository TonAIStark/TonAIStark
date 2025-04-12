# DeploymentDataDto

When this field is set, the paymaster will deploy the user's account before executing the typed data. To retrieve the deployment data, you can read https://community.starknet.io/t/snip-deployment-interface-between-dapps-and-wallets/101923. For now, the paymaster only allows the deployment of account for sponsored transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_hash** | **str** |  | 
**salt** | **str** |  | 
**unique** | **str** |  | 
**calldata** | **List[str]** |  | 
**sigdata** | **List[str]** |  | 

## Example

```python
from avnu_python_client.models.deployment_data_dto import DeploymentDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDataDto from a JSON string
deployment_data_dto_instance = DeploymentDataDto.from_json(json)
# print the JSON string representation of the object
print(DeploymentDataDto.to_json())

# convert the object into a dict
deployment_data_dto_dict = deployment_data_dto_instance.to_dict()
# create an instance of DeploymentDataDto from a dict
deployment_data_dto_from_dict = DeploymentDataDto.from_dict(deployment_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DeployAccountRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_address** | **str** |  | 
**deployment_data** | [**DeploymentDataDto**](DeploymentDataDto.md) |  | 

## Example

```python
from avnu_python_client.models.deploy_account_request_dto import DeployAccountRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAccountRequestDto from a JSON string
deploy_account_request_dto_instance = DeployAccountRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeployAccountRequestDto.to_json())

# convert the object into a dict
deploy_account_request_dto_dict = deploy_account_request_dto_instance.to_dict()
# create an instance of DeployAccountRequestDto from a dict
deploy_account_request_dto_from_dict = DeployAccountRequestDto.from_dict(deploy_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



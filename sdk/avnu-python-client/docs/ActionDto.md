# ActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_number** | **int** |  | 
**var_date** | **datetime** |  | 
**transaction_hash** | **str** |  | 
**gas_fee** | [**GasFeeInfo**](GasFeeInfo.md) |  | [optional] 
**type** | **str** |  | 
**metadata** | **object** |  | 

## Example

```python
from avnu_python_client.models.action_dto import ActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDto from a JSON string
action_dto_instance = ActionDto.from_json(json)
# print the JSON string representation of the object
print(ActionDto.to_json())

# convert the object into a dict
action_dto_dict = action_dto_instance.to_dict()
# create an instance of ActionDto from a dict
action_dto_from_dict = ActionDto.from_dict(action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



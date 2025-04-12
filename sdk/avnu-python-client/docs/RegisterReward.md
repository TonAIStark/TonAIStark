# RegisterReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The user&#39;s address | 
**campaign** | **str** | The name of the company&#39;s campaign | 
**protocol** | **str** | The protocol where the reward can be used | [optional] 
**free_tx** | **int** | The number of free transaction | 
**expiration_date** | **datetime** | Reward&#39;s expiration date | [optional] 
**whitelisted_calls** | [**List[WhitelistedCall]**](WhitelistedCall.md) | The list of whitelisted calls | 

## Example

```python
from avnu_python_client.models.register_reward import RegisterReward

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterReward from a JSON string
register_reward_instance = RegisterReward.from_json(json)
# print the JSON string representation of the object
print(RegisterReward.to_json())

# convert the object into a dict
register_reward_dict = register_reward_instance.to_dict()
# create an instance of RegisterReward from a dict
register_reward_from_dict = RegisterReward.from_dict(register_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



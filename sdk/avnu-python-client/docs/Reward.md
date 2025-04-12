# Reward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Reward&#39;s creation date | 
**address** | **str** | The user&#39;s address | 
**sponsor** | **str** | The company that will pay the gas fees | 
**campaign** | **str** | The name of the company&#39;s campaign | 
**protocol** | **str** | The protocol where the reward can be used | [optional] 
**free_tx** | **int** | The number of free transaction | 
**remaining_tx** | **int** | The number of remaining transactions | 
**expiration_date** | **datetime** | Reward&#39;s expiration date | [optional] 
**whitelisted_calls** | [**List[WhitelistedCall]**](WhitelistedCall.md) | The list of whitelisted calls | 

## Example

```python
from avnu_python_client.models.reward import Reward

# TODO update the JSON string below
json = "{}"
# create an instance of Reward from a JSON string
reward_instance = Reward.from_json(json)
# print the JSON string representation of the object
print(Reward.to_json())

# convert the object into a dict
reward_dict = reward_instance.to_dict()
# create an instance of Reward from a dict
reward_from_dict = Reward.from_dict(reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



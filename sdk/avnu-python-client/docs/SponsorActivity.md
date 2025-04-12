# SponsorActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The sponsor&#39;s name | 
**succeeded_tx_count** | **int** | The number of succeeded transactions | 
**reverted_tx_count** | **int** | The number of reverted transactions | 
**tx_count** | **int** | The total number executed transactions | 
**succeeded_gas_fees** | **str** | The amount of ETH paid for succeeded transactions | 
**reverted_gas_fees** | **str** | The amount of ETH paid for reverted transactions | 
**gas_fees** | **str** | The amount of ETH paid for all transactions | 
**remaining_credits** | **str** | The remaining credits. When zero, please contact us so you can recharge | 

## Example

```python
from avnu_python_client.models.sponsor_activity import SponsorActivity

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorActivity from a JSON string
sponsor_activity_instance = SponsorActivity.from_json(json)
# print the JSON string representation of the object
print(SponsorActivity.to_json())

# convert the object into a dict
sponsor_activity_dict = sponsor_activity_instance.to_dict()
# create an instance of SponsorActivity from a dict
sponsor_activity_from_dict = SponsorActivity.from_dict(sponsor_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



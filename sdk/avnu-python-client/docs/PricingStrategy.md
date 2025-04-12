# PricingStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_to_min_amount** | **str** | The buy token&#39;s min price you&#39;re agree to execute a trade | [optional] 
**token_to_max_amount** | **str** | The buy token&#39;s max price you&#39;re agree to execute a trade | [optional] 

## Example

```python
from avnu_python_client.models.pricing_strategy import PricingStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of PricingStrategy from a JSON string
pricing_strategy_instance = PricingStrategy.from_json(json)
# print the JSON string representation of the object
print(PricingStrategy.to_json())

# convert the object into a dict
pricing_strategy_dict = pricing_strategy_instance.to_dict()
# create an instance of PricingStrategy from a dict
pricing_strategy_from_dict = PricingStrategy.from_dict(pricing_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



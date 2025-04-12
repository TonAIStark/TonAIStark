# WhitelistedCall

The list of whitelisted calls

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | The value can be &#39;*&#39; if all contracts are whitelisted or can be the contract address (hex format) | 
**entrypoint** | **str** | The value can be &#39;*&#39; if all entrypoint are whitelisted or can be the entrypoint name (string format) | 

## Example

```python
from avnu_python_client.models.whitelisted_call import WhitelistedCall

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistedCall from a JSON string
whitelisted_call_instance = WhitelistedCall.from_json(json)
# print the JSON string representation of the object
print(WhitelistedCall.to_json())

# convert the object into a dict
whitelisted_call_dict = whitelisted_call_instance.to_dict()
# create an instance of WhitelistedCall from a dict
whitelisted_call_from_dict = WhitelistedCall.from_dict(whitelisted_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



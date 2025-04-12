# BuildSwapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain&#39;s id | 
**contract_address** | **str** | The address of the contract to send call data to | 
**entrypoint** | **str** | The entrypoint | 
**calldata** | **List[str]** | The call data required to be sent to the to contract address | 

## Example

```python
from avnu_python_client.models.build_swap_response import BuildSwapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuildSwapResponse from a JSON string
build_swap_response_instance = BuildSwapResponse.from_json(json)
# print the JSON string representation of the object
print(BuildSwapResponse.to_json())

# convert the object into a dict
build_swap_response_dict = build_swap_response_instance.to_dict()
# create an instance of BuildSwapResponse from a dict
build_swap_response_from_dict = BuildSwapResponse.from_dict(build_swap_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



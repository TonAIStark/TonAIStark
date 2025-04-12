# BuildSwapRequestDtoV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | The unique id of the quote | 
**taker_address** | **str** | The address which will fill the quote. Not required if then taker address was provided during the quote request | [optional] 
**slippage** | **float** | The maximum acceptable slippage of the buyAmount amount. Default value is 5%. This value is ignored if slippage is not applicable to the selected quote | 
**include_approve** | **bool** | If true, the response will contains the approve call (if necessary) | 

## Example

```python
from avnu_python_client.models.build_swap_request_dto_v2 import BuildSwapRequestDtoV2

# TODO update the JSON string below
json = "{}"
# create an instance of BuildSwapRequestDtoV2 from a JSON string
build_swap_request_dto_v2_instance = BuildSwapRequestDtoV2.from_json(json)
# print the JSON string representation of the object
print(BuildSwapRequestDtoV2.to_json())

# convert the object into a dict
build_swap_request_dto_v2_dict = build_swap_request_dto_v2_instance.to_dict()
# create an instance of BuildSwapRequestDtoV2 from a dict
build_swap_request_dto_v2_from_dict = BuildSwapRequestDtoV2.from_dict(build_swap_request_dto_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



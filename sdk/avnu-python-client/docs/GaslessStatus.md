# GaslessStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | The gasless status | 

## Example

```python
from avnu_python_client.models.gasless_status import GaslessStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GaslessStatus from a JSON string
gasless_status_instance = GaslessStatus.from_json(json)
# print the JSON string representation of the object
print(GaslessStatus.to_json())

# convert the object into a dict
gasless_status_dict = gasless_status_instance.to_dict()
# create an instance of GaslessStatus from a dict
gasless_status_from_dict = GaslessStatus.from_dict(gasless_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateOrderTypedDataRequestFrequency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | [optional] 
**zero** | **bool** |  | [optional] 
**nano** | **int** |  | [optional] 
**negative** | **bool** |  | [optional] 
**units** | [**List[CreateOrderTypedDataRequestFrequencyUnitsInner]**](CreateOrderTypedDataRequestFrequencyUnitsInner.md) |  | [optional] 

## Example

```python
from avnu_python_client.models.create_order_typed_data_request_frequency import CreateOrderTypedDataRequestFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderTypedDataRequestFrequency from a JSON string
create_order_typed_data_request_frequency_instance = CreateOrderTypedDataRequestFrequency.from_json(json)
# print the JSON string representation of the object
print(CreateOrderTypedDataRequestFrequency.to_json())

# convert the object into a dict
create_order_typed_data_request_frequency_dict = create_order_typed_data_request_frequency_instance.to_dict()
# create an instance of CreateOrderTypedDataRequestFrequency from a dict
create_order_typed_data_request_frequency_from_dict = CreateOrderTypedDataRequestFrequency.from_dict(create_order_typed_data_request_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



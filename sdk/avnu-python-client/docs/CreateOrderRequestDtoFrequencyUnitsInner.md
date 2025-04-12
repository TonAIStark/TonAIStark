# CreateOrderRequestDtoFrequencyUnitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_estimated** | **bool** |  | [optional] 
**duration** | [**CreateOrderRequestDtoFrequencyUnitsInnerDuration**](CreateOrderRequestDtoFrequencyUnitsInnerDuration.md) |  | [optional] 
**time_based** | **bool** |  | [optional] 
**date_based** | **bool** |  | [optional] 

## Example

```python
from avnu_python_client.models.create_order_request_dto_frequency_units_inner import CreateOrderRequestDtoFrequencyUnitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequestDtoFrequencyUnitsInner from a JSON string
create_order_request_dto_frequency_units_inner_instance = CreateOrderRequestDtoFrequencyUnitsInner.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequestDtoFrequencyUnitsInner.to_json())

# convert the object into a dict
create_order_request_dto_frequency_units_inner_dict = create_order_request_dto_frequency_units_inner_instance.to_dict()
# create an instance of CreateOrderRequestDtoFrequencyUnitsInner from a dict
create_order_request_dto_frequency_units_inner_from_dict = CreateOrderRequestDtoFrequencyUnitsInner.from_dict(create_order_request_dto_frequency_units_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



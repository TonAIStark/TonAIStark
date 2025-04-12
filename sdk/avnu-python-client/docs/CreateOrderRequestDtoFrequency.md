# CreateOrderRequestDtoFrequency

The duration between each iteration. Follows ISO 8601 standard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** |  | [optional] 
**zero** | **bool** |  | [optional] 
**nano** | **int** |  | [optional] 
**negative** | **bool** |  | [optional] 
**units** | [**List[CreateOrderRequestDtoFrequencyUnitsInner]**](CreateOrderRequestDtoFrequencyUnitsInner.md) |  | [optional] 

## Example

```python
from avnu_python_client.models.create_order_request_dto_frequency import CreateOrderRequestDtoFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequestDtoFrequency from a JSON string
create_order_request_dto_frequency_instance = CreateOrderRequestDtoFrequency.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequestDtoFrequency.to_json())

# convert the object into a dict
create_order_request_dto_frequency_dict = create_order_request_dto_frequency_instance.to_dict()
# create an instance of CreateOrderRequestDtoFrequency from a dict
create_order_request_dto_frequency_from_dict = CreateOrderRequestDtoFrequency.from_dict(create_order_request_dto_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



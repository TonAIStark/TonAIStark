# OrderResponseDtoFrequency

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
from avnu_python_client.models.order_response_dto_frequency import OrderResponseDtoFrequency

# TODO update the JSON string below
json = "{}"
# create an instance of OrderResponseDtoFrequency from a JSON string
order_response_dto_frequency_instance = OrderResponseDtoFrequency.from_json(json)
# print the JSON string representation of the object
print(OrderResponseDtoFrequency.to_json())

# convert the object into a dict
order_response_dto_frequency_dict = order_response_dto_frequency_instance.to_dict()
# create an instance of OrderResponseDtoFrequency from a dict
order_response_dto_frequency_from_dict = OrderResponseDtoFrequency.from_dict(order_response_dto_frequency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TradeResponseDto

The trades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sell_amount** | **str** | The amount sold | 
**sell_amount_in_usd** | **float** | The amount sold in USD | [optional] 
**buy_amount** | **str** | The amount bought | [optional] 
**buy_amount_in_usd** | **float** | The amount bought in USD | [optional] 
**expected_trade_date** | **datetime** | The expected trade date | 
**status** | **str** | The actual trade date | 
**actual_trade_date** | **datetime** | The actual trade date | [optional] 
**tx_hash** | **str** | The transaction hash of the trade | [optional] 
**error_reason** | **str** | The error reason. Defined only if the trade failed | [optional] 

## Example

```python
from avnu_python_client.models.trade_response_dto import TradeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TradeResponseDto from a JSON string
trade_response_dto_instance = TradeResponseDto.from_json(json)
# print the JSON string representation of the object
print(TradeResponseDto.to_json())

# convert the object into a dict
trade_response_dto_dict = trade_response_dto_instance.to_dict()
# create an instance of TradeResponseDto from a dict
trade_response_dto_from_dict = TradeResponseDto.from_dict(trade_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



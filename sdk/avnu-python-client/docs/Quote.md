# Quote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** | The unique id of the quote | 
**sell_token_address** | **str** | The token address user wants to sell | 
**sell_amount** | **str** | The amount of sellAmount that would be sold in this swap | 
**sell_amount_in_usd** | **float** | The amount of sellAmount that would be sold in this swap in usd | 
**buy_token_address** | **str** | The token address user wants to buy | 
**buy_amount** | **str** | The amount of buyToken that would be bought in this swap | 
**buy_amount_in_usd** | **float** | The amount of buyToken that would be bought in this swap in usd | 
**buy_amount_without_fees** | **str** | The amount of buyToken without fees | 
**buy_amount_without_fees_in_usd** | **float** | The amount of buyToken without fees in usd | 
**estimated_amount** | **bool** | If true, user should define a slippage when he executes the quote | 
**chain_id** | **str** | The chain&#39;s id | 
**block_number** | **str** | Defined when quote comes from a DEX | [optional] 
**expiry** | **float** | Unix timestamp when quotes expires in seconds | [optional] 
**routes** | [**List[Route]**](Route.md) |  | 
**gas_fees** | **str** | The estimated amount of gas fees | 
**gas_fees_in_usd** | **float** | The estimated amount of gas fees in USD | [optional] 
**avnu_fees** | **str** | The actual fees taken by AVNU | 
**avnu_fees_in_usd** | **float** | The actual fees taken by AVNU is usd | 
**avnu_fees_bps** | **str** | The fees in bps taken by AVNU | 
**integrator_fees** | **str** | The actual fees taken by the integrator | 
**integrator_fees_in_usd** | **float** | The actual fees taken by the integrator in usd | 
**integrator_fees_bps** | **str** | The fees in bps taken by the integrator | 
**price_ratio_usd** | **float** | Price ratio in usd and in bps | 
**liquidity_source** | **str** | The type of liquidity source | 
**sell_token_price_in_usd** | **float** | The amount in USD to buy 1 sellToken | [optional] 
**buy_token_price_in_usd** | **float** | The amount in USD to buy 1 buyToken | [optional] 
**gasless** | [**Gasless**](Gasless.md) |  | 

## Example

```python
from avnu_python_client.models.quote import Quote

# TODO update the JSON string below
json = "{}"
# create an instance of Quote from a JSON string
quote_instance = Quote.from_json(json)
# print the JSON string representation of the object
print(Quote.to_json())

# convert the object into a dict
quote_dict = quote_instance.to_dict()
# create an instance of Quote from a dict
quote_from_dict = Quote.from_dict(quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



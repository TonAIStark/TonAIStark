import json
import requests
from typing import Annotated, TypedDict

from langgraph.types import StreamWriter
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool

from ..tokens import SUPPORTED_STARKNET_TOKENS
from ..utils import dec_2_erc20hex


KEYS_TO_EXTRACT = [
    'quoteId',
    'sellAmount',
    'sellAmountInUsd',
    'buyAmount',
    'buyAmountInUsd',
    'priceRatioUsd'    
]


@tool
def get_swap_quota_tool(
    token_to_buy: Annotated[str, "The symbol or name of the token the user wants to buy (e.g., 'ETH', 'USDC'). Must be one of the supported Starknet tokens."],
    token_to_sell: Annotated[str, "The symbol or name of the token the user wants to sell (e.g., 'STRK', 'DAI'). Must be one of the supported Starknet tokens."],
    sell_amount: Annotated[str, "The amount of the `token_to_sell` the user wants to exchange, represented as a string (e.g., '1.5', '100')."]
) -> str:
    """
    Fetches the best swap quote for exchanging a specified amount of one supported Starknet token for another using the AVNU API.
    This tool identifies the most favorable exchange rate available through the AVNU protocol aggregator on Starknet.
    It requires the symbols of the tokens to be bought and sold, and the quantity of the token being sold.
    """
    pass # Implementation is handled by get_swap_quota_streamed


class SwapQuotaInput(TypedDict):
    """
    Defines the structure for the input data required by the `get_swap_quota_streamed` function.
    It includes the symbols for the tokens involved in the swap, the amount to sell,
    and the unique identifier for the originating tool call.
    """
    token_to_buy: str
    token_to_sell: str
    sell_amount: str
    tool_call_id: str


async def get_swap_quota_streamed(input: SwapQuotaInput, writer: StreamWriter):
    """
    Asynchronously fetches swap quotes from the AVNU Starknet API based on the provided input dictionary.
    """
    token_to_buy  = input['token_to_buy']
    token_to_sell = input['token_to_sell']
    tool_call_id  = input["tool_call_id"]
    sell_amount   = input['sell_amount']
    
    if token_to_buy not in SUPPORTED_STARKNET_TOKENS:
        print(f'Specified token to buy ({token_to_buy}) not supported')
        msg = ToolMessage(content=f'Token ({token_to_buy}) not supported', tool_call_id=tool_call_id)    
        return {'messages': [msg], 'swap_data': None}   
    
    if token_to_sell not in SUPPORTED_STARKNET_TOKENS:
        print(f'Specified token to sell ({token_to_sell}) not supported')
        msg = ToolMessage(content=f'Token ({token_to_sell}) not supported', tool_call_id=tool_call_id)    
        return {'messages': [msg], 'swap_data': None}
    
    b_token = SUPPORTED_STARKNET_TOKENS[token_to_buy]
    s_token = SUPPORTED_STARKNET_TOKENS[token_to_sell] 

    # sell amount should be float, but needs to be
    # converted to hex as indicated in ERC20 contracts
    sell_amount_hex = dec_2_erc20hex(float(sell_amount), s_token['decimals'])

    # do the HTTP request
    base_url = f"https://starknet.api.avnu.fi/swap/v2/quotes"
    headers  = {"accept": "application/json"}
    qparams  = {
        'sellTokenAddress': s_token['address'], 
        'buyTokenAddress':  b_token['address'], 
        'sellAmount':       sell_amount_hex
    }

    try:
        response = requests.get(base_url, params=qparams, headers=headers)
        response.raise_for_status()
        results = response.json()
    except:
        print(f'HTTP error when requesting swap quotes.')
        msg = ToolMessage(content=f'HTTP error when requesting swap quotes.', tool_call_id=tool_call_id)    
        return {'messages': [msg], 'swap_data': None}

    if len(results) == 0:
        print(f'No quotas found')
        msg = ToolMessage(content='No quotas found', tool_call_id=tool_call_id)    
        return {'messages': [msg], 'swap_data': None }

    best_quote = results[0]
    best_quote = { k:best_quote[k] for k in KEYS_TO_EXTRACT }

    tool_message = ToolMessage(content=json.dumps(best_quote), tool_call_id=tool_call_id)
    return {
        'messages': [tool_message],
        'swap_data': best_quote
    }
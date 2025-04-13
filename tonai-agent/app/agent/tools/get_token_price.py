import os
import json
import httpx
import datetime
from typing import Annotated, TypedDict

from langgraph.types import StreamWriter
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool

from ..tokens import SUPPORTED_STARKNET_TOKENS


@tool
def get_token_price_tool(
    token: Annotated[str, "The ID of the cryptocurrency token (e.g., 'STRK' for starknet or 'ETH' for ethereum"],
    history_length_in_days: Annotated[int, "The number of past days for which to retrieve the price history."]
) -> str:
    """
    Retrieves the historical price of a cryptocurrency token for a specified number of past days.
    """
    pass


class TokenPriceInput(TypedDict):
    """
    Input dictionary for the get_token_price_streamed asynchronous function.
    It includes the cryptocurrency ID, the length of the historical data to fetch, 
    and the LangChain tool call ID.
    """
    token: str
    history_length_in_days: str
    tool_call_id: str


async def get_token_price_streamed(input: TokenPriceInput, writer: StreamWriter):
    """
    Asynchronously fetches the historical price data for a given cryptocurrency 
    token and streams the result as a LangChain ToolMessage.

    Args:
        input (TokenPriceInput): A dictionary containing TokenPriceInput args
        writer (StreamWriter): An asynchronous writer for streaming LangChain messages.

    Returns:
        dict: A dictionary containing a list with a single ToolMessage representing the fetched price data.
    """
    token = input['token']
    tool_call_id = input["tool_call_id"]
    history_length_in_days = int(input['history_length_in_days'])
    
    if token not in SUPPORTED_STARKNET_TOKENS:
        print(f'Specified token ({token}) not supported')
        msg = ToolMessage(content=f'Specified token ({token}) not supported', tool_call_id=tool_call_id)    
        return {'messages': [msg]}

    coin_id = SUPPORTED_STARKNET_TOKENS[token]['api_id']        
    to_date = datetime.datetime.now(datetime.timezone.utc)
    fr_date = to_date - datetime.timedelta(days=history_length_in_days)
    
    to = int(to_date.timestamp())
    fr = int(fr_date.timestamp())    

    coingecko_api_key = os.environ.get("COINGECKO_API_KEY")
    base_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    qparams  = {'from': fr, 'to': to, 'precision': 'full', 'vs_currency': 'usd'}
    headers  = {"accept": "application/json", "x-cg-demo-api-key": coingecko_api_key }

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=qparams, headers=headers)
        result_content = json.dumps(response.json())
        print('[TOOL get_token_price]', result_content[:15])    
        tool_message = ToolMessage(content=result_content, tool_call_id=tool_call_id)
    
    return {'messages': [tool_message]}
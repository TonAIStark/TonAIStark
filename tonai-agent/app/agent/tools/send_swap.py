# import json
# import requests
# from typing import Annotated, TypedDict

# from langgraph.types import StreamWriter
# from langchain_core.messages import ToolMessage
# from langchain_core.tools import tool

# from ..tokens import SUPPORTED_STARKNET_TOKENS
# from ..utils import dec_2_erc20hex


# @tool
# def send_swap_tool(
#     token_to_buy: Annotated[str, "The symbol or name of the token the user wants to buy (e.g., 'ETH', 'USDC'). Must be one of the supported Starknet tokens."],
#     token_to_sell: Annotated[str, "The symbol or name of the token the user wants to sell (e.g., 'STRK', 'DAI'). Must be one of the supported Starknet tokens."],
#     sell_amount: Annotated[str, "The amount of the `token_to_sell` the user wants to exchange, represented as a string (e.g., '1.5', '100')."]
# ) -> str:
#     """
#     TO FILL.
#     """
#     pass # Implementation is handled by get_swap_quota_streamed


# class SendSwapInput(TypedDict):
#     """
#     TO FILL.
#     """
#     token_to_buy: str
#     token_to_sell: str
#     sell_amount: str
#     tool_call_id: str


# async def send_swap_streamed(input: SendSwapInput, writer: StreamWriter):
#     """
#     TO FILL.
#     """
#     quote_id  = input['quote_id']
#     token_to_sell = input['token_to_sell']
#     tool_call_id  = input["tool_call_id"]
#     sell_amount   = input['sell_amount']
    
#     url = "https://starknet.api.avnu.fi/swap/v2/build"
#     headers = {'Content-Type': 'application/json'}
#     payload = {
#         "quoteId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
#         "takerAddress": "0x052D8E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89",
#         "slippage": 0.05,
#         "includeApprove": True
#     }

#     try:
#         response = requests.post(url, headers=headers, data=json.dumps(payload))
#         response.raise_for_status()  # Raise an exception for bad status codes
#         print("Request successful!")
#         print("Response JSON:")
#         print(response.json())

#     except:
#         print(f'HTTP error when sending swap.')
#         msg = ToolMessage(content=f'HTTP error when sending swap.', tool_call_id=tool_call_id)    
#         return {'messages': [msg]}

#     # tool_message = ToolMessage(content=best_quote, tool_call_id=tool_call_id)
#     # return {'messages': [tool_message]}
# import os
# import json
# import httpx
# import datetime
# from typing import Annotated, TypedDict

# from langgraph.types import StreamWriter
# from langchain_core.messages import ToolMessage
# from langchain_core.tools import tool


# @tool
# def sign_contract_tool() -> str:
#     """
#     Sign the proposed contract.
#     """
#     pass


# class SignContractInput(TypedDict):
#     """
#     """
#     tool_call_id: str


# async def sign_contract_streamed(input: SignContractInput, writer: StreamWriter):
#     """
#     """       
#     print('sign contract called.')
        
#     tool_call_id = input["tool_call_id"]
#     tool_message = ToolMessage(content='ok', tool_call_id=tool_call_id)
#     return {'messages': [tool_message]}
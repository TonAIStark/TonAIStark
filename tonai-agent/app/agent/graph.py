import os
import json
import httpx
import datetime
from typing import Annotated, TypedDict, Sequence, Literal
from dataclasses import field
from dotenv import load_dotenv

from langgraph import graph as lgraph
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import StreamWriter, interrupt, Send
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, ToolMessage, AnyMessage
from langchain_core.tools import tool

from .prompts import SYSTEM_PROMPT
from .tools.get_token_price import (
    get_token_price_tool,
    get_token_price_streamed,
)
from .tools.get_swap_quota import (
    get_swap_quota_tool,
    get_swap_quota_streamed
)
# from .tools.sign_contract import (
#     sign_contract_tool,
#     sign_contract_streamed
# )

load_dotenv()

print('CoinGecko key')
print(os.environ.get("COINGECKO_API_KEY"))

print('OpenAI key')
print(os.environ.get("OPENAI_API_KEY"))


class State(lgraph.MessagesState):
    """
    State of the automa
    """
    messages: Annotated[Sequence[AnyMessage], add_messages] \
        = field(default_factory=list)
    
    swap_quote_id: dict = field(default_factory={})
    
#==============================================
# LLM agent
#==============================================

    
async def chatbot(state: State):
    """
    The LLM node definition.
    """     
    tools = [ 
        get_token_price_tool,
        get_swap_quota_tool,
    ]
    
    # llm = ChatOpenAI(model="gpt-3.5-turbo").bind_tools(tools)
    llm = ChatOpenAI(model="o3-mini").bind_tools(tools)
    
    # If the first message in state is not a SystemMessage, add one at the beginning
    if not state["messages"] or state["messages"][0].type != "system":
        state["messages"].insert(0, SystemMessage(content=SYSTEM_PROMPT))

    response = await llm.ainvoke(state["messages"])
    return {"messages": [response]}


#========================
# Building the graph.
#========================


_TOOLS_MAP = {
        
    'get_token_price_tool': lambda t: Send('get_token_price', {
        'token': t['args']['token'],
        'history_length_in_days': t['args']['history_length_in_days'],
        'tool_call_id': t['id']        
    }),
    
    'get_swap_quota_tool': lambda t: Send('get_swap_quota', {
        'tool_call_id': t['id'],
        'token_to_buy': t['args']['token_to_buy'],
        'token_to_sell': t['args']['token_to_sell'],
        'sell_amount': t['args']['sell_amount'],
    }),
    
}


def route_tool(state: State) -> str:
    """
    Route LLM chatbot through tools.
    Declare the tool into _TOOLS_MAP first!!
    """
    message = state["messages"][-1]
    if not message.tool_calls: return "__end__"
    
    send_list = []
    for tool in message.tool_calls:
        tool_name = tool['name']
        
        if tool_name not in _TOOLS_MAP:
            raise Exception(f'Found uknown tool call: {tool_name}')

        send_object = _TOOLS_MAP[tool_name](tool)
        send_list.append(send_object)
            
    return send_list if len(send_list) > 0 else "__end__"


workflow = lgraph.StateGraph(State)
workflow.add_node("chatbot", chatbot)
workflow.add_node("get_token_price", get_token_price_streamed)
workflow.add_node("get_swap_quota", get_swap_quota_streamed)

# debugging
workflow.add_edge(lgraph.START, "chatbot")
workflow.add_conditional_edges("chatbot", route_tool)
workflow.add_edge("get_token_price", "chatbot")
workflow.add_edge("get_swap_quota", "chatbot")

workflow.add_edge("chatbot", lgraph.END)


memory = MemorySaver()
graph = workflow.compile(checkpointer=memory)
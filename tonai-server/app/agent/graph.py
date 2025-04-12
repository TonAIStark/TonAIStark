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
    
    
#==============================================
# Is Odd tool
#==============================================
    
@tool
def is_odd_tool(
    number: Annotated[str, "The number (in str format) to be analysed"]
) -> str:
    """
    This tool determines if the number is even or odd.
    """
    pass


class IsOddInput(TypedDict):
    """
    """
    number: str
    tool_call_id: str


async def is_odd_streamed(input: IsOddInput, writer: StreamWriter):
    """
    """
    tool_number = input['number']
    tool_callid = input["tool_call_id"]    
    print(f'[TOOL is_odd] Il numero è {tool_number} e l\'ID è {tool_callid}')
    
    # tool action.
    result = "even" if int(tool_number) % 2 == 0 else "odd"
    
    msg = ToolMessage(content=result, tool_call_id=tool_callid)
    return { 'messages': [msg] }

    
#==============================================
# Get Crypto Prices Tool (New Tool)
#==============================================

@tool
def get_crypto_prices_tool(
    coin_id: Annotated[str, "The identifier for the cryptocurrency (e.g., 'bitcoin', 'ethereum')."],
    history_length_in_days: Annotated[int, "The number of days of historical price data to fetch, ending at the current time."]
) -> str:
    """
    Fetches historical market price data (price vs USD) for a given cryptocurrency
    for a specified number of past days, ending at the current time. Uses the CoinGecko API.
    """
    pass


class CryptoPricesInput(TypedDict):
    """
    """
    coin_id: str
    history_length_in_days: str
    tool_call_id: str


async def get_crypto_prices_streamed(input: CryptoPricesInput, writer: StreamWriter):
    """
    """        
    coin_id = input['coin_id']
    history_length_in_days = int(input['history_length_in_days'])
    tool_call_id = input["tool_call_id"]
    
    to_date = datetime.datetime.now(datetime.timezone.utc)
    fr_date = to_date - datetime.timedelta(days=history_length_in_days)
    
    to = int(to_date.timestamp())
    fr = int(fr_date.timestamp())    

    # Separate the base URL and path
    coingecko_api_key = os.environ.get("COINGECKO_API_KEY")
    base_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    qparams  = {'from': fr, 'to': to, 'precision': 'full', 'vs_currency': 'usd'}
    headers  = {"accept": "application/json", "x-cg-demo-api-key": coingecko_api_key }

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=qparams, headers=headers)
        result_content = json.dumps(response.json())
        print('[TOOL get_crypto_prices]', result_content[:15])    
        tool_message = ToolMessage(content=result_content, tool_call_id=tool_call_id)
    
    return {'messages': [tool_message]}

    
#==============================================
# LLM agent
#==============================================

    
async def chatbot(state: State):
    """
    The LLM node definition.
    """     
    tools = [ 
        is_odd_tool,
        get_crypto_prices_tool
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
    
    'is_odd_tool': lambda t: Send('is_odd', {
        'number': t['args']['number'], 
        'tool_call_id': t['id']
    }),
    
    'get_crypto_prices_tool': lambda t: Send('get_crypto_prices', {
        'coin_id': t['args']['coin_id'],
        'history_length_in_days': t['args']['history_length_in_days'],
        'tool_call_id': t['id']        
    })

}


def route_tool(state: State) -> Literal["is_odd", "__end__"]:
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
workflow.add_node("is_odd", is_odd_streamed)
workflow.add_node("get_crypto_prices", get_crypto_prices_streamed)

workflow.add_edge(lgraph.START, "chatbot")
workflow.add_conditional_edges("chatbot", route_tool)
workflow.add_edge("is_odd", "chatbot")
workflow.add_edge("get_crypto_prices", "chatbot")
workflow.add_edge("chatbot", lgraph.END)

memory = MemorySaver()
graph = workflow.compile(checkpointer=memory)
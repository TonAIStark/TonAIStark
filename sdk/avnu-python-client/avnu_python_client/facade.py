
import json
from avnu_python_client.api_client import ApiClient
from avnu_python_client.configuration import Configuration
from avnu_python_client.api.starknet_api import StarknetApi
from avnu_python_client.api.swap_api import SwapApi
from avnu_python_client.models.token_dto import TokenDto
from avnu_python_client.models.quote import Quote
from avnu_python_client.models.build_swap_response import BuildSwapResponse

from typing import List

configuration = Configuration(
    host = "https://sepolia.api.avnu.fi" 
)
apiClient = ApiClient(configuration)

"""Returns the tokens"""
def get_tokens(page: int = 0, size: int = 10, sort: List[str] = ["string"], tag = ["AVNU"]) -> List[TokenDto]:
    """
    Returns the tokens supported by AVNU.
    :return: List of TokenDto
    """
    # Create an instance of the API client
    apiClient = ApiClient(configuration)
    
    # Create an instance of the StarknetApi
    starknet_api = StarknetApi(apiClient)
    
    # Call the get_tokens method and return the result
    return starknet_api.get_tokens({
        "page": page,
        "size": size,
        "sort": sort
    }, tag=tag).content
    
"""Return the quotes"""
def get_quotes(sellTokenAddress: str, buyTokenAddress: str, sellAmount: str) -> List[Quote]:
    """
    Returns the quotes for the given tokens.
    :param sellTokenAddress: The address of the token to sell.
    :param buyTokenAddress: The address of the token to buy.
    :param amount: The amount of tokens to sell (in hex string).
    :return: The quotes for the given tokens.
    """
    # Create an instance of the API client
    apiClient = ApiClient(configuration)
    
    # Create an instance of the SwapApi
    swap_api = SwapApi(apiClient)
    
    # Call the get_quotes method and return the result
    try:
        response = swap_api.get_quotes(
            sell_token_address=sellTokenAddress,
            buy_token_address=buyTokenAddress,
            sell_amount=sellAmount)
        json_str = response.read().decode("utf-8")
        
        print(json_str)
        # Parse the JSON response
        quotes_data = json.loads(json_str)
        return quotes_data
    except Exception as e:
        print(f"Error: {e}")
        return []

tokens: List[TokenDto] = get_tokens()
quote: List[Quote] = get_quotes(
    sellTokenAddress="0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    buyTokenAddress="0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    sellAmount="0xDE0B6B3A7640000")

print(quote)
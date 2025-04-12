from avnu_python_client.api_client import ApiClient
from avnu_python_client.configuration import Configuration
from avnu_python_client.api.starknet_api import StarknetApi
from avnu_python_client.models.token_dto import TokenDto

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
    }, tag=tag)
    
"""
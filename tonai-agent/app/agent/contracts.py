from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.contract import Contract


import asyncio

node_url = "https://free-rpc.nethermind.io/sepolia-juno"
client = FullNodeClient(node_url=node_url)

account = Account(
    client=client,
    address="0x006Bcdf9e4A67af8D194d0BFd2778e23CdB4593604cca46F9afCc0dae0bcfe1b",
    key_pair=KeyPair.from_private_key(key="0x01320b6f4ebc46fa496abe15634d333fe03e341d82cd9f0e206bbcce00bb584d"),
    chain=StarknetChainId.SEPOLIA,
)

# 0x04c5772d1914fe6ce891b64eb35bf3522aeae1315647314aac58b01137607f3f ETH L2

abi = [
    {
        "inputs": [
            {"name": "sell_token_address", "type": "felt"},
            {"name": "sell_token_amount", "type": "felt"},
            {"name": "sell_token_max_amount", "type": "felt"},
            {"name": "buy_token_address", "type": "felt"},
            {"name": "buy_token_amount", "type": "felt"},
            {"name": "beneficiary", "type": "felt"},
            {"name": "routes", "type": "Route[]"}
        ],
        "name": "swap_exact_token_to",
        "outputs": [{"name": "success", "type": "felt"}],
        "type": "function"
    }
]



contract = Contract(address="0x02c56e8b00dbe2a71e57472685378fc8988bba947e9a99b26a00fade2b4fe7c2", abi=abi, provider=account, cairo_version=0)

"""
{"name": "sell_token_address", "type": "felt"},
{"name": "sell_token_amount", "type": "Uint256"},
{"name": "sell_token_max_amount", "type": "Uint256"},
{"name": "buy_token_address", "type": "felt"},
{"name": "buy_token_amount", "type": "Uint256"},
{"name": "beneficiary", "type": "felt"},
{"name": "routes", "type": "felt"}
"""


async def invoke_and_wait(contract):
    invocation = contract.functions["swap_exact_token_to"].invoke(
        "0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
        1000000000000000000,
        1000000000000000000,
        "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
        1000000000000000000,
        "0x006Bcdf9e4A67af8D194d0BFd2778e23CdB4593604cca46F9afCc0dae0bcfe1b",
        [
        {
          name: 'AMM2',
          address: '0x975910cd99bc56bd289eaaa5cee6cd557f0ddafdb2ce6ebea15b158eb2c662',
          percent: 1,
          sellTokenAddress: '0x3e85bfbb8e2a42b7bead9e88e9a1b19dbccf661471061807292120462396ec9',
          buyTokenAddress: '0x2e2faab2cad8ecdde5e991798673ddcc08983b872304a66e5f99fbb24e14abc',
          routes: [
            {
                    name: 'AMM1',
                    address: '0x975910cd99bc56bd289eaaa5cee6cd557f0ddafdb2ce6ebea15b158eb2c661',
                    percent: 1,
                    sellTokenAddress: '0x2e2faab2cad8ecdde5e991798673ddcc08983b872304a66e5f99fbb24e14abc',
                    buyTokenAddress: '0x72df4dc5b6c4df72e4288857317caf2ce9da166ab8719ab8306516a2fddfff7',
                    routes: [],
                    },
                ],
        },
        ],
    )
    await invocation.wait_for_acceptance()

result = asyncio.run(invoke_and_wait(contract))

print(result)

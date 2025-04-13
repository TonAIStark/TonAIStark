from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.contract import Contract
from starknet_py.net.client_models import ResourceBounds, ResourceBoundsMapping
from starknet_py.hash.selector import get_selector_from_name
from starknet_py.net.client_models import Call
from starknet_py.net.signer.stark_curve_signer import StarkCurveSigner



import asyncio



#TODO move this to a config file
#node_url = "https://rpc.nethermind.io/mainnet-juno/?apikey=0pcMoH4WVEiYt4fmD7DpUCvAdUrXxJv1tBwaqVg9lPvCdOJUXnbFSjTfTttN2hDz"
node_url = "http://localhost:6060/"
client = FullNodeClient(node_url=node_url)
#account = Account(
#    client=client,
#    address="0x0105acDC86841C5e9aD9EBbf668932f4b8568DddBdd2bf49Db4838f062071C04",
#    key_pair=KeyPair.from_private_key("0x03b1f7c508249dda008e5a11f2489515b58cde34698c51ca74d8966fdee12d42"),
#    chain=StarknetChainId.SEPOLIA,
#)

signer = StarkCurveSigner("0x0105acDC86841C5e9aD9EBbf668932f4b8568DddBdd2bf49Db4838f062071C04", KeyPair.from_private_key("0x03b1f7c508249dda008e5a11f2489515b58cde34698c51ca74d8966fdee12d42"), StarknetChainId.SEPOLIA)
account = Account(
    client=client, address="0x0105acDC86841C5e9aD9EBbf668932f4b8568DddBdd2bf49Db4838f062071C04", signer=signer, chain=StarknetChainId.SEPOLIA
)


async def main():
    resource_bounds=ResourceBoundsMapping(
    	l1_gas=ResourceBounds(max_amount=int(1e5), max_price_per_unit=int(1e13)),
        l2_gas=ResourceBounds(max_amount=int(1e10), max_price_per_unit=int(1e17)),
        l1_data_gas=ResourceBounds(
            max_amount=int(1e5), max_price_per_unit=int(1e13)
        ),   
    )
    
    
    json_input = {
  "chainId": "0x534e5f5345504f4c4941",
  "contractAddress": "0x2c56e8b00dbe2a71e57472685378fc8988bba947e9a99b26a00fade2b4fe7c2",
  "entrypoint": "multi_route_swap",
  "calldata": [
    "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    "0x8ac7230489e80000",
    "0x0",
    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    "0xe84a61acbc05f",
    "0x0",
    "0xdcad0ffdb29f3",
    "0x0",
    "0x6bcdf9e4a67af8d194d0bfd2778e23cdb4593604cca46f9afcc0dae0bcfe1b",
    "0x0",
    "0x0",
    "0x3",
    "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
    "0x180f25810",
    "0x6",
    "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    "0x20c49ba5e353f80000000000000000",
    "0x3e8",
    "0x0",
    "0x244ac2d3bad981346909982badd920",
    "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
    "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
    "0xe8d4a51000",
    "0x6",
    "0x4718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
    "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
    "0x20c49ba5e353f80000000000000000",
    "0x3e8",
    "0x0",
    "0x76f40538a1d96f3ab632666faf",
    "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    "0x444a09d96389aa7148f1aada508e30b71299ffe650d9c97fdaae38cb9a23384",
    "0xe8d4a51000",
    "0x6",
    "0x49d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
    "0x53b40a647cedfca6ca84f542a0fe36736031905a9639a7f19a3c1e66bfd5080",
    "0x20c49ba5e353f80000000000000000",
    "0x3e8",
    "0x0",
    "0xd2814d35653ca3d8f72db6de3"
  ]
}
    call_obj = Call(to_addr=json_input["contractAddress"],
		selector=get_selector_from_name(json_input["entrypoint"]),
		calldata=json_input["calldata"],
	)
	
    resp = await account.execute_v3(
		calls=call_obj,
	)
    await account.client.wait_for_tx(resp.transaction_hash)
	

asyncio.run(main())
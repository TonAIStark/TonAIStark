avnu_abi = [
    {
        "inputs": [
            {"name": "owner", "type": "felt"},
            {"name": "fee_recipient", "type": "felt"},
            {"name": "fees_bps_0", "type": "felt"},
            {"name": "fees_bps_1", "type": "felt"},
            {"name": "swap_exact_token_to_fees_bps", "type": "felt"}
        ],
        "name": "initialize",
        "outputs": [],
        "type": "function"
    },
    {
        "inputs": [
            {"name": "exchange_address", "type": "felt"}
        ],
        "name": "get_adapter_class_hash",
        "outputs": [{"name": "class_hash", "type": "felt"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"name": "exchange_address", "type": "felt"},
            {"name": "adapter_class_hash", "type": "felt"}
        ],
        "name": "set_adapter_class_hash",
        "outputs": [{"name": "success", "type": "felt"}],
        "type": "function"
    },
    {
        "inputs": [
            {"name": "sell_token_address", "type": "felt"},
            {"name": "sell_token_amount", "type": "Uint256"},
            {"name": "buy_token_address", "type": "felt"},
            {"name": "buy_token_amount", "type": "Uint256"},
            {"name": "buy_token_min_amount", "type": "Uint256"},
            {"name": "beneficiary", "type": "felt"},
            {"name": "integrator_fee_amount_bps", "type": "felt"},
            {"name": "integrator_fee_recipient", "type": "felt"},
            {"name": "routes", "type": "Route[]"}
        ],
        "name": "multi_route_swap",
        "outputs": [{"name": "success", "type": "felt"}],
        "type": "function"
    },
    {
        "inputs": [
            {"name": "sell_token_address", "type": "felt"},
            {"name": "sell_token_amount", "type": "Uint256"},
            {"name": "sell_token_max_amount", "type": "Uint256"},
            {"name": "buy_token_address", "type": "felt"},
            {"name": "buy_token_amount", "type": "Uint256"},
            {"name": "beneficiary", "type": "felt"},
            {"name": "routes", "type": "Route[]"}
        ],
        "name": "swap_exact_token_to",
        "outputs": [{"name": "success", "type": "felt"}],
        "type": "function"
    },
    {
        "inputs": [
            {"name": "taker_address", "type": "felt"},
            {"name": "sell_address", "type": "felt"},
            {"name": "sell_amount", "type": "Uint256"},
            {"name": "buy_address", "type": "felt"},
            {"name": "buy_amount", "type": "Uint256"},
            {"name": "beneficiary", "type": "felt"}
        ],
        "name": "Swap",
        "type": "event"
    }
]

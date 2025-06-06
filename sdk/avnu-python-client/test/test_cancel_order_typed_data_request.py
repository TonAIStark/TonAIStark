# coding: utf-8

"""
    AVNU API

    REST API documentation for accessing liquidity on Layer 2.  AVNU is a decentralized exchange protocol enabling the fastest and the most efficient operations in DeFi for Layer 2 with better pricing, zero slippage, MEV-protection and gasless trading.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avnu_python_client.models.cancel_order_typed_data_request import CancelOrderTypedDataRequest

class TestCancelOrderTypedDataRequest(unittest.TestCase):
    """CancelOrderTypedDataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CancelOrderTypedDataRequest:
        """Test CancelOrderTypedDataRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CancelOrderTypedDataRequest`
        """
        model = CancelOrderTypedDataRequest()
        if include_optional:
            return CancelOrderTypedDataRequest(
                trader_address = '',
                gas_token_address = '0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8',
                max_gas_token_amount = ''
            )
        else:
            return CancelOrderTypedDataRequest(
                trader_address = '',
                gas_token_address = '0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8',
        )
        """

    def testCancelOrderTypedDataRequest(self):
        """Test CancelOrderTypedDataRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

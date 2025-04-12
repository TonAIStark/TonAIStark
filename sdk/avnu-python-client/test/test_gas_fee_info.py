# coding: utf-8

"""
    AVNU API

    REST API documentation for accessing liquidity on Layer 2.  AVNU is a decentralized exchange protocol enabling the fastest and the most efficient operations in DeFi for Layer 2 with better pricing, zero slippage, MEV-protection and gasless trading.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avnu_python_client.models.gas_fee_info import GasFeeInfo

class TestGasFeeInfo(unittest.TestCase):
    """GasFeeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GasFeeInfo:
        """Test GasFeeInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GasFeeInfo`
        """
        model = GasFeeInfo()
        if include_optional:
            return GasFeeInfo(
                gas_fee_amount = '',
                gas_fee_amount_usd = 1.337,
                gas_fee_token_address = ''
            )
        else:
            return GasFeeInfo(
        )
        """

    def testGasFeeInfo(self):
        """Test GasFeeInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

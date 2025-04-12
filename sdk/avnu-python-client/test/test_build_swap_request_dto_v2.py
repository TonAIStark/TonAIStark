# coding: utf-8

"""
    AVNU API

    REST API documentation for accessing liquidity on Layer 2.  AVNU is a decentralized exchange protocol enabling the fastest and the most efficient operations in DeFi for Layer 2 with better pricing, zero slippage, MEV-protection and gasless trading.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avnu_python_client.models.build_swap_request_dto_v2 import BuildSwapRequestDtoV2

class TestBuildSwapRequestDtoV2(unittest.TestCase):
    """BuildSwapRequestDtoV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuildSwapRequestDtoV2:
        """Test BuildSwapRequestDtoV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuildSwapRequestDtoV2`
        """
        model = BuildSwapRequestDtoV2()
        if include_optional:
            return BuildSwapRequestDtoV2(
                quote_id = '',
                taker_address = '0x052D8E9778D026588a51595E30B0F45609B4F771EecF0E335CdeFeD1d84a9D89',
                slippage = 0.05,
                include_approve = True
            )
        else:
            return BuildSwapRequestDtoV2(
                quote_id = '',
                slippage = 0.05,
                include_approve = True,
        )
        """

    def testBuildSwapRequestDtoV2(self):
        """Test BuildSwapRequestDtoV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

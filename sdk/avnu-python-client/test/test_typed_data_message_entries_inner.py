# coding: utf-8

"""
    AVNU API

    REST API documentation for accessing liquidity on Layer 2.  AVNU is a decentralized exchange protocol enabling the fastest and the most efficient operations in DeFi for Layer 2 with better pricing, zero slippage, MEV-protection and gasless trading.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from avnu_python_client.models.typed_data_message_entries_inner import TypedDataMessageEntriesInner

class TestTypedDataMessageEntriesInner(unittest.TestCase):
    """TypedDataMessageEntriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TypedDataMessageEntriesInner:
        """Test TypedDataMessageEntriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TypedDataMessageEntriesInner`
        """
        model = TypedDataMessageEntriesInner()
        if include_optional:
            return TypedDataMessageEntriesInner(
                value = avnu_python_client.models.json_element.JsonElement(),
                key = ''
            )
        else:
            return TypedDataMessageEntriesInner(
        )
        """

    def testTypedDataMessageEntriesInner(self):
        """Test TypedDataMessageEntriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

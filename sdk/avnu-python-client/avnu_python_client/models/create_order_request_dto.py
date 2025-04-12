# coding: utf-8

"""
    AVNU API

    REST API documentation for accessing liquidity on Layer 2.  AVNU is a decentralized exchange protocol enabling the fastest and the most efficient operations in DeFi for Layer 2 with better pricing, zero slippage, MEV-protection and gasless trading.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from avnu_python_client.models.create_order_request_dto_frequency import CreateOrderRequestDtoFrequency
from avnu_python_client.models.pricing_strategy import PricingStrategy
from typing import Optional, Set
from typing_extensions import Self

class CreateOrderRequestDto(BaseModel):
    """
    CreateOrderRequestDto
    """ # noqa: E501
    trader_address: StrictStr = Field(description="The trader address (hex format)", alias="traderAddress")
    sell_token_address: StrictStr = Field(description="The sell token address (hex format)", alias="sellTokenAddress")
    sell_amount: StrictStr = Field(description="The total amount you want to invest (hex format)", alias="sellAmount")
    sell_amount_per_cycle: StrictStr = Field(description="The amount that will be sold at each iteration (hex format)", alias="sellAmountPerCycle")
    buy_token_address: StrictStr = Field(description="The sell token address (hex format)", alias="buyTokenAddress")
    frequency: CreateOrderRequestDtoFrequency
    start_date: Optional[datetime] = Field(default=None, description="You can choose when you want the order to start. By default, it starts immediately", alias="startDate")
    pricing_strategy: PricingStrategy = Field(alias="pricingStrategy")
    __properties: ClassVar[List[str]] = ["traderAddress", "sellTokenAddress", "sellAmount", "sellAmountPerCycle", "buyTokenAddress", "frequency", "startDate", "pricingStrategy"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOrderRequestDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of frequency
        if self.frequency:
            _dict['frequency'] = self.frequency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing_strategy
        if self.pricing_strategy:
            _dict['pricingStrategy'] = self.pricing_strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "traderAddress": obj.get("traderAddress"),
            "sellTokenAddress": obj.get("sellTokenAddress"),
            "sellAmount": obj.get("sellAmount"),
            "sellAmountPerCycle": obj.get("sellAmountPerCycle"),
            "buyTokenAddress": obj.get("buyTokenAddress"),
            "frequency": CreateOrderRequestDtoFrequency.from_dict(obj["frequency"]) if obj.get("frequency") is not None else None,
            "startDate": obj.get("startDate"),
            "pricingStrategy": PricingStrategy.from_dict(obj["pricingStrategy"]) if obj.get("pricingStrategy") is not None else None
        })
        return _obj



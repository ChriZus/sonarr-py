# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from sonarr.models.language import Language
from sonarr.models.language_profile_item_resource import LanguageProfileItemResource

class LanguageProfileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    upgrade_allowed: Optional[bool]
    cutoff: Optional[Language]
    languages: Optional[List]
    __properties = ["id", "name", "upgradeAllowed", "cutoff", "languages"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LanguageProfileResource:
        """Create an instance of LanguageProfileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cutoff
        if self.cutoff:
            _dict['cutoff'] = self.cutoff.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LanguageProfileResource:
        """Create an instance of LanguageProfileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return LanguageProfileResource.parse_obj(obj)

        _obj = LanguageProfileResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "upgrade_allowed": obj.get("upgradeAllowed"),
            "cutoff": Language.from_dict(obj.get("cutoff")) if obj.get("cutoff") is not None else None,
            "languages": [LanguageProfileItemResource.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None
        })
        return _obj


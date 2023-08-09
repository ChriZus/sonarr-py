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


from typing import Optional
from pydantic import BaseModel

class QueueStatusResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    total_count: Optional[int]
    count: Optional[int]
    unknown_count: Optional[int]
    errors: Optional[bool]
    warnings: Optional[bool]
    unknown_errors: Optional[bool]
    unknown_warnings: Optional[bool]
    __properties = ["id", "totalCount", "count", "unknownCount", "errors", "warnings", "unknownErrors", "unknownWarnings"]

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
    def from_json(cls, json_str: str) -> QueueStatusResource:
        """Create an instance of QueueStatusResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueueStatusResource:
        """Create an instance of QueueStatusResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QueueStatusResource.parse_obj(obj)

        _obj = QueueStatusResource.parse_obj({
            "id": obj.get("id"),
            "total_count": obj.get("totalCount"),
            "count": obj.get("count"),
            "unknown_count": obj.get("unknownCount"),
            "errors": obj.get("errors"),
            "warnings": obj.get("warnings"),
            "unknown_errors": obj.get("unknownErrors"),
            "unknown_warnings": obj.get("unknownWarnings")
        })
        return _obj


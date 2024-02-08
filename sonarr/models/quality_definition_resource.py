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



from pydantic import BaseModel
from sonarr.models.quality import Quality

class QualityDefinitionResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    quality: Optional[Quality]
    title: Optional[str]
    weight: Optional[int]
    min_size: Optional[float]
    max_size: Optional[float]
    preferred_size: Optional[float]
    __properties = ["id", "quality", "title", "weight", "minSize", "maxSize", "preferredSize"]

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
    def from_json(cls, json_str: str) -> QualityDefinitionResource:
        """Create an instance of QualityDefinitionResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if min_size (nullable) is None
        if self.min_size is None:
            _dict['minSize'] = None

        # set to None if max_size (nullable) is None
        if self.max_size is None:
            _dict['maxSize'] = None

        # set to None if preferred_size (nullable) is None
        if self.preferred_size is None:
            _dict['preferredSize'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualityDefinitionResource:
        """Create an instance of QualityDefinitionResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QualityDefinitionResource.parse_obj(obj)

        _obj = QualityDefinitionResource.parse_obj({
            "id": obj.get("id"),
            "quality": Quality.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "title": obj.get("title"),
            "weight": obj.get("weight"),
            "min_size": obj.get("minSize"),
            "max_size": obj.get("maxSize"),
            "preferred_size": obj.get("preferredSize")
        })
        return _obj


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
from sonarr.models.apply_tags import ApplyTags

class IndexerBulkResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    ids: Optional[List]
    tags: Optional[List]
    apply_tags: Optional[ApplyTags]
    enable_rss: Optional[bool]
    enable_automatic_search: Optional[bool]
    enable_interactive_search: Optional[bool]
    priority: Optional[int]
    __properties = ["ids", "tags", "applyTags", "enableRss", "enableAutomaticSearch", "enableInteractiveSearch", "priority"]

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
    def from_json(cls, json_str: str) -> IndexerBulkResource:
        """Create an instance of IndexerBulkResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ids (nullable) is None
        if self.ids is None:
            _dict['ids'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if enable_rss (nullable) is None
        if self.enable_rss is None:
            _dict['enableRss'] = None

        # set to None if enable_automatic_search (nullable) is None
        if self.enable_automatic_search is None:
            _dict['enableAutomaticSearch'] = None

        # set to None if enable_interactive_search (nullable) is None
        if self.enable_interactive_search is None:
            _dict['enableInteractiveSearch'] = None

        # set to None if priority (nullable) is None
        if self.priority is None:
            _dict['priority'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IndexerBulkResource:
        """Create an instance of IndexerBulkResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IndexerBulkResource.parse_obj(obj)

        _obj = IndexerBulkResource.parse_obj({
            "ids": obj.get("ids"),
            "tags": obj.get("tags"),
            "apply_tags": obj.get("applyTags"),
            "enable_rss": obj.get("enableRss"),
            "enable_automatic_search": obj.get("enableAutomaticSearch"),
            "enable_interactive_search": obj.get("enableInteractiveSearch"),
            "priority": obj.get("priority")
        })
        return _obj


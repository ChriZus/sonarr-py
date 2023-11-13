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
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.episode_resource import EpisodeResource
from sonarr.models.language import Language
from sonarr.models.parsed_episode_info import ParsedEpisodeInfo
from sonarr.models.series_resource import SeriesResource

class ParseResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    title: Optional[str]
    parsed_episode_info: Optional[ParsedEpisodeInfo]
    series: Optional[SeriesResource]
    episodes: Optional[List]
    languages: Optional[List]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    __properties = ["id", "title", "parsedEpisodeInfo", "series", "episodes", "languages", "customFormats", "customFormatScore"]

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
    def from_json(cls, json_str: str) -> ParseResource:
        """Create an instance of ParseResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parsed_episode_info
        if self.parsed_episode_info:
            _dict['parsedEpisodeInfo'] = self.parsed_episode_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in episodes (list)
        _items = []
        if self.episodes:
            for _item in self.episodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['episodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if episodes (nullable) is None
        if self.episodes is None:
            _dict['episodes'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParseResource:
        """Create an instance of ParseResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParseResource.parse_obj(obj)

        _obj = ParseResource.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "parsed_episode_info": ParsedEpisodeInfo.from_dict(obj.get("parsedEpisodeInfo")) if obj.get("parsedEpisodeInfo") is not None else None,
            "series": SeriesResource.from_dict(obj.get("series")) if obj.get("series") is not None else None,
            "episodes": [EpisodeResource.from_dict(_item) for _item in obj.get("episodes")] if obj.get("episodes") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore")
        })
        return _obj


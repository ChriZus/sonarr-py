# coding: utf-8

"""
    Sonarr

    Sonarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel
from sonarr.models.episode_resource import EpisodeResource
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.rejection import Rejection

class ManualImportReprocessResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    path: Optional[str]
    series_id: Optional[int]
    season_number: Optional[int]
    episodes: Optional[List]
    episode_ids: Optional[List]
    quality: Optional[QualityModel]
    languages: Optional[List]
    release_group: Optional[str]
    download_id: Optional[str]
    rejections: Optional[List]
    __properties = ["id", "path", "seriesId", "seasonNumber", "episodes", "episodeIds", "quality", "languages", "releaseGroup", "downloadId", "rejections"]

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
    def from_json(cls, json_str: str) -> ManualImportReprocessResource:
        """Create an instance of ManualImportReprocessResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in episodes (list)
        _items = []
        if self.episodes:
            for _item in self.episodes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['episodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejections (list)
        _items = []
        if self.rejections:
            for _item in self.rejections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rejections'] = _items
        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if season_number (nullable) is None
        if self.season_number is None:
            _dict['seasonNumber'] = None

        # set to None if episodes (nullable) is None
        if self.episodes is None:
            _dict['episodes'] = None

        # set to None if episode_ids (nullable) is None
        if self.episode_ids is None:
            _dict['episodeIds'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if rejections (nullable) is None
        if self.rejections is None:
            _dict['rejections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualImportReprocessResource:
        """Create an instance of ManualImportReprocessResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ManualImportReprocessResource.parse_obj(obj)

        _obj = ManualImportReprocessResource.parse_obj({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "series_id": obj.get("seriesId"),
            "season_number": obj.get("seasonNumber"),
            "episodes": [EpisodeResource.from_dict(_item) for _item in obj.get("episodes")] if obj.get("episodes") is not None else None,
            "episode_ids": obj.get("episodeIds"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "release_group": obj.get("releaseGroup"),
            "download_id": obj.get("downloadId"),
            "rejections": [Rejection.from_dict(_item) for _item in obj.get("rejections")] if obj.get("rejections") is not None else None
        })
        return _obj


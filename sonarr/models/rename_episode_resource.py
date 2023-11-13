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

class RenameEpisodeResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    series_id: Optional[int]
    season_number: Optional[int]
    episode_numbers: Optional[List]
    episode_file_id: Optional[int]
    existing_path: Optional[str]
    new_path: Optional[str]
    __properties = ["id", "seriesId", "seasonNumber", "episodeNumbers", "episodeFileId", "existingPath", "newPath"]

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
    def from_json(cls, json_str: str) -> RenameEpisodeResource:
        """Create an instance of RenameEpisodeResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if episode_numbers (nullable) is None
        if self.episode_numbers is None:
            _dict['episodeNumbers'] = None

        # set to None if existing_path (nullable) is None
        if self.existing_path is None:
            _dict['existingPath'] = None

        # set to None if new_path (nullable) is None
        if self.new_path is None:
            _dict['newPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RenameEpisodeResource:
        """Create an instance of RenameEpisodeResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RenameEpisodeResource.parse_obj(obj)

        _obj = RenameEpisodeResource.parse_obj({
            "id": obj.get("id"),
            "series_id": obj.get("seriesId"),
            "season_number": obj.get("seasonNumber"),
            "episode_numbers": obj.get("episodeNumbers"),
            "episode_file_id": obj.get("episodeFileId"),
            "existing_path": obj.get("existingPath"),
            "new_path": obj.get("newPath")
        })
        return _obj


# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: v4.0.8.1874
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class SeasonStatisticsResource(BaseModel):
    """
    SeasonStatisticsResource
    """ # noqa: E501
    next_airing: Optional[datetime] = Field(default=None, alias="nextAiring")
    previous_airing: Optional[datetime] = Field(default=None, alias="previousAiring")
    episode_file_count: Optional[StrictInt] = Field(default=None, alias="episodeFileCount")
    episode_count: Optional[StrictInt] = Field(default=None, alias="episodeCount")
    total_episode_count: Optional[StrictInt] = Field(default=None, alias="totalEpisodeCount")
    size_on_disk: Optional[StrictInt] = Field(default=None, alias="sizeOnDisk")
    release_groups: Optional[List[StrictStr]] = Field(default=None, alias="releaseGroups")
    percent_of_episodes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="percentOfEpisodes")
    __properties: ClassVar[List[str]] = ["nextAiring", "previousAiring", "episodeFileCount", "episodeCount", "totalEpisodeCount", "sizeOnDisk", "releaseGroups", "percentOfEpisodes"]

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
        """Create an instance of SeasonStatisticsResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "percent_of_episodes",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if next_airing (nullable) is None
        # and model_fields_set contains the field
        if self.next_airing is None and "next_airing" in self.model_fields_set:
            _dict['nextAiring'] = None

        # set to None if previous_airing (nullable) is None
        # and model_fields_set contains the field
        if self.previous_airing is None and "previous_airing" in self.model_fields_set:
            _dict['previousAiring'] = None

        # set to None if release_groups (nullable) is None
        # and model_fields_set contains the field
        if self.release_groups is None and "release_groups" in self.model_fields_set:
            _dict['releaseGroups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeasonStatisticsResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nextAiring": obj.get("nextAiring"),
            "previousAiring": obj.get("previousAiring"),
            "episodeFileCount": obj.get("episodeFileCount"),
            "episodeCount": obj.get("episodeCount"),
            "totalEpisodeCount": obj.get("totalEpisodeCount"),
            "sizeOnDisk": obj.get("sizeOnDisk"),
            "releaseGroups": obj.get("releaseGroups"),
            "percentOfEpisodes": obj.get("percentOfEpisodes")
        })
        return _obj



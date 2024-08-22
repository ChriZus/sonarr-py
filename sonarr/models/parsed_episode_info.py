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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.release_type import ReleaseType
from sonarr.models.series_title_info import SeriesTitleInfo
from typing import Optional, Set
from typing_extensions import Self

class ParsedEpisodeInfo(BaseModel):
    """
    ParsedEpisodeInfo
    """ # noqa: E501
    release_title: Optional[StrictStr] = Field(default=None, alias="releaseTitle")
    series_title: Optional[StrictStr] = Field(default=None, alias="seriesTitle")
    series_title_info: Optional[SeriesTitleInfo] = Field(default=None, alias="seriesTitleInfo")
    quality: Optional[QualityModel] = None
    season_number: Optional[StrictInt] = Field(default=None, alias="seasonNumber")
    episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="episodeNumbers")
    absolute_episode_numbers: Optional[List[StrictInt]] = Field(default=None, alias="absoluteEpisodeNumbers")
    special_absolute_episode_numbers: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="specialAbsoluteEpisodeNumbers")
    air_date: Optional[StrictStr] = Field(default=None, alias="airDate")
    languages: Optional[List[Language]] = None
    full_season: Optional[StrictBool] = Field(default=None, alias="fullSeason")
    is_partial_season: Optional[StrictBool] = Field(default=None, alias="isPartialSeason")
    is_multi_season: Optional[StrictBool] = Field(default=None, alias="isMultiSeason")
    is_season_extra: Optional[StrictBool] = Field(default=None, alias="isSeasonExtra")
    is_split_episode: Optional[StrictBool] = Field(default=None, alias="isSplitEpisode")
    is_mini_series: Optional[StrictBool] = Field(default=None, alias="isMiniSeries")
    special: Optional[StrictBool] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    release_hash: Optional[StrictStr] = Field(default=None, alias="releaseHash")
    season_part: Optional[StrictInt] = Field(default=None, alias="seasonPart")
    release_tokens: Optional[StrictStr] = Field(default=None, alias="releaseTokens")
    daily_part: Optional[StrictInt] = Field(default=None, alias="dailyPart")
    is_daily: Optional[StrictBool] = Field(default=None, alias="isDaily")
    is_absolute_numbering: Optional[StrictBool] = Field(default=None, alias="isAbsoluteNumbering")
    is_possible_special_episode: Optional[StrictBool] = Field(default=None, alias="isPossibleSpecialEpisode")
    is_possible_scene_season_special: Optional[StrictBool] = Field(default=None, alias="isPossibleSceneSeasonSpecial")
    release_type: Optional[ReleaseType] = Field(default=None, alias="releaseType")
    __properties: ClassVar[List[str]] = ["releaseTitle", "seriesTitle", "seriesTitleInfo", "quality", "seasonNumber", "episodeNumbers", "absoluteEpisodeNumbers", "specialAbsoluteEpisodeNumbers", "airDate", "languages", "fullSeason", "isPartialSeason", "isMultiSeason", "isSeasonExtra", "isSplitEpisode", "isMiniSeries", "special", "releaseGroup", "releaseHash", "seasonPart", "releaseTokens", "dailyPart", "isDaily", "isAbsoluteNumbering", "isPossibleSpecialEpisode", "isPossibleSceneSeasonSpecial", "releaseType"]

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
        """Create an instance of ParsedEpisodeInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_daily",
            "is_absolute_numbering",
            "is_possible_special_episode",
            "is_possible_scene_season_special",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of series_title_info
        if self.series_title_info:
            _dict['seriesTitleInfo'] = self.series_title_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # set to None if release_title (nullable) is None
        # and model_fields_set contains the field
        if self.release_title is None and "release_title" in self.model_fields_set:
            _dict['releaseTitle'] = None

        # set to None if series_title (nullable) is None
        # and model_fields_set contains the field
        if self.series_title is None and "series_title" in self.model_fields_set:
            _dict['seriesTitle'] = None

        # set to None if episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.episode_numbers is None and "episode_numbers" in self.model_fields_set:
            _dict['episodeNumbers'] = None

        # set to None if absolute_episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.absolute_episode_numbers is None and "absolute_episode_numbers" in self.model_fields_set:
            _dict['absoluteEpisodeNumbers'] = None

        # set to None if special_absolute_episode_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.special_absolute_episode_numbers is None and "special_absolute_episode_numbers" in self.model_fields_set:
            _dict['specialAbsoluteEpisodeNumbers'] = None

        # set to None if air_date (nullable) is None
        # and model_fields_set contains the field
        if self.air_date is None and "air_date" in self.model_fields_set:
            _dict['airDate'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        # and model_fields_set contains the field
        if self.release_hash is None and "release_hash" in self.model_fields_set:
            _dict['releaseHash'] = None

        # set to None if release_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.release_tokens is None and "release_tokens" in self.model_fields_set:
            _dict['releaseTokens'] = None

        # set to None if daily_part (nullable) is None
        # and model_fields_set contains the field
        if self.daily_part is None and "daily_part" in self.model_fields_set:
            _dict['dailyPart'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParsedEpisodeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "releaseTitle": obj.get("releaseTitle"),
            "seriesTitle": obj.get("seriesTitle"),
            "seriesTitleInfo": SeriesTitleInfo.from_dict(obj["seriesTitleInfo"]) if obj.get("seriesTitleInfo") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "seasonNumber": obj.get("seasonNumber"),
            "episodeNumbers": obj.get("episodeNumbers"),
            "absoluteEpisodeNumbers": obj.get("absoluteEpisodeNumbers"),
            "specialAbsoluteEpisodeNumbers": obj.get("specialAbsoluteEpisodeNumbers"),
            "airDate": obj.get("airDate"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "fullSeason": obj.get("fullSeason"),
            "isPartialSeason": obj.get("isPartialSeason"),
            "isMultiSeason": obj.get("isMultiSeason"),
            "isSeasonExtra": obj.get("isSeasonExtra"),
            "isSplitEpisode": obj.get("isSplitEpisode"),
            "isMiniSeries": obj.get("isMiniSeries"),
            "special": obj.get("special"),
            "releaseGroup": obj.get("releaseGroup"),
            "releaseHash": obj.get("releaseHash"),
            "seasonPart": obj.get("seasonPart"),
            "releaseTokens": obj.get("releaseTokens"),
            "dailyPart": obj.get("dailyPart"),
            "isDaily": obj.get("isDaily"),
            "isAbsoluteNumbering": obj.get("isAbsoluteNumbering"),
            "isPossibleSpecialEpisode": obj.get("isPossibleSpecialEpisode"),
            "isPossibleSceneSeasonSpecial": obj.get("isPossibleSceneSeasonSpecial"),
            "releaseType": obj.get("releaseType")
        })
        return _obj



# coding: utf-8

"""
    Sonarr

    Sonarr API docs - The v3 API docs apply to both v3 and v4 versions of Sonarr. Some functionality may only be available in v4 of the Sonarr application.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sonarr.models.custom_format_resource import CustomFormatResource
from sonarr.models.download_protocol import DownloadProtocol
from sonarr.models.language import Language
from sonarr.models.quality_model import QualityModel
from sonarr.models.series_resource import SeriesResource
from typing import Optional, Set
from typing_extensions import Self

class BlocklistResource(BaseModel):
    """
    BlocklistResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    series_id: Optional[StrictInt] = Field(default=None, alias="seriesId")
    episode_ids: Optional[List[StrictInt]] = Field(default=None, alias="episodeIds")
    source_title: Optional[StrictStr] = Field(default=None, alias="sourceTitle")
    languages: Optional[List[Language]] = None
    quality: Optional[QualityModel] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    var_date: Optional[datetime] = Field(default=None, alias="date")
    protocol: Optional[DownloadProtocol] = None
    indexer: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    series: Optional[SeriesResource] = None
    __properties: ClassVar[List[str]] = ["id", "seriesId", "episodeIds", "sourceTitle", "languages", "quality", "customFormats", "date", "protocol", "indexer", "message", "series"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BlocklistResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of series
        if self.series:
            _dict['series'] = self.series.to_dict()
        # set to None if episode_ids (nullable) is None
        # and model_fields_set contains the field
        if self.episode_ids is None and "episode_ids" in self.model_fields_set:
            _dict['episodeIds'] = None

        # set to None if source_title (nullable) is None
        # and model_fields_set contains the field
        if self.source_title is None and "source_title" in self.model_fields_set:
            _dict['sourceTitle'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlocklistResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "seriesId": obj.get("seriesId"),
            "episodeIds": obj.get("episodeIds"),
            "sourceTitle": obj.get("sourceTitle"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "date": obj.get("date"),
            "protocol": obj.get("protocol"),
            "indexer": obj.get("indexer"),
            "message": obj.get("message"),
            "series": SeriesResource.from_dict(obj["series"]) if obj.get("series") is not None else None
        })
        return _obj



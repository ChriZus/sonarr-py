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
from sonarr.models.download_protocol import DownloadProtocol

class DelayProfileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    enable_usenet: Optional[bool]
    enable_torrent: Optional[bool]
    preferred_protocol: Optional[DownloadProtocol]
    usenet_delay: Optional[int]
    torrent_delay: Optional[int]
    bypass_if_highest_quality: Optional[bool]
    bypass_if_above_custom_format_score: Optional[bool]
    minimum_custom_format_score: Optional[int]
    order: Optional[int]
    tags: Optional[List]
    __properties = ["id", "enableUsenet", "enableTorrent", "preferredProtocol", "usenetDelay", "torrentDelay", "bypassIfHighestQuality", "bypassIfAboveCustomFormatScore", "minimumCustomFormatScore", "order", "tags"]

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
    def from_json(cls, json_str: str) -> DelayProfileResource:
        """Create an instance of DelayProfileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DelayProfileResource:
        """Create an instance of DelayProfileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DelayProfileResource.parse_obj(obj)

        _obj = DelayProfileResource.parse_obj({
            "id": obj.get("id"),
            "enable_usenet": obj.get("enableUsenet"),
            "enable_torrent": obj.get("enableTorrent"),
            "preferred_protocol": obj.get("preferredProtocol"),
            "usenet_delay": obj.get("usenetDelay"),
            "torrent_delay": obj.get("torrentDelay"),
            "bypass_if_highest_quality": obj.get("bypassIfHighestQuality"),
            "bypass_if_above_custom_format_score": obj.get("bypassIfAboveCustomFormatScore"),
            "minimum_custom_format_score": obj.get("minimumCustomFormatScore"),
            "order": obj.get("order"),
            "tags": obj.get("tags")
        })
        return _obj


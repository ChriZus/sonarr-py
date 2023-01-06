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
from sonarr.models.field import Field
from sonarr.models.provider_message import ProviderMessage

class NotificationResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    fields: Optional[List]
    implementation_name: Optional[str]
    implementation: Optional[str]
    config_contract: Optional[str]
    info_link: Optional[str]
    message: Optional[ProviderMessage]
    tags: Optional[List]
    presets: Optional[List]
    link: Optional[str]
    on_grab: Optional[bool]
    on_download: Optional[bool]
    on_upgrade: Optional[bool]
    on_rename: Optional[bool]
    on_series_delete: Optional[bool]
    on_episode_file_delete: Optional[bool]
    on_episode_file_delete_for_upgrade: Optional[bool]
    on_health_issue: Optional[bool]
    on_application_update: Optional[bool]
    supports_on_grab: Optional[bool]
    supports_on_download: Optional[bool]
    supports_on_upgrade: Optional[bool]
    supports_on_rename: Optional[bool]
    supports_on_series_delete: Optional[bool]
    supports_on_episode_file_delete: Optional[bool]
    supports_on_episode_file_delete_for_upgrade: Optional[bool]
    supports_on_health_issue: Optional[bool]
    supports_on_application_update: Optional[bool]
    include_health_warnings: Optional[bool]
    test_command: Optional[str]
    __properties = ["id", "name", "fields", "implementationName", "implementation", "configContract", "infoLink", "message", "tags", "presets", "link", "onGrab", "onDownload", "onUpgrade", "onRename", "onSeriesDelete", "onEpisodeFileDelete", "onEpisodeFileDeleteForUpgrade", "onHealthIssue", "onApplicationUpdate", "supportsOnGrab", "supportsOnDownload", "supportsOnUpgrade", "supportsOnRename", "supportsOnSeriesDelete", "supportsOnEpisodeFileDelete", "supportsOnEpisodeFileDeleteForUpgrade", "supportsOnHealthIssue", "supportsOnApplicationUpdate", "includeHealthWarnings", "testCommand"]

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
    def from_json(cls, json_str: str) -> NotificationResource:
        """Create an instance of NotificationResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        if self.fields is None:
            _dict['fields'] = None

        # set to None if implementation_name (nullable) is None
        if self.implementation_name is None:
            _dict['implementationName'] = None

        # set to None if implementation (nullable) is None
        if self.implementation is None:
            _dict['implementation'] = None

        # set to None if config_contract (nullable) is None
        if self.config_contract is None:
            _dict['configContract'] = None

        # set to None if info_link (nullable) is None
        if self.info_link is None:
            _dict['infoLink'] = None

        # set to None if tags (nullable) is None
        if self.tags is None:
            _dict['tags'] = None

        # set to None if presets (nullable) is None
        if self.presets is None:
            _dict['presets'] = None

        # set to None if link (nullable) is None
        if self.link is None:
            _dict['link'] = None

        # set to None if test_command (nullable) is None
        if self.test_command is None:
            _dict['testCommand'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationResource:
        """Create an instance of NotificationResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NotificationResource.parse_obj(obj)

        _obj = NotificationResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fields": [Field.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "implementation_name": obj.get("implementationName"),
            "implementation": obj.get("implementation"),
            "config_contract": obj.get("configContract"),
            "info_link": obj.get("infoLink"),
            "message": ProviderMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None,
            "tags": obj.get("tags"),
            "presets": [NotificationResource.from_dict(_item) for _item in obj.get("presets")] if obj.get("presets") is not None else None,
            "link": obj.get("link"),
            "on_grab": obj.get("onGrab"),
            "on_download": obj.get("onDownload"),
            "on_upgrade": obj.get("onUpgrade"),
            "on_rename": obj.get("onRename"),
            "on_series_delete": obj.get("onSeriesDelete"),
            "on_episode_file_delete": obj.get("onEpisodeFileDelete"),
            "on_episode_file_delete_for_upgrade": obj.get("onEpisodeFileDeleteForUpgrade"),
            "on_health_issue": obj.get("onHealthIssue"),
            "on_application_update": obj.get("onApplicationUpdate"),
            "supports_on_grab": obj.get("supportsOnGrab"),
            "supports_on_download": obj.get("supportsOnDownload"),
            "supports_on_upgrade": obj.get("supportsOnUpgrade"),
            "supports_on_rename": obj.get("supportsOnRename"),
            "supports_on_series_delete": obj.get("supportsOnSeriesDelete"),
            "supports_on_episode_file_delete": obj.get("supportsOnEpisodeFileDelete"),
            "supports_on_episode_file_delete_for_upgrade": obj.get("supportsOnEpisodeFileDeleteForUpgrade"),
            "supports_on_health_issue": obj.get("supportsOnHealthIssue"),
            "supports_on_application_update": obj.get("supportsOnApplicationUpdate"),
            "include_health_warnings": obj.get("includeHealthWarnings"),
            "test_command": obj.get("testCommand")
        })
        return _obj


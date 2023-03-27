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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TaskResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    task_name: Optional[str]
    interval: Optional[int]
    last_execution: Optional[datetime]
    last_start_time: Optional[datetime]
    next_execution: Optional[datetime]
    last_duration: Optional[str]
    __properties = ["id", "name", "taskName", "interval", "lastExecution", "lastStartTime", "nextExecution", "lastDuration"]

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
    def from_json(cls, json_str: str) -> TaskResource:
        """Create an instance of TaskResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if task_name (nullable) is None
        if self.task_name is None:
            _dict['taskName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskResource:
        """Create an instance of TaskResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TaskResource.parse_obj(obj)

        _obj = TaskResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "task_name": obj.get("taskName"),
            "interval": obj.get("interval"),
            "last_execution": obj.get("lastExecution"),
            "last_start_time": obj.get("lastStartTime"),
            "next_execution": obj.get("nextExecution"),
            "last_duration": obj.get("lastDuration")
        })
        return _obj


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
from sonarr.models.command_trigger import CommandTrigger

class Command(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    send_updates_to_client: Optional[bool]
    update_scheduled_task: Optional[bool]
    completion_message: Optional[str]
    requires_disk_access: Optional[bool]
    is_exclusive: Optional[bool]
    is_long_running: Optional[bool]
    name: Optional[str]
    last_execution_time: Optional[datetime]
    last_start_time: Optional[datetime]
    trigger: Optional[CommandTrigger]
    suppress_messages: Optional[bool]
    client_user_agent: Optional[str]
    __properties = ["sendUpdatesToClient", "updateScheduledTask", "completionMessage", "requiresDiskAccess", "isExclusive", "isLongRunning", "name", "lastExecutionTime", "lastStartTime", "trigger", "suppressMessages", "clientUserAgent"]

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
    def from_json(cls, json_str: str) -> Command:
        """Create an instance of Command from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "update_scheduled_task",
                            "completion_message",
                            "requires_disk_access",
                            "is_exclusive",
                            "is_long_running",
                            "name",
                          },
                          exclude_none=True)
        # set to None if completion_message (nullable) is None
        if self.completion_message is None:
            _dict['completionMessage'] = None

        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if last_execution_time (nullable) is None
        if self.last_execution_time is None:
            _dict['lastExecutionTime'] = None

        # set to None if last_start_time (nullable) is None
        if self.last_start_time is None:
            _dict['lastStartTime'] = None

        # set to None if client_user_agent (nullable) is None
        if self.client_user_agent is None:
            _dict['clientUserAgent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Command:
        """Create an instance of Command from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Command.parse_obj(obj)

        _obj = Command.parse_obj({
            "send_updates_to_client": obj.get("sendUpdatesToClient"),
            "update_scheduled_task": obj.get("updateScheduledTask"),
            "completion_message": obj.get("completionMessage"),
            "requires_disk_access": obj.get("requiresDiskAccess"),
            "is_exclusive": obj.get("isExclusive"),
            "is_long_running": obj.get("isLongRunning"),
            "name": obj.get("name"),
            "last_execution_time": obj.get("lastExecutionTime"),
            "last_start_time": obj.get("lastStartTime"),
            "trigger": obj.get("trigger"),
            "suppress_messages": obj.get("suppressMessages"),
            "client_user_agent": obj.get("clientUserAgent")
        })
        return _obj


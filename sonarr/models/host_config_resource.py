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
from sonarr.models.authentication_required_type import AuthenticationRequiredType
from sonarr.models.authentication_type import AuthenticationType
from sonarr.models.certificate_validation_type import CertificateValidationType
from sonarr.models.proxy_type import ProxyType
from sonarr.models.update_mechanism import UpdateMechanism

class HostConfigResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    bind_address: Optional[str]
    port: Optional[int]
    ssl_port: Optional[int]
    enable_ssl: Optional[bool]
    launch_browser: Optional[bool]
    authentication_method: Optional[AuthenticationType]
    authentication_required: Optional[AuthenticationRequiredType]
    analytics_enabled: Optional[bool]
    username: Optional[str]
    password: Optional[str]
    password_confirmation: Optional[str]
    log_level: Optional[str]
    console_log_level: Optional[str]
    branch: Optional[str]
    api_key: Optional[str]
    ssl_cert_path: Optional[str]
    ssl_cert_password: Optional[str]
    url_base: Optional[str]
    instance_name: Optional[str]
    application_url: Optional[str]
    update_automatically: Optional[bool]
    update_mechanism: Optional[UpdateMechanism]
    update_script_path: Optional[str]
    proxy_enabled: Optional[bool]
    proxy_type: Optional[ProxyType]
    proxy_hostname: Optional[str]
    proxy_port: Optional[int]
    proxy_username: Optional[str]
    proxy_password: Optional[str]
    proxy_bypass_filter: Optional[str]
    proxy_bypass_local_addresses: Optional[bool]
    certificate_validation: Optional[CertificateValidationType]
    backup_folder: Optional[str]
    backup_interval: Optional[int]
    backup_retention: Optional[int]
    __properties = ["id", "bindAddress", "port", "sslPort", "enableSsl", "launchBrowser", "authenticationMethod", "authenticationRequired", "analyticsEnabled", "username", "password", "passwordConfirmation", "logLevel", "consoleLogLevel", "branch", "apiKey", "sslCertPath", "sslCertPassword", "urlBase", "instanceName", "applicationUrl", "updateAutomatically", "updateMechanism", "updateScriptPath", "proxyEnabled", "proxyType", "proxyHostname", "proxyPort", "proxyUsername", "proxyPassword", "proxyBypassFilter", "proxyBypassLocalAddresses", "certificateValidation", "backupFolder", "backupInterval", "backupRetention"]

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
    def from_json(cls, json_str: str) -> HostConfigResource:
        """Create an instance of HostConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if bind_address (nullable) is None
        if self.bind_address is None:
            _dict['bindAddress'] = None

        # set to None if username (nullable) is None
        if self.username is None:
            _dict['username'] = None

        # set to None if password (nullable) is None
        if self.password is None:
            _dict['password'] = None

        # set to None if password_confirmation (nullable) is None
        if self.password_confirmation is None:
            _dict['passwordConfirmation'] = None

        # set to None if log_level (nullable) is None
        if self.log_level is None:
            _dict['logLevel'] = None

        # set to None if console_log_level (nullable) is None
        if self.console_log_level is None:
            _dict['consoleLogLevel'] = None

        # set to None if branch (nullable) is None
        if self.branch is None:
            _dict['branch'] = None

        # set to None if api_key (nullable) is None
        if self.api_key is None:
            _dict['apiKey'] = None

        # set to None if ssl_cert_path (nullable) is None
        if self.ssl_cert_path is None:
            _dict['sslCertPath'] = None

        # set to None if ssl_cert_password (nullable) is None
        if self.ssl_cert_password is None:
            _dict['sslCertPassword'] = None

        # set to None if url_base (nullable) is None
        if self.url_base is None:
            _dict['urlBase'] = None

        # set to None if instance_name (nullable) is None
        if self.instance_name is None:
            _dict['instanceName'] = None

        # set to None if application_url (nullable) is None
        if self.application_url is None:
            _dict['applicationUrl'] = None

        # set to None if update_script_path (nullable) is None
        if self.update_script_path is None:
            _dict['updateScriptPath'] = None

        # set to None if proxy_hostname (nullable) is None
        if self.proxy_hostname is None:
            _dict['proxyHostname'] = None

        # set to None if proxy_username (nullable) is None
        if self.proxy_username is None:
            _dict['proxyUsername'] = None

        # set to None if proxy_password (nullable) is None
        if self.proxy_password is None:
            _dict['proxyPassword'] = None

        # set to None if proxy_bypass_filter (nullable) is None
        if self.proxy_bypass_filter is None:
            _dict['proxyBypassFilter'] = None

        # set to None if backup_folder (nullable) is None
        if self.backup_folder is None:
            _dict['backupFolder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HostConfigResource:
        """Create an instance of HostConfigResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HostConfigResource.parse_obj(obj)

        _obj = HostConfigResource.parse_obj({
            "id": obj.get("id"),
            "bind_address": obj.get("bindAddress"),
            "port": obj.get("port"),
            "ssl_port": obj.get("sslPort"),
            "enable_ssl": obj.get("enableSsl"),
            "launch_browser": obj.get("launchBrowser"),
            "authentication_method": obj.get("authenticationMethod"),
            "authentication_required": obj.get("authenticationRequired"),
            "analytics_enabled": obj.get("analyticsEnabled"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "password_confirmation": obj.get("passwordConfirmation"),
            "log_level": obj.get("logLevel"),
            "console_log_level": obj.get("consoleLogLevel"),
            "branch": obj.get("branch"),
            "api_key": obj.get("apiKey"),
            "ssl_cert_path": obj.get("sslCertPath"),
            "ssl_cert_password": obj.get("sslCertPassword"),
            "url_base": obj.get("urlBase"),
            "instance_name": obj.get("instanceName"),
            "application_url": obj.get("applicationUrl"),
            "update_automatically": obj.get("updateAutomatically"),
            "update_mechanism": obj.get("updateMechanism"),
            "update_script_path": obj.get("updateScriptPath"),
            "proxy_enabled": obj.get("proxyEnabled"),
            "proxy_type": obj.get("proxyType"),
            "proxy_hostname": obj.get("proxyHostname"),
            "proxy_port": obj.get("proxyPort"),
            "proxy_username": obj.get("proxyUsername"),
            "proxy_password": obj.get("proxyPassword"),
            "proxy_bypass_filter": obj.get("proxyBypassFilter"),
            "proxy_bypass_local_addresses": obj.get("proxyBypassLocalAddresses"),
            "certificate_validation": obj.get("certificateValidation"),
            "backup_folder": obj.get("backupFolder"),
            "backup_interval": obj.get("backupInterval"),
            "backup_retention": obj.get("backupRetention")
        })
        return _obj


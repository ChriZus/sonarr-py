# coding: utf-8

"""
    Sonarr

    Sonarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EpisodeHistoryEventType(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    UNKNOWN = 'unknown'
    GRABBED = 'grabbed'
    SERIES_FOLDER_IMPORTED = 'seriesFolderImported'
    DOWNLOAD_FOLDER_IMPORTED = 'downloadFolderImported'
    DOWNLOAD_FAILED = 'downloadFailed'
    EPISODE_FILE_DELETED = 'episodeFileDeleted'
    EPISODE_FILE_RENAMED = 'episodeFileRenamed'
    DOWNLOAD_IGNORED = 'downloadIgnored'


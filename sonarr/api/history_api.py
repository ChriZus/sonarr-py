# coding: utf-8

"""
    Sonarr

    Sonarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import datetime

from pydantic import StrictBool, StrictInt

from typing import List, Optional

from sonarr.models.episode_history_event_type import EpisodeHistoryEventType
from sonarr.models.history_resource import HistoryResource
from sonarr.models.history_resource_paging_resource import HistoryResourcePagingResource

from sonarr.api_client import ApiClient
from sonarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class HistoryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_history_failed_by_id(self, id : StrictInt, **kwargs) -> None:  # noqa: E501
        """create_history_failed_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_history_failed_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.create_history_failed_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def create_history_failed_by_id_with_http_info(self, id : StrictInt, **kwargs):  # noqa: E501
        """create_history_failed_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_history_failed_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_history_failed_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v3/history/failed/{id}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_history(self, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs) -> HistoryResourcePagingResource:  # noqa: E501
        """get_history  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_history(include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HistoryResourcePagingResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_history_with_http_info(include_series, include_episode, **kwargs)  # noqa: E501

    @validate_arguments
    def get_history_with_http_info(self, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """get_history  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_history_with_http_info(include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(HistoryResourcePagingResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'include_series',
            'include_episode'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_history" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('include_series') is not None:  # noqa: E501
            _query_params.append(('includeSeries', _params['include_series']))
        if _params.get('include_episode') is not None:  # noqa: E501
            _query_params.append(('includeEpisode', _params['include_episode']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {
            '200': "HistoryResourcePagingResource",
        }

        return self.api_client.call_api(
            '/api/v3/history', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_history_series(self, series_id : Optional[StrictInt] = None, season_number : Optional[StrictInt] = None, event_type : Optional[EpisodeHistoryEventType] = None, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs) -> List[HistoryResource]:  # noqa: E501
        """list_history_series  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_history_series(series_id, season_number, event_type, include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param series_id:
        :type series_id: int
        :param season_number:
        :type season_number: int
        :param event_type:
        :type event_type: EpisodeHistoryEventType
        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[HistoryResource]
        """
        kwargs['_return_http_data_only'] = True
        return self.list_history_series_with_http_info(series_id, season_number, event_type, include_series, include_episode, **kwargs)  # noqa: E501

    @validate_arguments
    def list_history_series_with_http_info(self, series_id : Optional[StrictInt] = None, season_number : Optional[StrictInt] = None, event_type : Optional[EpisodeHistoryEventType] = None, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """list_history_series  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_history_series_with_http_info(series_id, season_number, event_type, include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param series_id:
        :type series_id: int
        :param season_number:
        :type season_number: int
        :param event_type:
        :type event_type: EpisodeHistoryEventType
        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[HistoryResource], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'series_id',
            'season_number',
            'event_type',
            'include_series',
            'include_episode'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_history_series" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('series_id') is not None:  # noqa: E501
            _query_params.append(('seriesId', _params['series_id']))
        if _params.get('season_number') is not None:  # noqa: E501
            _query_params.append(('seasonNumber', _params['season_number']))
        if _params.get('event_type') is not None:  # noqa: E501
            _query_params.append(('eventType', _params['event_type']))
        if _params.get('include_series') is not None:  # noqa: E501
            _query_params.append(('includeSeries', _params['include_series']))
        if _params.get('include_episode') is not None:  # noqa: E501
            _query_params.append(('includeEpisode', _params['include_episode']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {
            '200': "List[HistoryResource]",
        }

        return self.api_client.call_api(
            '/api/v3/history/series', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_history_since(self, var_date : Optional[datetime] = None, event_type : Optional[EpisodeHistoryEventType] = None, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs) -> List[HistoryResource]:  # noqa: E501
        """list_history_since  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_history_since(var_date, event_type, include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param var_date:
        :type var_date: datetime
        :param event_type:
        :type event_type: EpisodeHistoryEventType
        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[HistoryResource]
        """
        kwargs['_return_http_data_only'] = True
        return self.list_history_since_with_http_info(var_date, event_type, include_series, include_episode, **kwargs)  # noqa: E501

    @validate_arguments
    def list_history_since_with_http_info(self, var_date : Optional[datetime] = None, event_type : Optional[EpisodeHistoryEventType] = None, include_series : Optional[StrictBool] = None, include_episode : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """list_history_since  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_history_since_with_http_info(var_date, event_type, include_series, include_episode, async_req=True)
        >>> result = thread.get()

        :param var_date:
        :type var_date: datetime
        :param event_type:
        :type event_type: EpisodeHistoryEventType
        :param include_series:
        :type include_series: bool
        :param include_episode:
        :type include_episode: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[HistoryResource], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'var_date',
            'event_type',
            'include_series',
            'include_episode'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_history_since" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('var_date') is not None:  # noqa: E501
            _query_params.append(('date', _params['var_date']))
        if _params.get('event_type') is not None:  # noqa: E501
            _query_params.append(('eventType', _params['event_type']))
        if _params.get('include_series') is not None:  # noqa: E501
            _query_params.append(('includeSeries', _params['include_series']))
        if _params.get('include_episode') is not None:  # noqa: E501
            _query_params.append(('includeEpisode', _params['include_episode']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-Api-Key', 'apikey']  # noqa: E501

        _response_types_map = {
            '200': "List[HistoryResource]",
        }

        return self.api_client.call_api(
            '/api/v3/history/since', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

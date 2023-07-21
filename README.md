# sonarr-py
Sonarr API docs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

[comment]: # (x-release-please-start-version)
- Package version: 0.7.0

[comment]: # (x-release-please-end)
- API version: 3.0.0

- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/devopsarr/sonarr-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/devopsarr/sonarr-py.git`)

Then import the package:
```python
import sonarr
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sonarr
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import sonarr
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'


# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ApiInfoApi(api_client)

    try:
        api_instance.get_api()
    except ApiException as e:
        print("Exception when calling ApiInfoApi->get_api: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8989*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiInfoApi* | [**get_api**](docs/ApiInfoApi.md#get_api) | **GET** /api | 
*AuthenticationApi* | [**create_login**](docs/AuthenticationApi.md#create_login) | **POST** /login | 
*AuthenticationApi* | [**get_logout**](docs/AuthenticationApi.md#get_logout) | **GET** /logout | 
*AutoTaggingApi* | [**create_auto_tagging**](docs/AutoTaggingApi.md#create_auto_tagging) | **POST** /api/v3/autotagging | 
*AutoTaggingApi* | [**delete_auto_tagging**](docs/AutoTaggingApi.md#delete_auto_tagging) | **DELETE** /api/v3/autotagging/{id} | 
*AutoTaggingApi* | [**get_auto_tagging_by_id**](docs/AutoTaggingApi.md#get_auto_tagging_by_id) | **GET** /api/v3/autotagging/{id} | 
*AutoTaggingApi* | [**get_auto_tagging_schema**](docs/AutoTaggingApi.md#get_auto_tagging_schema) | **GET** /api/v3/autotagging/schema | 
*AutoTaggingApi* | [**list_auto_tagging**](docs/AutoTaggingApi.md#list_auto_tagging) | **GET** /api/v3/autotagging | 
*AutoTaggingApi* | [**update_auto_tagging**](docs/AutoTaggingApi.md#update_auto_tagging) | **PUT** /api/v3/autotagging/{id} | 
*BackupApi* | [**create_system_backup_restore_by_id**](docs/BackupApi.md#create_system_backup_restore_by_id) | **POST** /api/v3/system/backup/restore/{id} | 
*BackupApi* | [**create_system_backup_restore_upload**](docs/BackupApi.md#create_system_backup_restore_upload) | **POST** /api/v3/system/backup/restore/upload | 
*BackupApi* | [**delete_system_backup**](docs/BackupApi.md#delete_system_backup) | **DELETE** /api/v3/system/backup/{id} | 
*BackupApi* | [**list_system_backup**](docs/BackupApi.md#list_system_backup) | **GET** /api/v3/system/backup | 
*BlocklistApi* | [**delete_blocklist**](docs/BlocklistApi.md#delete_blocklist) | **DELETE** /api/v3/blocklist/{id} | 
*BlocklistApi* | [**delete_blocklist_bulk**](docs/BlocklistApi.md#delete_blocklist_bulk) | **DELETE** /api/v3/blocklist/bulk | 
*BlocklistApi* | [**get_blocklist**](docs/BlocklistApi.md#get_blocklist) | **GET** /api/v3/blocklist | 
*CalendarApi* | [**get_calendar_by_id**](docs/CalendarApi.md#get_calendar_by_id) | **GET** /api/v3/calendar/{id} | 
*CalendarApi* | [**list_calendar**](docs/CalendarApi.md#list_calendar) | **GET** /api/v3/calendar | 
*CalendarFeedApi* | [**get_feed_v3_calendar_sonarr_ics**](docs/CalendarFeedApi.md#get_feed_v3_calendar_sonarr_ics) | **GET** /feed/v3/calendar/sonarr.ics | 
*CommandApi* | [**create_command**](docs/CommandApi.md#create_command) | **POST** /api/v3/command | 
*CommandApi* | [**delete_command**](docs/CommandApi.md#delete_command) | **DELETE** /api/v3/command/{id} | 
*CommandApi* | [**get_command_by_id**](docs/CommandApi.md#get_command_by_id) | **GET** /api/v3/command/{id} | 
*CommandApi* | [**list_command**](docs/CommandApi.md#list_command) | **GET** /api/v3/command | 
*CustomFilterApi* | [**create_custom_filter**](docs/CustomFilterApi.md#create_custom_filter) | **POST** /api/v3/customfilter | 
*CustomFilterApi* | [**delete_custom_filter**](docs/CustomFilterApi.md#delete_custom_filter) | **DELETE** /api/v3/customfilter/{id} | 
*CustomFilterApi* | [**get_custom_filter_by_id**](docs/CustomFilterApi.md#get_custom_filter_by_id) | **GET** /api/v3/customfilter/{id} | 
*CustomFilterApi* | [**list_custom_filter**](docs/CustomFilterApi.md#list_custom_filter) | **GET** /api/v3/customfilter | 
*CustomFilterApi* | [**update_custom_filter**](docs/CustomFilterApi.md#update_custom_filter) | **PUT** /api/v3/customfilter/{id} | 
*CustomFormatApi* | [**create_custom_format**](docs/CustomFormatApi.md#create_custom_format) | **POST** /api/v3/customformat | 
*CustomFormatApi* | [**delete_custom_format**](docs/CustomFormatApi.md#delete_custom_format) | **DELETE** /api/v3/customformat/{id} | 
*CustomFormatApi* | [**get_custom_format_by_id**](docs/CustomFormatApi.md#get_custom_format_by_id) | **GET** /api/v3/customformat/{id} | 
*CustomFormatApi* | [**list_custom_format**](docs/CustomFormatApi.md#list_custom_format) | **GET** /api/v3/customformat | 
*CustomFormatApi* | [**list_custom_format_schema**](docs/CustomFormatApi.md#list_custom_format_schema) | **GET** /api/v3/customformat/schema | 
*CustomFormatApi* | [**update_custom_format**](docs/CustomFormatApi.md#update_custom_format) | **PUT** /api/v3/customformat/{id} | 
*CutoffApi* | [**get_wanted_cutoff**](docs/CutoffApi.md#get_wanted_cutoff) | **GET** /api/v3/wanted/cutoff | 
*CutoffApi* | [**get_wanted_cutoff_by_id**](docs/CutoffApi.md#get_wanted_cutoff_by_id) | **GET** /api/v3/wanted/cutoff/{id} | 
*DelayProfileApi* | [**create_delay_profile**](docs/DelayProfileApi.md#create_delay_profile) | **POST** /api/v3/delayprofile | 
*DelayProfileApi* | [**delete_delay_profile**](docs/DelayProfileApi.md#delete_delay_profile) | **DELETE** /api/v3/delayprofile/{id} | 
*DelayProfileApi* | [**get_delay_profile_by_id**](docs/DelayProfileApi.md#get_delay_profile_by_id) | **GET** /api/v3/delayprofile/{id} | 
*DelayProfileApi* | [**list_delay_profile**](docs/DelayProfileApi.md#list_delay_profile) | **GET** /api/v3/delayprofile | 
*DelayProfileApi* | [**update_delay_profile**](docs/DelayProfileApi.md#update_delay_profile) | **PUT** /api/v3/delayprofile/{id} | 
*DelayProfileApi* | [**update_delay_profile_reorder**](docs/DelayProfileApi.md#update_delay_profile_reorder) | **PUT** /api/v3/delayprofile/reorder/{id} | 
*DiskSpaceApi* | [**list_disk_space**](docs/DiskSpaceApi.md#list_disk_space) | **GET** /api/v3/diskspace | 
*DownloadClientApi* | [**create_download_client**](docs/DownloadClientApi.md#create_download_client) | **POST** /api/v3/downloadclient | 
*DownloadClientApi* | [**create_download_client_action_by_name**](docs/DownloadClientApi.md#create_download_client_action_by_name) | **POST** /api/v3/downloadclient/action/{name} | 
*DownloadClientApi* | [**delete_download_client**](docs/DownloadClientApi.md#delete_download_client) | **DELETE** /api/v3/downloadclient/{id} | 
*DownloadClientApi* | [**delete_download_client_bulk**](docs/DownloadClientApi.md#delete_download_client_bulk) | **DELETE** /api/v3/downloadclient/bulk | 
*DownloadClientApi* | [**get_download_client_by_id**](docs/DownloadClientApi.md#get_download_client_by_id) | **GET** /api/v3/downloadclient/{id} | 
*DownloadClientApi* | [**list_download_client**](docs/DownloadClientApi.md#list_download_client) | **GET** /api/v3/downloadclient | 
*DownloadClientApi* | [**list_download_client_schema**](docs/DownloadClientApi.md#list_download_client_schema) | **GET** /api/v3/downloadclient/schema | 
*DownloadClientApi* | [**put_download_client_bulk**](docs/DownloadClientApi.md#put_download_client_bulk) | **PUT** /api/v3/downloadclient/bulk | 
*DownloadClientApi* | [**test_download_client**](docs/DownloadClientApi.md#test_download_client) | **POST** /api/v3/downloadclient/test | 
*DownloadClientApi* | [**testall_download_client**](docs/DownloadClientApi.md#testall_download_client) | **POST** /api/v3/downloadclient/testall | 
*DownloadClientApi* | [**update_download_client**](docs/DownloadClientApi.md#update_download_client) | **PUT** /api/v3/downloadclient/{id} | 
*DownloadClientConfigApi* | [**get_download_client_config**](docs/DownloadClientConfigApi.md#get_download_client_config) | **GET** /api/v3/config/downloadclient | 
*DownloadClientConfigApi* | [**get_download_client_config_by_id**](docs/DownloadClientConfigApi.md#get_download_client_config_by_id) | **GET** /api/v3/config/downloadclient/{id} | 
*DownloadClientConfigApi* | [**update_download_client_config**](docs/DownloadClientConfigApi.md#update_download_client_config) | **PUT** /api/v3/config/downloadclient/{id} | 
*EpisodeApi* | [**get_episode_by_id**](docs/EpisodeApi.md#get_episode_by_id) | **GET** /api/v3/episode/{id} | 
*EpisodeApi* | [**list_episode**](docs/EpisodeApi.md#list_episode) | **GET** /api/v3/episode | 
*EpisodeApi* | [**put_episode_monitor**](docs/EpisodeApi.md#put_episode_monitor) | **PUT** /api/v3/episode/monitor | 
*EpisodeApi* | [**update_episode**](docs/EpisodeApi.md#update_episode) | **PUT** /api/v3/episode/{id} | 
*EpisodeFileApi* | [**delete_episode_file**](docs/EpisodeFileApi.md#delete_episode_file) | **DELETE** /api/v3/episodefile/{id} | 
*EpisodeFileApi* | [**delete_episode_file_bulk**](docs/EpisodeFileApi.md#delete_episode_file_bulk) | **DELETE** /api/v3/episodefile/bulk | 
*EpisodeFileApi* | [**get_episode_file_by_id**](docs/EpisodeFileApi.md#get_episode_file_by_id) | **GET** /api/v3/episodefile/{id} | 
*EpisodeFileApi* | [**list_episode_file**](docs/EpisodeFileApi.md#list_episode_file) | **GET** /api/v3/episodefile | 
*EpisodeFileApi* | [**put_episode_file_bulk**](docs/EpisodeFileApi.md#put_episode_file_bulk) | **PUT** /api/v3/episodefile/bulk | 
*EpisodeFileApi* | [**put_episode_file_editor**](docs/EpisodeFileApi.md#put_episode_file_editor) | **PUT** /api/v3/episodefile/editor | 
*EpisodeFileApi* | [**update_episode_file**](docs/EpisodeFileApi.md#update_episode_file) | **PUT** /api/v3/episodefile/{id} | 
*FileSystemApi* | [**get_file_system**](docs/FileSystemApi.md#get_file_system) | **GET** /api/v3/filesystem | 
*FileSystemApi* | [**get_file_system_mediafiles**](docs/FileSystemApi.md#get_file_system_mediafiles) | **GET** /api/v3/filesystem/mediafiles | 
*FileSystemApi* | [**get_file_system_type**](docs/FileSystemApi.md#get_file_system_type) | **GET** /api/v3/filesystem/type | 
*HealthApi* | [**list_health**](docs/HealthApi.md#list_health) | **GET** /api/v3/health | 
*HistoryApi* | [**create_history_failed_by_id**](docs/HistoryApi.md#create_history_failed_by_id) | **POST** /api/v3/history/failed/{id} | 
*HistoryApi* | [**get_history**](docs/HistoryApi.md#get_history) | **GET** /api/v3/history | 
*HistoryApi* | [**list_history_series**](docs/HistoryApi.md#list_history_series) | **GET** /api/v3/history/series | 
*HistoryApi* | [**list_history_since**](docs/HistoryApi.md#list_history_since) | **GET** /api/v3/history/since | 
*HostConfigApi* | [**get_host_config**](docs/HostConfigApi.md#get_host_config) | **GET** /api/v3/config/host | 
*HostConfigApi* | [**get_host_config_by_id**](docs/HostConfigApi.md#get_host_config_by_id) | **GET** /api/v3/config/host/{id} | 
*HostConfigApi* | [**update_host_config**](docs/HostConfigApi.md#update_host_config) | **PUT** /api/v3/config/host/{id} | 
*ImportListApi* | [**create_import_list**](docs/ImportListApi.md#create_import_list) | **POST** /api/v3/importlist | 
*ImportListApi* | [**create_import_list_action_by_name**](docs/ImportListApi.md#create_import_list_action_by_name) | **POST** /api/v3/importlist/action/{name} | 
*ImportListApi* | [**delete_import_list**](docs/ImportListApi.md#delete_import_list) | **DELETE** /api/v3/importlist/{id} | 
*ImportListApi* | [**delete_import_list_bulk**](docs/ImportListApi.md#delete_import_list_bulk) | **DELETE** /api/v3/importlist/bulk | 
*ImportListApi* | [**get_import_list_by_id**](docs/ImportListApi.md#get_import_list_by_id) | **GET** /api/v3/importlist/{id} | 
*ImportListApi* | [**list_import_list**](docs/ImportListApi.md#list_import_list) | **GET** /api/v3/importlist | 
*ImportListApi* | [**list_import_list_schema**](docs/ImportListApi.md#list_import_list_schema) | **GET** /api/v3/importlist/schema | 
*ImportListApi* | [**put_import_list_bulk**](docs/ImportListApi.md#put_import_list_bulk) | **PUT** /api/v3/importlist/bulk | 
*ImportListApi* | [**test_import_list**](docs/ImportListApi.md#test_import_list) | **POST** /api/v3/importlist/test | 
*ImportListApi* | [**testall_import_list**](docs/ImportListApi.md#testall_import_list) | **POST** /api/v3/importlist/testall | 
*ImportListApi* | [**update_import_list**](docs/ImportListApi.md#update_import_list) | **PUT** /api/v3/importlist/{id} | 
*ImportListExclusionApi* | [**create_import_list_exclusion**](docs/ImportListExclusionApi.md#create_import_list_exclusion) | **POST** /api/v3/importlistexclusion | 
*ImportListExclusionApi* | [**delete_import_list_exclusion**](docs/ImportListExclusionApi.md#delete_import_list_exclusion) | **DELETE** /api/v3/importlistexclusion/{id} | 
*ImportListExclusionApi* | [**get_import_list_exclusion_by_id**](docs/ImportListExclusionApi.md#get_import_list_exclusion_by_id) | **GET** /api/v3/importlistexclusion/{id} | 
*ImportListExclusionApi* | [**list_import_list_exclusion**](docs/ImportListExclusionApi.md#list_import_list_exclusion) | **GET** /api/v3/importlistexclusion | 
*ImportListExclusionApi* | [**update_import_list_exclusion**](docs/ImportListExclusionApi.md#update_import_list_exclusion) | **PUT** /api/v3/importlistexclusion/{id} | 
*IndexerApi* | [**create_indexer**](docs/IndexerApi.md#create_indexer) | **POST** /api/v3/indexer | 
*IndexerApi* | [**create_indexer_action_by_name**](docs/IndexerApi.md#create_indexer_action_by_name) | **POST** /api/v3/indexer/action/{name} | 
*IndexerApi* | [**delete_indexer**](docs/IndexerApi.md#delete_indexer) | **DELETE** /api/v3/indexer/{id} | 
*IndexerApi* | [**delete_indexer_bulk**](docs/IndexerApi.md#delete_indexer_bulk) | **DELETE** /api/v3/indexer/bulk | 
*IndexerApi* | [**get_indexer_by_id**](docs/IndexerApi.md#get_indexer_by_id) | **GET** /api/v3/indexer/{id} | 
*IndexerApi* | [**list_indexer**](docs/IndexerApi.md#list_indexer) | **GET** /api/v3/indexer | 
*IndexerApi* | [**list_indexer_schema**](docs/IndexerApi.md#list_indexer_schema) | **GET** /api/v3/indexer/schema | 
*IndexerApi* | [**put_indexer_bulk**](docs/IndexerApi.md#put_indexer_bulk) | **PUT** /api/v3/indexer/bulk | 
*IndexerApi* | [**test_indexer**](docs/IndexerApi.md#test_indexer) | **POST** /api/v3/indexer/test | 
*IndexerApi* | [**testall_indexer**](docs/IndexerApi.md#testall_indexer) | **POST** /api/v3/indexer/testall | 
*IndexerApi* | [**update_indexer**](docs/IndexerApi.md#update_indexer) | **PUT** /api/v3/indexer/{id} | 
*IndexerConfigApi* | [**get_indexer_config**](docs/IndexerConfigApi.md#get_indexer_config) | **GET** /api/v3/config/indexer | 
*IndexerConfigApi* | [**get_indexer_config_by_id**](docs/IndexerConfigApi.md#get_indexer_config_by_id) | **GET** /api/v3/config/indexer/{id} | 
*IndexerConfigApi* | [**update_indexer_config**](docs/IndexerConfigApi.md#update_indexer_config) | **PUT** /api/v3/config/indexer/{id} | 
*LanguageApi* | [**get_language_by_id**](docs/LanguageApi.md#get_language_by_id) | **GET** /api/v3/language/{id} | 
*LanguageApi* | [**list_language**](docs/LanguageApi.md#list_language) | **GET** /api/v3/language | 
*LanguageProfileApi* | [**create_language_profile**](docs/LanguageProfileApi.md#create_language_profile) | **POST** /api/v3/languageprofile | 
*LanguageProfileApi* | [**delete_language_profile**](docs/LanguageProfileApi.md#delete_language_profile) | **DELETE** /api/v3/languageprofile/{id} | 
*LanguageProfileApi* | [**get_language_profile_by_id**](docs/LanguageProfileApi.md#get_language_profile_by_id) | **GET** /api/v3/languageprofile/{id} | 
*LanguageProfileApi* | [**list_language_profile**](docs/LanguageProfileApi.md#list_language_profile) | **GET** /api/v3/languageprofile | 
*LanguageProfileApi* | [**update_language_profile**](docs/LanguageProfileApi.md#update_language_profile) | **PUT** /api/v3/languageprofile/{id} | 
*LanguageProfileSchemaApi* | [**get_languageprofile_schema**](docs/LanguageProfileSchemaApi.md#get_languageprofile_schema) | **GET** /api/v3/languageprofile/schema | 
*LocalizationApi* | [**get_localization**](docs/LocalizationApi.md#get_localization) | **GET** /api/v3/localization | 
*LocalizationApi* | [**get_localization_by_id**](docs/LocalizationApi.md#get_localization_by_id) | **GET** /api/v3/localization/{id} | 
*LocalizationApi* | [**get_localization_language**](docs/LocalizationApi.md#get_localization_language) | **GET** /api/v3/localization/language | 
*LogApi* | [**get_log**](docs/LogApi.md#get_log) | **GET** /api/v3/log | 
*LogFileApi* | [**get_log_file_by_filename**](docs/LogFileApi.md#get_log_file_by_filename) | **GET** /api/v3/log/file/{filename} | 
*LogFileApi* | [**list_log_file**](docs/LogFileApi.md#list_log_file) | **GET** /api/v3/log/file | 
*ManualImportApi* | [**create_manual_import**](docs/ManualImportApi.md#create_manual_import) | **POST** /api/v3/manualimport | 
*ManualImportApi* | [**list_manual_import**](docs/ManualImportApi.md#list_manual_import) | **GET** /api/v3/manualimport | 
*MediaCoverApi* | [**get_media_coverseries_id_by_filename**](docs/MediaCoverApi.md#get_media_coverseries_id_by_filename) | **GET** /api/v3/mediacover/{seriesId}/{filename} | 
*MediaManagementConfigApi* | [**get_media_management_config**](docs/MediaManagementConfigApi.md#get_media_management_config) | **GET** /api/v3/config/mediamanagement | 
*MediaManagementConfigApi* | [**get_media_management_config_by_id**](docs/MediaManagementConfigApi.md#get_media_management_config_by_id) | **GET** /api/v3/config/mediamanagement/{id} | 
*MediaManagementConfigApi* | [**update_media_management_config**](docs/MediaManagementConfigApi.md#update_media_management_config) | **PUT** /api/v3/config/mediamanagement/{id} | 
*MetadataApi* | [**create_metadata**](docs/MetadataApi.md#create_metadata) | **POST** /api/v3/metadata | 
*MetadataApi* | [**create_metadata_action_by_name**](docs/MetadataApi.md#create_metadata_action_by_name) | **POST** /api/v3/metadata/action/{name} | 
*MetadataApi* | [**delete_metadata**](docs/MetadataApi.md#delete_metadata) | **DELETE** /api/v3/metadata/{id} | 
*MetadataApi* | [**get_metadata_by_id**](docs/MetadataApi.md#get_metadata_by_id) | **GET** /api/v3/metadata/{id} | 
*MetadataApi* | [**list_metadata**](docs/MetadataApi.md#list_metadata) | **GET** /api/v3/metadata | 
*MetadataApi* | [**list_metadata_schema**](docs/MetadataApi.md#list_metadata_schema) | **GET** /api/v3/metadata/schema | 
*MetadataApi* | [**test_metadata**](docs/MetadataApi.md#test_metadata) | **POST** /api/v3/metadata/test | 
*MetadataApi* | [**testall_metadata**](docs/MetadataApi.md#testall_metadata) | **POST** /api/v3/metadata/testall | 
*MetadataApi* | [**update_metadata**](docs/MetadataApi.md#update_metadata) | **PUT** /api/v3/metadata/{id} | 
*MissingApi* | [**get_wanted_missing**](docs/MissingApi.md#get_wanted_missing) | **GET** /api/v3/wanted/missing | 
*MissingApi* | [**get_wanted_missing_by_id**](docs/MissingApi.md#get_wanted_missing_by_id) | **GET** /api/v3/wanted/missing/{id} | 
*NamingConfigApi* | [**get_naming_config**](docs/NamingConfigApi.md#get_naming_config) | **GET** /api/v3/config/naming | 
*NamingConfigApi* | [**get_naming_config_by_id**](docs/NamingConfigApi.md#get_naming_config_by_id) | **GET** /api/v3/config/naming/{id} | 
*NamingConfigApi* | [**get_naming_config_examples**](docs/NamingConfigApi.md#get_naming_config_examples) | **GET** /api/v3/config/naming/examples | 
*NamingConfigApi* | [**update_naming_config**](docs/NamingConfigApi.md#update_naming_config) | **PUT** /api/v3/config/naming/{id} | 
*NotificationApi* | [**create_notification**](docs/NotificationApi.md#create_notification) | **POST** /api/v3/notification | 
*NotificationApi* | [**create_notification_action_by_name**](docs/NotificationApi.md#create_notification_action_by_name) | **POST** /api/v3/notification/action/{name} | 
*NotificationApi* | [**delete_notification**](docs/NotificationApi.md#delete_notification) | **DELETE** /api/v3/notification/{id} | 
*NotificationApi* | [**get_notification_by_id**](docs/NotificationApi.md#get_notification_by_id) | **GET** /api/v3/notification/{id} | 
*NotificationApi* | [**list_notification**](docs/NotificationApi.md#list_notification) | **GET** /api/v3/notification | 
*NotificationApi* | [**list_notification_schema**](docs/NotificationApi.md#list_notification_schema) | **GET** /api/v3/notification/schema | 
*NotificationApi* | [**test_notification**](docs/NotificationApi.md#test_notification) | **POST** /api/v3/notification/test | 
*NotificationApi* | [**testall_notification**](docs/NotificationApi.md#testall_notification) | **POST** /api/v3/notification/testall | 
*NotificationApi* | [**update_notification**](docs/NotificationApi.md#update_notification) | **PUT** /api/v3/notification/{id} | 
*ParseApi* | [**get_parse**](docs/ParseApi.md#get_parse) | **GET** /api/v3/parse | 
*PingApi* | [**get_ping**](docs/PingApi.md#get_ping) | **GET** /ping | 
*QualityDefinitionApi* | [**get_quality_definition_by_id**](docs/QualityDefinitionApi.md#get_quality_definition_by_id) | **GET** /api/v3/qualitydefinition/{id} | 
*QualityDefinitionApi* | [**list_quality_definition**](docs/QualityDefinitionApi.md#list_quality_definition) | **GET** /api/v3/qualitydefinition | 
*QualityDefinitionApi* | [**put_quality_definition_update**](docs/QualityDefinitionApi.md#put_quality_definition_update) | **PUT** /api/v3/qualitydefinition/update | 
*QualityDefinitionApi* | [**update_quality_definition**](docs/QualityDefinitionApi.md#update_quality_definition) | **PUT** /api/v3/qualitydefinition/{id} | 
*QualityProfileApi* | [**create_quality_profile**](docs/QualityProfileApi.md#create_quality_profile) | **POST** /api/v3/qualityprofile | 
*QualityProfileApi* | [**delete_quality_profile**](docs/QualityProfileApi.md#delete_quality_profile) | **DELETE** /api/v3/qualityprofile/{id} | 
*QualityProfileApi* | [**get_quality_profile_by_id**](docs/QualityProfileApi.md#get_quality_profile_by_id) | **GET** /api/v3/qualityprofile/{id} | 
*QualityProfileApi* | [**list_quality_profile**](docs/QualityProfileApi.md#list_quality_profile) | **GET** /api/v3/qualityprofile | 
*QualityProfileApi* | [**update_quality_profile**](docs/QualityProfileApi.md#update_quality_profile) | **PUT** /api/v3/qualityprofile/{id} | 
*QualityProfileSchemaApi* | [**get_qualityprofile_schema**](docs/QualityProfileSchemaApi.md#get_qualityprofile_schema) | **GET** /api/v3/qualityprofile/schema | 
*QueueApi* | [**delete_queue**](docs/QueueApi.md#delete_queue) | **DELETE** /api/v3/queue/{id} | 
*QueueApi* | [**delete_queue_bulk**](docs/QueueApi.md#delete_queue_bulk) | **DELETE** /api/v3/queue/bulk | 
*QueueApi* | [**get_queue**](docs/QueueApi.md#get_queue) | **GET** /api/v3/queue | 
*QueueActionApi* | [**create_queue_grab_bulk**](docs/QueueActionApi.md#create_queue_grab_bulk) | **POST** /api/v3/queue/grab/bulk | 
*QueueActionApi* | [**create_queue_grab_by_id**](docs/QueueActionApi.md#create_queue_grab_by_id) | **POST** /api/v3/queue/grab/{id} | 
*QueueDetailsApi* | [**list_queue_details**](docs/QueueDetailsApi.md#list_queue_details) | **GET** /api/v3/queue/details | 
*QueueStatusApi* | [**get_queue_status**](docs/QueueStatusApi.md#get_queue_status) | **GET** /api/v3/queue/status | 
*ReleaseApi* | [**create_release**](docs/ReleaseApi.md#create_release) | **POST** /api/v3/release | 
*ReleaseApi* | [**list_release**](docs/ReleaseApi.md#list_release) | **GET** /api/v3/release | 
*ReleaseProfileApi* | [**create_release_profile**](docs/ReleaseProfileApi.md#create_release_profile) | **POST** /api/v3/releaseprofile | 
*ReleaseProfileApi* | [**delete_release_profile**](docs/ReleaseProfileApi.md#delete_release_profile) | **DELETE** /api/v3/releaseprofile/{id} | 
*ReleaseProfileApi* | [**get_release_profile_by_id**](docs/ReleaseProfileApi.md#get_release_profile_by_id) | **GET** /api/v3/releaseprofile/{id} | 
*ReleaseProfileApi* | [**list_release_profile**](docs/ReleaseProfileApi.md#list_release_profile) | **GET** /api/v3/releaseprofile | 
*ReleaseProfileApi* | [**update_release_profile**](docs/ReleaseProfileApi.md#update_release_profile) | **PUT** /api/v3/releaseprofile/{id} | 
*ReleasePushApi* | [**create_release_push**](docs/ReleasePushApi.md#create_release_push) | **POST** /api/v3/release/push | 
*RemotePathMappingApi* | [**create_remote_path_mapping**](docs/RemotePathMappingApi.md#create_remote_path_mapping) | **POST** /api/v3/remotepathmapping | 
*RemotePathMappingApi* | [**delete_remote_path_mapping**](docs/RemotePathMappingApi.md#delete_remote_path_mapping) | **DELETE** /api/v3/remotepathmapping/{id} | 
*RemotePathMappingApi* | [**get_remote_path_mapping_by_id**](docs/RemotePathMappingApi.md#get_remote_path_mapping_by_id) | **GET** /api/v3/remotepathmapping/{id} | 
*RemotePathMappingApi* | [**list_remote_path_mapping**](docs/RemotePathMappingApi.md#list_remote_path_mapping) | **GET** /api/v3/remotepathmapping | 
*RemotePathMappingApi* | [**update_remote_path_mapping**](docs/RemotePathMappingApi.md#update_remote_path_mapping) | **PUT** /api/v3/remotepathmapping/{id} | 
*RenameEpisodeApi* | [**list_rename**](docs/RenameEpisodeApi.md#list_rename) | **GET** /api/v3/rename | 
*RootFolderApi* | [**create_root_folder**](docs/RootFolderApi.md#create_root_folder) | **POST** /api/v3/rootfolder | 
*RootFolderApi* | [**delete_root_folder**](docs/RootFolderApi.md#delete_root_folder) | **DELETE** /api/v3/rootfolder/{id} | 
*RootFolderApi* | [**get_root_folder_by_id**](docs/RootFolderApi.md#get_root_folder_by_id) | **GET** /api/v3/rootfolder/{id} | 
*RootFolderApi* | [**list_root_folder**](docs/RootFolderApi.md#list_root_folder) | **GET** /api/v3/rootfolder | 
*SeasonPassApi* | [**create_season_pass**](docs/SeasonPassApi.md#create_season_pass) | **POST** /api/v3/seasonpass | 
*SeriesApi* | [**create_series**](docs/SeriesApi.md#create_series) | **POST** /api/v3/series | 
*SeriesApi* | [**delete_series**](docs/SeriesApi.md#delete_series) | **DELETE** /api/v3/series/{id} | 
*SeriesApi* | [**get_series_by_id**](docs/SeriesApi.md#get_series_by_id) | **GET** /api/v3/series/{id} | 
*SeriesApi* | [**list_series**](docs/SeriesApi.md#list_series) | **GET** /api/v3/series | 
*SeriesApi* | [**update_series**](docs/SeriesApi.md#update_series) | **PUT** /api/v3/series/{id} | 
*SeriesEditorApi* | [**delete_series_editor**](docs/SeriesEditorApi.md#delete_series_editor) | **DELETE** /api/v3/series/editor | 
*SeriesEditorApi* | [**put_series_editor**](docs/SeriesEditorApi.md#put_series_editor) | **PUT** /api/v3/series/editor | 
*SeriesImportApi* | [**create_series_import**](docs/SeriesImportApi.md#create_series_import) | **POST** /api/v3/series/import | 
*SeriesLookupApi* | [**list_series_lookup**](docs/SeriesLookupApi.md#list_series_lookup) | **GET** /api/v3/series/lookup | 
*StaticResourceApi* | [**get**](docs/StaticResourceApi.md#get) | **GET** / | 
*StaticResourceApi* | [**get_by_path**](docs/StaticResourceApi.md#get_by_path) | **GET** /{path} | 
*StaticResourceApi* | [**get_content_by_path**](docs/StaticResourceApi.md#get_content_by_path) | **GET** /content/{path} | 
*StaticResourceApi* | [**get_login**](docs/StaticResourceApi.md#get_login) | **GET** /login | 
*SystemApi* | [**create_system_restart**](docs/SystemApi.md#create_system_restart) | **POST** /api/v3/system/restart | 
*SystemApi* | [**create_system_shutdown**](docs/SystemApi.md#create_system_shutdown) | **POST** /api/v3/system/shutdown | 
*SystemApi* | [**get_system_routes**](docs/SystemApi.md#get_system_routes) | **GET** /api/v3/system/routes | 
*SystemApi* | [**get_system_routes_duplicate**](docs/SystemApi.md#get_system_routes_duplicate) | **GET** /api/v3/system/routes/duplicate | 
*SystemApi* | [**get_system_status**](docs/SystemApi.md#get_system_status) | **GET** /api/v3/system/status | 
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /api/v3/tag | 
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /api/v3/tag/{id} | 
*TagApi* | [**get_tag_by_id**](docs/TagApi.md#get_tag_by_id) | **GET** /api/v3/tag/{id} | 
*TagApi* | [**list_tag**](docs/TagApi.md#list_tag) | **GET** /api/v3/tag | 
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PUT** /api/v3/tag/{id} | 
*TagDetailsApi* | [**get_tag_detail_by_id**](docs/TagDetailsApi.md#get_tag_detail_by_id) | **GET** /api/v3/tag/detail/{id} | 
*TagDetailsApi* | [**list_tag_detail**](docs/TagDetailsApi.md#list_tag_detail) | **GET** /api/v3/tag/detail | 
*TaskApi* | [**get_system_task_by_id**](docs/TaskApi.md#get_system_task_by_id) | **GET** /api/v3/system/task/{id} | 
*TaskApi* | [**list_system_task**](docs/TaskApi.md#list_system_task) | **GET** /api/v3/system/task | 
*UiConfigApi* | [**get_ui_config**](docs/UiConfigApi.md#get_ui_config) | **GET** /api/v3/config/ui | 
*UiConfigApi* | [**get_ui_config_by_id**](docs/UiConfigApi.md#get_ui_config_by_id) | **GET** /api/v3/config/ui/{id} | 
*UiConfigApi* | [**update_ui_config**](docs/UiConfigApi.md#update_ui_config) | **PUT** /api/v3/config/ui/{id} | 
*UpdateApi* | [**list_update**](docs/UpdateApi.md#list_update) | **GET** /api/v3/update | 
*UpdateLogFileApi* | [**get_log_file_update_by_filename**](docs/UpdateLogFileApi.md#get_log_file_update_by_filename) | **GET** /api/v3/log/file/update/{filename} | 
*UpdateLogFileApi* | [**list_log_file_update**](docs/UpdateLogFileApi.md#list_log_file_update) | **GET** /api/v3/log/file/update | 


## Documentation For Models

 - [AddSeriesOptions](docs/AddSeriesOptions.md)
 - [AlternateTitleResource](docs/AlternateTitleResource.md)
 - [ApplyTags](docs/ApplyTags.md)
 - [AuthenticationRequiredType](docs/AuthenticationRequiredType.md)
 - [AuthenticationType](docs/AuthenticationType.md)
 - [AutoTaggingResource](docs/AutoTaggingResource.md)
 - [AutoTaggingSpecificationSchema](docs/AutoTaggingSpecificationSchema.md)
 - [BackupResource](docs/BackupResource.md)
 - [BackupType](docs/BackupType.md)
 - [BlocklistBulkResource](docs/BlocklistBulkResource.md)
 - [BlocklistResource](docs/BlocklistResource.md)
 - [BlocklistResourcePagingResource](docs/BlocklistResourcePagingResource.md)
 - [CertificateValidationType](docs/CertificateValidationType.md)
 - [Command](docs/Command.md)
 - [CommandPriority](docs/CommandPriority.md)
 - [CommandResource](docs/CommandResource.md)
 - [CommandResult](docs/CommandResult.md)
 - [CommandStatus](docs/CommandStatus.md)
 - [CommandTrigger](docs/CommandTrigger.md)
 - [CustomFilterResource](docs/CustomFilterResource.md)
 - [CustomFormatResource](docs/CustomFormatResource.md)
 - [CustomFormatSpecificationSchema](docs/CustomFormatSpecificationSchema.md)
 - [DelayProfileResource](docs/DelayProfileResource.md)
 - [DiskSpaceResource](docs/DiskSpaceResource.md)
 - [DownloadClientBulkResource](docs/DownloadClientBulkResource.md)
 - [DownloadClientConfigResource](docs/DownloadClientConfigResource.md)
 - [DownloadClientResource](docs/DownloadClientResource.md)
 - [DownloadProtocol](docs/DownloadProtocol.md)
 - [EpisodeFileListResource](docs/EpisodeFileListResource.md)
 - [EpisodeFileResource](docs/EpisodeFileResource.md)
 - [EpisodeHistoryEventType](docs/EpisodeHistoryEventType.md)
 - [EpisodeResource](docs/EpisodeResource.md)
 - [EpisodeResourcePagingResource](docs/EpisodeResourcePagingResource.md)
 - [EpisodeTitleRequiredType](docs/EpisodeTitleRequiredType.md)
 - [EpisodesMonitoredResource](docs/EpisodesMonitoredResource.md)
 - [Field](docs/Field.md)
 - [FileDateType](docs/FileDateType.md)
 - [HealthCheckResult](docs/HealthCheckResult.md)
 - [HealthResource](docs/HealthResource.md)
 - [HistoryResource](docs/HistoryResource.md)
 - [HistoryResourcePagingResource](docs/HistoryResourcePagingResource.md)
 - [HostConfigResource](docs/HostConfigResource.md)
 - [ImportListBulkResource](docs/ImportListBulkResource.md)
 - [ImportListExclusionResource](docs/ImportListExclusionResource.md)
 - [ImportListResource](docs/ImportListResource.md)
 - [ImportListType](docs/ImportListType.md)
 - [IndexerBulkResource](docs/IndexerBulkResource.md)
 - [IndexerConfigResource](docs/IndexerConfigResource.md)
 - [IndexerResource](docs/IndexerResource.md)
 - [Language](docs/Language.md)
 - [LanguageProfileItemResource](docs/LanguageProfileItemResource.md)
 - [LanguageProfileResource](docs/LanguageProfileResource.md)
 - [LanguageResource](docs/LanguageResource.md)
 - [LocalizationLanguageResource](docs/LocalizationLanguageResource.md)
 - [LocalizationResource](docs/LocalizationResource.md)
 - [LogFileResource](docs/LogFileResource.md)
 - [LogResource](docs/LogResource.md)
 - [LogResourcePagingResource](docs/LogResourcePagingResource.md)
 - [ManualImportReprocessResource](docs/ManualImportReprocessResource.md)
 - [ManualImportResource](docs/ManualImportResource.md)
 - [MediaCover](docs/MediaCover.md)
 - [MediaCoverTypes](docs/MediaCoverTypes.md)
 - [MediaInfoResource](docs/MediaInfoResource.md)
 - [MediaManagementConfigResource](docs/MediaManagementConfigResource.md)
 - [MetadataResource](docs/MetadataResource.md)
 - [MonitorTypes](docs/MonitorTypes.md)
 - [MonitoringOptions](docs/MonitoringOptions.md)
 - [NamingConfigResource](docs/NamingConfigResource.md)
 - [NotificationResource](docs/NotificationResource.md)
 - [PagingResourceFilter](docs/PagingResourceFilter.md)
 - [ParseResource](docs/ParseResource.md)
 - [ParsedEpisodeInfo](docs/ParsedEpisodeInfo.md)
 - [PingResource](docs/PingResource.md)
 - [PrivacyLevel](docs/PrivacyLevel.md)
 - [ProfileFormatItemResource](docs/ProfileFormatItemResource.md)
 - [ProperDownloadTypes](docs/ProperDownloadTypes.md)
 - [ProviderMessage](docs/ProviderMessage.md)
 - [ProviderMessageType](docs/ProviderMessageType.md)
 - [ProxyType](docs/ProxyType.md)
 - [Quality](docs/Quality.md)
 - [QualityDefinitionResource](docs/QualityDefinitionResource.md)
 - [QualityModel](docs/QualityModel.md)
 - [QualityProfileQualityItemResource](docs/QualityProfileQualityItemResource.md)
 - [QualityProfileResource](docs/QualityProfileResource.md)
 - [QualitySource](docs/QualitySource.md)
 - [QueueBulkResource](docs/QueueBulkResource.md)
 - [QueueResource](docs/QueueResource.md)
 - [QueueResourcePagingResource](docs/QueueResourcePagingResource.md)
 - [QueueStatusResource](docs/QueueStatusResource.md)
 - [Ratings](docs/Ratings.md)
 - [Rejection](docs/Rejection.md)
 - [RejectionType](docs/RejectionType.md)
 - [ReleaseEpisodeResource](docs/ReleaseEpisodeResource.md)
 - [ReleaseProfileResource](docs/ReleaseProfileResource.md)
 - [ReleaseResource](docs/ReleaseResource.md)
 - [RemotePathMappingResource](docs/RemotePathMappingResource.md)
 - [RenameEpisodeResource](docs/RenameEpisodeResource.md)
 - [RescanAfterRefreshType](docs/RescanAfterRefreshType.md)
 - [Revision](docs/Revision.md)
 - [RootFolderResource](docs/RootFolderResource.md)
 - [RuntimeMode](docs/RuntimeMode.md)
 - [SeasonPassResource](docs/SeasonPassResource.md)
 - [SeasonPassSeriesResource](docs/SeasonPassSeriesResource.md)
 - [SeasonResource](docs/SeasonResource.md)
 - [SeasonStatisticsResource](docs/SeasonStatisticsResource.md)
 - [SelectOption](docs/SelectOption.md)
 - [SeriesEditorResource](docs/SeriesEditorResource.md)
 - [SeriesResource](docs/SeriesResource.md)
 - [SeriesStatisticsResource](docs/SeriesStatisticsResource.md)
 - [SeriesStatusType](docs/SeriesStatusType.md)
 - [SeriesTitleInfo](docs/SeriesTitleInfo.md)
 - [SeriesTypes](docs/SeriesTypes.md)
 - [SortDirection](docs/SortDirection.md)
 - [SystemResource](docs/SystemResource.md)
 - [TagDetailsResource](docs/TagDetailsResource.md)
 - [TagResource](docs/TagResource.md)
 - [TaskResource](docs/TaskResource.md)
 - [TrackedDownloadState](docs/TrackedDownloadState.md)
 - [TrackedDownloadStatus](docs/TrackedDownloadStatus.md)
 - [TrackedDownloadStatusMessage](docs/TrackedDownloadStatusMessage.md)
 - [UiConfigResource](docs/UiConfigResource.md)
 - [UnmappedFolder](docs/UnmappedFolder.md)
 - [UpdateChanges](docs/UpdateChanges.md)
 - [UpdateMechanism](docs/UpdateMechanism.md)
 - [UpdateResource](docs/UpdateResource.md)


## Documentation For Authorization


## X-Api-Key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header


## apikey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author





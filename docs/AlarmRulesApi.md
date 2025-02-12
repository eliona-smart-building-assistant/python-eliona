# eliona.api_client.AlarmRulesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alarm_rule_by_id**](AlarmRulesApi.md#delete_alarm_rule_by_id) | **DELETE** /alarm-rules/{alarm-rule-id} | Delete an alarm rule
[**get_alarm_rule_by_id**](AlarmRulesApi.md#get_alarm_rule_by_id) | **GET** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
[**get_alarm_rules**](AlarmRulesApi.md#get_alarm_rules) | **GET** /alarm-rules | Information about alarm rules
[**post_alarm_rule**](AlarmRulesApi.md#post_alarm_rule) | **POST** /alarm-rules | Create an alarm rule
[**put_alarm_rule**](AlarmRulesApi.md#put_alarm_rule) | **PUT** /alarm-rules | Create or update an alarm rule
[**put_alarm_rule_by_id**](AlarmRulesApi.md#put_alarm_rule_by_id) | **PUT** /alarm-rules/{alarm-rule-id} | Update an alarm rule


# **delete_alarm_rule_by_id**
> delete_alarm_rule_by_id(alarm_rule_id)

Delete an alarm rule

Deletes an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule

    # example passing only required values which don't have defaults set
    try:
        # Delete an alarm rule
        api_instance.delete_alarm_rule_by_id(alarm_rule_id)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->delete_alarm_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_rule_by_id**
> AlarmRule get_alarm_rule_by_id(alarm_rule_id)

Information about an alarm rule

Gets information about an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(alarm_rule_id)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(alarm_rule_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_rules**
> [AlarmRule] get_alarm_rules()

Information about alarm rules

Gets information about alarm rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule_ids = [
        1,
    ] # [int], none_type | List of alarm rule ids for filtering (optional)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    expansions = [
        "expansions_example",
    ] # [str], none_type | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Information about alarm rules
        api_response = api_instance.get_alarm_rules(alarm_rule_ids=alarm_rule_ids, asset_id=asset_id, expansions=expansions)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_ids** | **[int], none_type**| List of alarm rule ids for filtering | [optional]
 **asset_id** | **int**| Filter for a specific asset id | [optional]
 **expansions** | **[str], none_type**| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional]

### Return type

[**[AlarmRule]**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarm rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alarm_rule**
> AlarmRule post_alarm_rule(alarm_rule)

Create an alarm rule

Create a new alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule = AlarmRule(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message={},
        tags=[
            "tags_example",
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        params={},
        notify_on="R",
        dont_mask=False,
        check_type="limits",
        asset_info=Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            tracker_id=4711,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            parent_functional_identifier="4712",
            parent_locational_identifier="4712",
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ) # AlarmRule | 

    # example passing only required values which don't have defaults set
    try:
        # Create an alarm rule
        api_response = api_instance.post_alarm_rule(alarm_rule)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->post_alarm_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  |

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new alarm rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm_rule**
> AlarmRule put_alarm_rule(alarm_rule)

Create or update an alarm rule

Deprecated - Use POST /alarm-rules to create and PUT /alarm-rules/{alarm-rule-id} to update

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule = AlarmRule(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message={},
        tags=[
            "tags_example",
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        params={},
        notify_on="R",
        dont_mask=False,
        check_type="limits",
        asset_info=Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            tracker_id=4711,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            parent_functional_identifier="4712",
            parent_locational_identifier="4712",
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ) # AlarmRule | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update an alarm rule
        api_response = api_instance.put_alarm_rule(alarm_rule)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  |

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing alarm rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm_rule_by_id**
> AlarmRule put_alarm_rule_by_id(alarm_rule_id, alarm_rule)

Update an alarm rule

Update an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import eliona.api_client
from eliona.api_client.api import alarm_rules_api
from eliona.api_client.model.alarm_rule import AlarmRule
from pprint import pprint
# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with eliona.api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alarm_rules_api.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    alarm_rule = AlarmRule(
        asset_id=4711,
        subtype=DataSubtype("input"),
        attribute="temperature",
        enable=True,
        priority=AlarmPriority(2),
        requires_acknowledge=False,
        equal=38.7,
        low=38.7,
        high=38.7,
        message={},
        tags=[
            "tags_example",
        ],
        subject="subject_example",
        urldoc="urldoc_example",
        params={},
        notify_on="R",
        dont_mask=False,
        check_type="limits",
        asset_info=Asset(
            resource_id="123e4567-e89b-12d3-a456-426655440000",
            device_ids=["XYZ0123",173493272],
            project_id="99",
            global_asset_identifier="zurich_swiss",
            name="Station Zurich",
            asset_type="asset_type_example",
            latitude=47.3667,
            longitude=8.55,
            is_tracker=False,
            tracker_id=4711,
            description="Weather station Zurich, Swiss",
            parent_functional_asset_id=4712,
            parent_locational_asset_id=4712,
            parent_functional_identifier="4712",
            parent_locational_identifier="4712",
            tags=["weather","location"],
            attachments=[
                Attachment(
                    name="example.gif",
                    content_type="image/png",
                    encoding="base64",
                    content="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                ),
            ],
        ),
    ) # AlarmRule | 

    # example passing only required values which don't have defaults set
    try:
        # Update an alarm rule
        api_response = api_instance.put_alarm_rule_by_id(alarm_rule_id, alarm_rule)
        pprint(api_response)
    except eliona.api_client.ApiException as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule |
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  |

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


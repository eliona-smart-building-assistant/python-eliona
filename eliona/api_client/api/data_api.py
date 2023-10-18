"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501

    The version of the OpenAPI document: 2.5.4
    Contact: hello@eliona.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eliona.api_client.api_client import ApiClient, Endpoint as _Endpoint
from eliona.api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from eliona.api_client.model.data import Data
from eliona.api_client.model.data_aggregated import DataAggregated


class DataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_data_endpoint = _Endpoint(
            settings={
                'response_type': ([Data],),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data',
                'operation_id': 'get_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'asset_id',
                    'data_subtype',
                    'asset_type_name',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'data_subtype',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('data_subtype',): {

                        "INPUT": "input",
                        "INFO": "info",
                        "STATUS": "status",
                        "OUTPUT": "output"
                    },
                },
                'openapi_types': {
                    'asset_id':
                        (int,),
                    'data_subtype':
                        (str,),
                    'asset_type_name':
                        (str,),
                },
                'attribute_map': {
                    'asset_id': 'assetId',
                    'data_subtype': 'dataSubtype',
                    'asset_type_name': 'assetTypeName',
                },
                'location_map': {
                    'asset_id': 'query',
                    'data_subtype': 'query',
                    'asset_type_name': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_data_aggregated_endpoint = _Endpoint(
            settings={
                'response_type': ([DataAggregated],),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data-aggregated',
                'operation_id': 'get_data_aggregated',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_date',
                    'to_date',
                    'asset_id',
                    'data_subtype',
                    'asset_type_name',
                    'aggregation_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'data_subtype',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('data_subtype',): {

                        "INPUT": "input",
                        "INFO": "info",
                        "STATUS": "status",
                        "OUTPUT": "output"
                    },
                },
                'openapi_types': {
                    'from_date':
                        (str,),
                    'to_date':
                        (str,),
                    'asset_id':
                        (int,),
                    'data_subtype':
                        (str,),
                    'asset_type_name':
                        (str,),
                    'aggregation_id':
                        (int,),
                },
                'attribute_map': {
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'asset_id': 'assetId',
                    'data_subtype': 'dataSubtype',
                    'asset_type_name': 'assetTypeName',
                    'aggregation_id': 'aggregationId',
                },
                'location_map': {
                    'from_date': 'query',
                    'to_date': 'query',
                    'asset_id': 'query',
                    'data_subtype': 'query',
                    'asset_type_name': 'query',
                    'aggregation_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_data_trends_endpoint = _Endpoint(
            settings={
                'response_type': ([Data],),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data-trends',
                'operation_id': 'get_data_trends',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'from_date',
                    'to_date',
                    'asset_id',
                    'data_subtype',
                    'asset_type_name',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'data_subtype',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('data_subtype',): {

                        "INPUT": "input",
                        "INFO": "info",
                        "STATUS": "status",
                        "OUTPUT": "output"
                    },
                },
                'openapi_types': {
                    'from_date':
                        (str,),
                    'to_date':
                        (str,),
                    'asset_id':
                        (int,),
                    'data_subtype':
                        (str,),
                    'asset_type_name':
                        (str,),
                },
                'attribute_map': {
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'asset_id': 'assetId',
                    'data_subtype': 'dataSubtype',
                    'asset_type_name': 'assetTypeName',
                },
                'location_map': {
                    'from_date': 'query',
                    'to_date': 'query',
                    'asset_id': 'query',
                    'data_subtype': 'query',
                    'asset_type_name': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.listen_data_endpoint = _Endpoint(
            settings={
                'response_type': (Data,),
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data-listener',
                'operation_id': 'listen_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'asset_id',
                    'data_subtype',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'data_subtype',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('data_subtype',): {

                        "INPUT": "input",
                        "INFO": "info",
                        "STATUS": "status",
                        "OUTPUT": "output"
                    },
                },
                'openapi_types': {
                    'asset_id':
                        (int,),
                    'data_subtype':
                        (str,),
                },
                'attribute_map': {
                    'asset_id': 'assetId',
                    'data_subtype': 'dataSubtype',
                },
                'location_map': {
                    'asset_id': 'query',
                    'data_subtype': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.put_bulk_data_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data-bulk',
                'operation_id': 'put_bulk_data',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'data',
                ],
                'required': [
                    'data',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data':
                        ([Data],),
                },
                'attribute_map': {
                },
                'location_map': {
                    'data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.put_data_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth',
                    'BearerAuth'
                ],
                'endpoint_path': '/data',
                'operation_id': 'put_data',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'data',
                ],
                'required': [
                    'data',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data':
                        (Data,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'data': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_data(
        self,
        **kwargs
    ):
        """Gets all data  # noqa: E501

        Gets information about data for assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            asset_id (int): Filter for a specific asset id. [optional]
            data_subtype (str): Filter for a specific type of asset data. [optional]
            asset_type_name (str): Filter the name of the asset type. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [Data]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_data_endpoint.call_with_http_info(**kwargs)

    def get_data_aggregated(
        self,
        **kwargs
    ):
        """Get aggregated data  # noqa: E501

        Gets aggregated data sets which combines a set of data points for a defined periodical raster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_aggregated(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            from_date (str): Filter by lower date time (RFC3339) limit inclusive. [optional]
            to_date (str): Filter by upper date time (RFC3339) limit exclusive. [optional]
            asset_id (int): Filter for a specific asset id. [optional]
            data_subtype (str): Filter for a specific type of asset data. [optional]
            asset_type_name (str): Filter the name of the asset type. [optional]
            aggregation_id (int): Filter for a specific aggregation id. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [DataAggregated]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_data_aggregated_endpoint.call_with_http_info(**kwargs)

    def get_data_trends(
        self,
        **kwargs
    ):
        """Get trend of historical data  # noqa: E501

        Gets trend information about historical data for assets.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_trends(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            from_date (str): Filter by lower date time (RFC3339) limit inclusive. [optional]
            to_date (str): Filter by upper date time (RFC3339) limit exclusive. [optional]
            asset_id (int): Filter for a specific asset id. [optional]
            data_subtype (str): Filter for a specific type of asset data. [optional]
            asset_type_name (str): Filter the name of the asset type. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [Data]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_data_trends_endpoint.call_with_http_info(**kwargs)

    def listen_data(
        self,
        **kwargs
    ):
        """WebSocket connection for asset data changes  # noqa: E501

        Open a WebSocket connection to get informed when new asset data is written or anything changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.listen_data(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            asset_id (int): Filter for a specific asset id. [optional]
            data_subtype (str): Filter for a specific type of asset data. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Data
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.listen_data_endpoint.call_with_http_info(**kwargs)

    def put_bulk_data(
        self,
        data,
        **kwargs
    ):
        """Create or update multiple asset data  # noqa: E501

        Create multiple asset data or update data if already exists. Uses the unique combination of asset id and subtype for updating.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_bulk_data(data, async_req=True)
        >>> result = thread.get()

        Args:
            data ([Data]):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['data'] = \
            data
        return self.put_bulk_data_endpoint.call_with_http_info(**kwargs)

    def put_data(
        self,
        data,
        **kwargs
    ):
        """Create or update asset data  # noqa: E501

        Create new asset data or update data if already exists. Uses the unique combination of asset id and subtype for updating.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_data(data, async_req=True)
        >>> result = thread.get()

        Args:
            data (Data):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['data'] = \
            data
        return self.put_data_endpoint.call_with_http_info(**kwargs)


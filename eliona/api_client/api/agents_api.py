"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.2.0
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
from eliona.api_client.model.agent import Agent
from eliona.api_client.model.agent_device import AgentDevice
from eliona.api_client.model.agent_device_mapping import AgentDeviceMapping


class AgentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_agent_device_mappings_by_id_endpoint = _Endpoint(
            settings={
                'response_type': ([AgentDeviceMapping],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agent-devices/{agent-class}/{agent-device-id}/mappings',
                'operation_id': 'get_agent_device_mappings_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                    'agent_device_id',
                ],
                'required': [
                    'agent_class',
                    'agent_device_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                    'agent_device_id':
                        (int,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                    'agent_device_id': 'agent-device-id',
                },
                'location_map': {
                    'agent_class': 'path',
                    'agent_device_id': 'path',
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
        self.get_agent_devices_by_id_endpoint = _Endpoint(
            settings={
                'response_type': ([AgentDevice],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agents/{agent-class}/{agent-id}/devices',
                'operation_id': 'get_agent_devices_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                    'agent_id',
                ],
                'required': [
                    'agent_class',
                    'agent_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                    'agent_id':
                        (int,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                    'agent_id': 'agent-id',
                },
                'location_map': {
                    'agent_class': 'path',
                    'agent_id': 'path',
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
        self.get_agents_endpoint = _Endpoint(
            settings={
                'response_type': ([Agent],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agents',
                'operation_id': 'get_agents',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
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
                },
                'attribute_map': {
                },
                'location_map': {
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
        self.get_agents_by_class_endpoint = _Endpoint(
            settings={
                'response_type': ([Agent],),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agents/{agent-class}',
                'operation_id': 'get_agents_by_class',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                ],
                'required': [
                    'agent_class',
                ],
                'nullable': [
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                },
                'location_map': {
                    'agent_class': 'path',
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
        self.put_agent_by_class_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agents/{agent-class}',
                'operation_id': 'put_agent_by_class',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                    'agent',
                ],
                'required': [
                    'agent_class',
                    'agent',
                ],
                'nullable': [
                    'agent',
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                    'agent':
                        (Agent,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                },
                'location_map': {
                    'agent_class': 'path',
                    'agent': 'body',
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
        self.put_agent_device_by_id_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agents/{agent-class}/{agent-id}/devices',
                'operation_id': 'put_agent_device_by_id',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                    'agent_id',
                    'agent_device',
                ],
                'required': [
                    'agent_class',
                    'agent_id',
                    'agent_device',
                ],
                'nullable': [
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                    'agent_id':
                        (int,),
                    'agent_device':
                        (AgentDevice,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                    'agent_id': 'agent-id',
                },
                'location_map': {
                    'agent_class': 'path',
                    'agent_id': 'path',
                    'agent_device': 'body',
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
        self.put_agent_device_mapping_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (AgentDeviceMapping,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/agent-devices/{agent-class}/{agent-device-id}/mappings',
                'operation_id': 'put_agent_device_mapping_by_id',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'agent_class',
                    'agent_device_id',
                    'agent_device_mapping',
                ],
                'required': [
                    'agent_class',
                    'agent_device_id',
                    'agent_device_mapping',
                ],
                'nullable': [
                ],
                'enum': [
                    'agent_class',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('agent_class',): {

                        "IOSYS": "iosys",
                        "MBUS": "mbus"
                    },
                },
                'openapi_types': {
                    'agent_class':
                        (str,),
                    'agent_device_id':
                        (int,),
                    'agent_device_mapping':
                        (AgentDeviceMapping,),
                },
                'attribute_map': {
                    'agent_class': 'agent-class',
                    'agent_device_id': 'agent-device-id',
                },
                'location_map': {
                    'agent_class': 'path',
                    'agent_device_id': 'path',
                    'agent_device_mapping': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_agent_device_mappings_by_id(
        self,
        agent_class,
        agent_device_id,
        **kwargs
    ):
        """Information about agent device mappings  # noqa: E501

        Gets information about mappings between agent and eliona.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_device_mappings_by_id(agent_class, agent_device_id, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent
            agent_device_id (int): The id of the device

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
            [AgentDeviceMapping]
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
        kwargs['agent_class'] = \
            agent_class
        kwargs['agent_device_id'] = \
            agent_device_id
        return self.get_agent_device_mappings_by_id_endpoint.call_with_http_info(**kwargs)

    def get_agent_devices_by_id(
        self,
        agent_class,
        agent_id,
        **kwargs
    ):
        """Information about agent devices  # noqa: E501

        Gets information about agent devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_devices_by_id(agent_class, agent_id, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent
            agent_id (int): The id of the agent

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
            [AgentDevice]
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
        kwargs['agent_class'] = \
            agent_class
        kwargs['agent_id'] = \
            agent_id
        return self.get_agent_devices_by_id_endpoint.call_with_http_info(**kwargs)

    def get_agents(
        self,
        **kwargs
    ):
        """Information about agents  # noqa: E501

        Gets information about agents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agents(async_req=True)
        >>> result = thread.get()


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
            [Agent]
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
        return self.get_agents_endpoint.call_with_http_info(**kwargs)

    def get_agents_by_class(
        self,
        agent_class,
        **kwargs
    ):
        """Information about agents for a specific class  # noqa: E501

        Gets information about agents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agents_by_class(agent_class, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent

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
            [Agent]
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
        kwargs['agent_class'] = \
            agent_class
        return self.get_agents_by_class_endpoint.call_with_http_info(**kwargs)

    def put_agent_by_class(
        self,
        agent_class,
        agent,
        **kwargs
    ):
        """Create or update an agent for a specific class  # noqa: E501

        Create a new agent or update an agent if already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_agent_by_class(agent_class, agent, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent
            agent (Agent):

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
        kwargs['agent_class'] = \
            agent_class
        kwargs['agent'] = \
            agent
        return self.put_agent_by_class_endpoint.call_with_http_info(**kwargs)

    def put_agent_device_by_id(
        self,
        agent_class,
        agent_id,
        agent_device,
        **kwargs
    ):
        """Create or update an agent device  # noqa: E501

        Create a new agent device or update an agent device if already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_agent_device_by_id(agent_class, agent_id, agent_device, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent
            agent_id (int): The id of the agent
            agent_device (AgentDevice):

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
        kwargs['agent_class'] = \
            agent_class
        kwargs['agent_id'] = \
            agent_id
        kwargs['agent_device'] = \
            agent_device
        return self.put_agent_device_by_id_endpoint.call_with_http_info(**kwargs)

    def put_agent_device_mapping_by_id(
        self,
        agent_class,
        agent_device_id,
        agent_device_mapping,
        **kwargs
    ):
        """Create or update an agent device mapping  # noqa: E501

        Create a new agent device mapping or update an agent device mapping if already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_agent_device_mapping_by_id(agent_class, agent_device_id, agent_device_mapping, async_req=True)
        >>> result = thread.get()

        Args:
            agent_class (str): The class of an agent
            agent_device_id (int): The id of the device
            agent_device_mapping (AgentDeviceMapping):

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
            AgentDeviceMapping
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
        kwargs['agent_class'] = \
            agent_class
        kwargs['agent_device_id'] = \
            agent_device_id
        kwargs['agent_device_mapping'] = \
            agent_device_mapping
        return self.put_agent_device_mapping_by_id_endpoint.call_with_http_info(**kwargs)


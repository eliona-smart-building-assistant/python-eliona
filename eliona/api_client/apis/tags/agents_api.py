# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""

from eliona.api_client.paths.agents_agent_class_agent_id.get import GetAgentByClassAndId
from eliona.api_client.paths.agent_devices_agent_class_agent_device_id.get import GetAgentDeviceById
from eliona.api_client.paths.agent_device_mappings_agent_class_agent_device_mapping_id.get import GetAgentDeviceMappingById
from eliona.api_client.paths.agent_devices_agent_class_agent_device_id_mappings.get import GetAgentDeviceMappingsByDeviceId
from eliona.api_client.paths.agents_agent_class_agent_id_devices.get import GetAgentDevicesByAgentId
from eliona.api_client.paths.agents.get import GetAgents
from eliona.api_client.paths.agents_agent_class.get import GetAgentsByClass
from eliona.api_client.paths.agents_agent_class.post import PostAgentByClass
from eliona.api_client.paths.agents_agent_class_agent_id_devices.post import PostAgentDeviceByAgentId
from eliona.api_client.paths.agent_devices_agent_class_agent_device_id_mappings.post import PostAgentDeviceMappingByDeviceId
from eliona.api_client.paths.agents_agent_class.put import PutAgentByClass
from eliona.api_client.paths.agents_agent_class_agent_id.put import PutAgentByClassAndId
from eliona.api_client.paths.agents_agent_class_agent_id_devices.put import PutAgentDeviceByAgentId
from eliona.api_client.paths.agent_devices_agent_class_agent_device_id.put import PutAgentDeviceById
from eliona.api_client.paths.agent_devices_agent_class_agent_device_id_mappings.put import PutAgentDeviceMappingByDeviceId
from eliona.api_client.paths.agent_device_mappings_agent_class_agent_device_mapping_id.put import PutAgentDeviceMappingById


class AgentsApi(
    GetAgentByClassAndId,
    GetAgentDeviceById,
    GetAgentDeviceMappingById,
    GetAgentDeviceMappingsByDeviceId,
    GetAgentDevicesByAgentId,
    GetAgents,
    GetAgentsByClass,
    PostAgentByClass,
    PostAgentDeviceByAgentId,
    PostAgentDeviceMappingByDeviceId,
    PutAgentByClass,
    PutAgentByClassAndId,
    PutAgentDeviceByAgentId,
    PutAgentDeviceById,
    PutAgentDeviceMappingByDeviceId,
    PutAgentDeviceMappingById,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

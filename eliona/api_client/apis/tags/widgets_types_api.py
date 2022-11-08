# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.4.3
    Generated by: https://openapi-generator.tech
"""

from eliona.api_client.paths.widget_types_widget_type_name.delete import DeleteWidgetTypeByName
from eliona.api_client.paths.widget_types_widget_type_name.get import GetWidgetTypeByName
from eliona.api_client.paths.widget_types.get import GetWidgetTypes
from eliona.api_client.paths.widget_types.post import PostWidgetType
from eliona.api_client.paths.widget_types.put import PutWidgetType
from eliona.api_client.paths.widget_types_widget_type_name.put import PutWidgetTypeByName


class WidgetsTypesApi(
    DeleteWidgetTypeByName,
    GetWidgetTypeByName,
    GetWidgetTypes,
    PostWidgetType,
    PutWidgetType,
    PutWidgetTypeByName,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

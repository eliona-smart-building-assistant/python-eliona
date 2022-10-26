# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from eliona.api_client import schemas  # noqa: F401


class Data(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Data for assets
    """


    class MetaOapg:
        required = {
            "data",
            "subtype",
            "assetId",
        }
        
        class properties:
            assetId = schemas.IntSchema
        
            @staticmethod
            def subtype() -> typing.Type['DataSubtype']:
                return DataSubtype
            data = schemas.DictSchema
            
            
            class timestamp(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'timestamp':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class assetTypeName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assetTypeName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "assetId": assetId,
                "subtype": subtype,
                "data": data,
                "timestamp": timestamp,
                "assetTypeName": assetTypeName,
            }
    
    data: MetaOapg.properties.data
    subtype: 'DataSubtype'
    assetId: MetaOapg.properties.assetId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetTypeName"]) -> MetaOapg.properties.assetTypeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetId", "subtype", "data", "timestamp", "assetTypeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetTypeName"]) -> typing.Union[MetaOapg.properties.assetTypeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetId", "subtype", "data", "timestamp", "assetTypeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, ],
        subtype: 'DataSubtype',
        assetId: typing.Union[MetaOapg.properties.assetId, decimal.Decimal, int, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, None, str, datetime, schemas.Unset] = schemas.unset,
        assetTypeName: typing.Union[MetaOapg.properties.assetTypeName, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Data':
        return super().__new__(
            cls,
            *args,
            data=data,
            subtype=subtype,
            assetId=assetId,
            timestamp=timestamp,
            assetTypeName=assetTypeName,
            _configuration=_configuration,
            **kwargs,
        )

from eliona/api_client.model.data_subtype import DataSubtype

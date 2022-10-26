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


class Alarm(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An alarm
    """


    class MetaOapg:
        required = {
            "occurrences",
            "subtype",
            "assetId",
            "priority",
            "timestamp",
        }
        
        class properties:
            assetId = schemas.IntSchema
        
            @staticmethod
            def subtype() -> typing.Type['DataSubtype']:
                return DataSubtype
        
            @staticmethod
            def priority() -> typing.Type['AlarmPriority']:
                return AlarmPriority
            timestamp = schemas.DateTimeSchema
            occurrences = schemas.IntSchema
            
            
            class ruleId(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ruleId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class attribute(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attribute':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            requiresAcknowledge = schemas.BoolSchema
            
            
            class value(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goneTimestamp(
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
                ) -> 'goneTimestamp':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class acknowledgeTimestamp(
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
                ) -> 'acknowledgeTimestamp':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class acknowledgeText(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'acknowledgeText':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class acknowledgeUserId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'text'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'acknowledgeUserId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class message(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def assetInfo() -> typing.Type['Asset']:
                return Asset
        
            @staticmethod
            def ruleInfo() -> typing.Type['AlarmRule']:
                return AlarmRule
            __annotations__ = {
                "assetId": assetId,
                "subtype": subtype,
                "priority": priority,
                "timestamp": timestamp,
                "occurrences": occurrences,
                "ruleId": ruleId,
                "attribute": attribute,
                "requiresAcknowledge": requiresAcknowledge,
                "value": value,
                "goneTimestamp": goneTimestamp,
                "acknowledgeTimestamp": acknowledgeTimestamp,
                "acknowledgeText": acknowledgeText,
                "acknowledgeUserId": acknowledgeUserId,
                "message": message,
                "assetInfo": assetInfo,
                "ruleInfo": ruleInfo,
            }

    
    occurrences: MetaOapg.properties.occurrences
    subtype: 'DataSubtype'
    assetId: MetaOapg.properties.assetId
    priority: 'AlarmPriority'
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> 'AlarmPriority': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["occurrences"]) -> MetaOapg.properties.occurrences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleId"]) -> MetaOapg.properties.ruleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute"]) -> MetaOapg.properties.attribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requiresAcknowledge"]) -> MetaOapg.properties.requiresAcknowledge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goneTimestamp"]) -> MetaOapg.properties.goneTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledgeTimestamp"]) -> MetaOapg.properties.acknowledgeTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledgeText"]) -> MetaOapg.properties.acknowledgeText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acknowledgeUserId"]) -> MetaOapg.properties.acknowledgeUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetInfo"]) -> 'Asset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ruleInfo"]) -> 'AlarmRule': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetId", "subtype", "priority", "timestamp", "occurrences", "ruleId", "attribute", "requiresAcknowledge", "value", "goneTimestamp", "acknowledgeTimestamp", "acknowledgeText", "acknowledgeUserId", "message", "assetInfo", "ruleInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtype"]) -> 'DataSubtype': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> 'AlarmPriority': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["occurrences"]) -> MetaOapg.properties.occurrences: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleId"]) -> typing.Union[MetaOapg.properties.ruleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute"]) -> typing.Union[MetaOapg.properties.attribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requiresAcknowledge"]) -> typing.Union[MetaOapg.properties.requiresAcknowledge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goneTimestamp"]) -> typing.Union[MetaOapg.properties.goneTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledgeTimestamp"]) -> typing.Union[MetaOapg.properties.acknowledgeTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledgeText"]) -> typing.Union[MetaOapg.properties.acknowledgeText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acknowledgeUserId"]) -> typing.Union[MetaOapg.properties.acknowledgeUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetInfo"]) -> typing.Union['Asset', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ruleInfo"]) -> typing.Union['AlarmRule', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetId", "subtype", "priority", "timestamp", "occurrences", "ruleId", "attribute", "requiresAcknowledge", "value", "goneTimestamp", "acknowledgeTimestamp", "acknowledgeText", "acknowledgeUserId", "message", "assetInfo", "ruleInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        ruleId: typing.Union[MetaOapg.properties.ruleId, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        attribute: typing.Union[MetaOapg.properties.attribute, None, str, schemas.Unset] = schemas.unset,
        requiresAcknowledge: typing.Union[MetaOapg.properties.requiresAcknowledge, bool, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        goneTimestamp: typing.Union[MetaOapg.properties.goneTimestamp, None, str, datetime, schemas.Unset] = schemas.unset,
        acknowledgeTimestamp: typing.Union[MetaOapg.properties.acknowledgeTimestamp, None, str, datetime, schemas.Unset] = schemas.unset,
        acknowledgeText: typing.Union[MetaOapg.properties.acknowledgeText, None, str, schemas.Unset] = schemas.unset,
        acknowledgeUserId: typing.Union[MetaOapg.properties.acknowledgeUserId, None, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        assetInfo: typing.Union['Asset', schemas.Unset] = schemas.unset,
        ruleInfo: typing.Union['AlarmRule', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Alarm':
        return super().__new__(
            cls,
            *args,
            ruleId=ruleId,
            attribute=attribute,
            requiresAcknowledge=requiresAcknowledge,
            value=value,
            goneTimestamp=goneTimestamp,
            acknowledgeTimestamp=acknowledgeTimestamp,
            acknowledgeText=acknowledgeText,
            acknowledgeUserId=acknowledgeUserId,
            message=message,
            assetInfo=assetInfo,
            ruleInfo=ruleInfo,
            _configuration=_configuration,
            **kwargs,
        )

from eliona/api_client.model.alarm_priority import AlarmPriority
from eliona/api_client.model.alarm_rule import AlarmRule
from eliona/api_client.model.asset import Asset
from eliona/api_client.model.data_subtype import DataSubtype

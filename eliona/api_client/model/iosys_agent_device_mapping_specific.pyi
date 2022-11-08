# coding: utf-8

"""
    Eliona API

    API to access Eliona Smart Building Assistant  # noqa: E501

    The version of the OpenAPI document: 2.4.3
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


class IosysAgentDeviceMappingSpecific(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specific mapping for IOSYS agents
    """


    class MetaOapg:
        
        class properties:
            
            
            class iosVar(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iosVar':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class iosType(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "INT": "INT",
                        "REAL": "REAL",
                        "STRING": "STRING",
                    }
                
                @schemas.classproperty
                def INT(cls):
                    return cls("INT")
                
                @schemas.classproperty
                def REAL(cls):
                    return cls("REAL")
                
                @schemas.classproperty
                def STRING(cls):
                    return cls("STRING")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iosType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class down(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'down':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class scale(
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
                ) -> 'scale':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class zero(
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
                ) -> 'zero':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class mask(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mask':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class maskAttributes(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maskAttributes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class deadTime(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deadTime':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class deadBand(
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
                ) -> 'deadBand':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class filter(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "LPF1": "LPF1",
                        "LPF2": "LPF2",
                        "MOVA": "MOVA",
                    }
                
                @schemas.classproperty
                def LPF1(cls):
                    return cls("LPF1")
                
                @schemas.classproperty
                def LPF2(cls):
                    return cls("LPF2")
                
                @schemas.classproperty
                def MOVA(cls):
                    return cls("MOVA")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'filter':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class tau(
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
                ) -> 'tau':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "iosVar": iosVar,
                "iosType": iosType,
                "down": down,
                "scale": scale,
                "zero": zero,
                "mask": mask,
                "maskAttributes": maskAttributes,
                "deadTime": deadTime,
                "deadBand": deadBand,
                "filter": filter,
                "tau": tau,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iosVar"]) -> MetaOapg.properties.iosVar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iosType"]) -> MetaOapg.properties.iosType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["down"]) -> MetaOapg.properties.down: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scale"]) -> MetaOapg.properties.scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zero"]) -> MetaOapg.properties.zero: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mask"]) -> MetaOapg.properties.mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maskAttributes"]) -> MetaOapg.properties.maskAttributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deadTime"]) -> MetaOapg.properties.deadTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deadBand"]) -> MetaOapg.properties.deadBand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tau"]) -> MetaOapg.properties.tau: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["iosVar", "iosType", "down", "scale", "zero", "mask", "maskAttributes", "deadTime", "deadBand", "filter", "tau", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iosVar"]) -> typing.Union[MetaOapg.properties.iosVar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iosType"]) -> typing.Union[MetaOapg.properties.iosType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["down"]) -> typing.Union[MetaOapg.properties.down, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scale"]) -> typing.Union[MetaOapg.properties.scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zero"]) -> typing.Union[MetaOapg.properties.zero, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mask"]) -> typing.Union[MetaOapg.properties.mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maskAttributes"]) -> typing.Union[MetaOapg.properties.maskAttributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deadTime"]) -> typing.Union[MetaOapg.properties.deadTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deadBand"]) -> typing.Union[MetaOapg.properties.deadBand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tau"]) -> typing.Union[MetaOapg.properties.tau, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["iosVar", "iosType", "down", "scale", "zero", "mask", "maskAttributes", "deadTime", "deadBand", "filter", "tau", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        iosVar: typing.Union[MetaOapg.properties.iosVar, None, str, schemas.Unset] = schemas.unset,
        iosType: typing.Union[MetaOapg.properties.iosType, None, str, schemas.Unset] = schemas.unset,
        down: typing.Union[MetaOapg.properties.down, None, bool, schemas.Unset] = schemas.unset,
        scale: typing.Union[MetaOapg.properties.scale, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        zero: typing.Union[MetaOapg.properties.zero, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        mask: typing.Union[MetaOapg.properties.mask, list, tuple, None, schemas.Unset] = schemas.unset,
        maskAttributes: typing.Union[MetaOapg.properties.maskAttributes, list, tuple, None, schemas.Unset] = schemas.unset,
        deadTime: typing.Union[MetaOapg.properties.deadTime, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deadBand: typing.Union[MetaOapg.properties.deadBand, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, None, str, schemas.Unset] = schemas.unset,
        tau: typing.Union[MetaOapg.properties.tau, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IosysAgentDeviceMappingSpecific':
        return super().__new__(
            cls,
            *args,
            iosVar=iosVar,
            iosType=iosType,
            down=down,
            scale=scale,
            zero=zero,
            mask=mask,
            maskAttributes=maskAttributes,
            deadTime=deadTime,
            deadBand=deadBand,
            filter=filter,
            tau=tau,
            _configuration=_configuration,
            **kwargs,
        )

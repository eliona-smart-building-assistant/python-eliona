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


class AgentClass(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The class of an agent
    """


    class MetaOapg:
        enum_value_to_name = {
            "iosys": "AGENT_CLASS_IOSYS",
            "mbus": "AGENT_CLASS_MBUS",
        }
    
    @schemas.classproperty
    def AGENT_CLASS_IOSYS(cls):
        return cls("iosys")
    
    @schemas.classproperty
    def AGENT_CLASS_MBUS(cls):
        return cls("mbus")


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AgentClass':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )

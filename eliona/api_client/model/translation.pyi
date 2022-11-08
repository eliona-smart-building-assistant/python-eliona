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


class Translation(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Readable text to display in frontend
    """


    class MetaOapg:
        
        class properties:
            de = schemas.StrSchema
            en = schemas.StrSchema
            fr = schemas.StrSchema
            it = schemas.StrSchema
            __annotations__ = {
                "de": de,
                "en": en,
                "fr": fr,
                "it": it,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["de"]) -> MetaOapg.properties.de: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["en"]) -> MetaOapg.properties.en: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fr"]) -> MetaOapg.properties.fr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["it"]) -> MetaOapg.properties.it: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["de", "en", "fr", "it", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["de"]) -> typing.Union[MetaOapg.properties.de, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["en"]) -> typing.Union[MetaOapg.properties.en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fr"]) -> typing.Union[MetaOapg.properties.fr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["it"]) -> typing.Union[MetaOapg.properties.it, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["de", "en", "fr", "it", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        de: typing.Union[MetaOapg.properties.de, str, schemas.Unset] = schemas.unset,
        en: typing.Union[MetaOapg.properties.en, str, schemas.Unset] = schemas.unset,
        fr: typing.Union[MetaOapg.properties.fr, str, schemas.Unset] = schemas.unset,
        it: typing.Union[MetaOapg.properties.it, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Translation':
        return super().__new__(
            cls,
            *args,
            de=de,
            en=en,
            fr=fr,
            it=it,
            _configuration=_configuration,
            **kwargs,
        )

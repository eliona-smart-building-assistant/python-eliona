"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501

    The version of the OpenAPI document: 2.4.12
    Contact: hello@eliona.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eliona.api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from eliona.api_client.exceptions import ApiAttributeError


def lazy_import():
    from eliona.api_client.model.alarm_priority import AlarmPriority
    from eliona.api_client.model.asset import Asset
    from eliona.api_client.model.data_subtype import DataSubtype
    globals()['AlarmPriority'] = AlarmPriority
    globals()['Asset'] = Asset
    globals()['DataSubtype'] = DataSubtype


class AlarmRule(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'asset_id': (int,),  # noqa: E501
            'subtype': (DataSubtype,),  # noqa: E501
            'attribute': (str,),  # noqa: E501
            'priority': (AlarmPriority,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'enable': (bool,),  # noqa: E501
            'requires_acknowledge': (bool,),  # noqa: E501
            'equal': (float, none_type,),  # noqa: E501
            'low': (float, none_type,),  # noqa: E501
            'high': (float, none_type,),  # noqa: E501
            'message': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'tags': ([str], none_type,),  # noqa: E501
            'subject': (str, none_type,),  # noqa: E501
            'urldoc': (str, none_type,),  # noqa: E501
            'notify_on': (str, none_type,),  # noqa: E501
            'dont_mask': (bool, none_type,),  # noqa: E501
            'asset_info': (Asset,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'asset_id': 'assetId',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'attribute': 'attribute',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'id': 'id',  # noqa: E501
        'enable': 'enable',  # noqa: E501
        'requires_acknowledge': 'requiresAcknowledge',  # noqa: E501
        'equal': 'equal',  # noqa: E501
        'low': 'low',  # noqa: E501
        'high': 'high',  # noqa: E501
        'message': 'message',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'urldoc': 'urldoc',  # noqa: E501
        'notify_on': 'notifyOn',  # noqa: E501
        'dont_mask': 'dontMask',  # noqa: E501
        'asset_info': 'assetInfo',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, asset_id, subtype, attribute, priority, *args, **kwargs):  # noqa: E501
        """AlarmRule - a model defined in OpenAPI

        Args:
            asset_id (int): ID of the corresponding asset
            subtype (DataSubtype):
            attribute (str): Name of the attribute of the asset type
            priority (AlarmPriority):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int, none_type): The id of the rule. [optional]  # noqa: E501
            enable (bool): Rule enabled or not. [optional] if omitted the server will use the default value of True  # noqa: E501
            requires_acknowledge (bool): Requires the alarm an acknowledgment. [optional] if omitted the server will use the default value of False  # noqa: E501
            equal (float, none_type): Triggers alarm if attribute value equals this value. [optional]  # noqa: E501
            low (float, none_type): Triggers alarm if attribute value is less than value. [optional]  # noqa: E501
            high (float, none_type): Triggers alarm if attribute value is greater than value. [optional]  # noqa: E501
            message ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Texts for alarm. [optional]  # noqa: E501
            tags ([str], none_type): List of associated tags. [optional]  # noqa: E501
            subject (str, none_type): The subject for the alarm. [optional]  # noqa: E501
            urldoc (str, none_type): The url describing the alarm. [optional]  # noqa: E501
            notify_on (str, none_type): Notification. [optional]  # noqa: E501
            dont_mask (bool, none_type): Do not mask. [optional] if omitted the server will use the default value of False  # noqa: E501
            asset_info (Asset): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_id = asset_id
        self.subtype = subtype
        self.attribute = attribute
        self.priority = priority
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, asset_id, subtype, attribute, priority, *args, **kwargs):  # noqa: E501
        """AlarmRule - a model defined in OpenAPI

        Args:
            asset_id (int): ID of the corresponding asset
            subtype (DataSubtype):
            attribute (str): Name of the attribute of the asset type
            priority (AlarmPriority):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int, none_type): The id of the rule. [optional]  # noqa: E501
            enable (bool): Rule enabled or not. [optional] if omitted the server will use the default value of True  # noqa: E501
            requires_acknowledge (bool): Requires the alarm an acknowledgment. [optional] if omitted the server will use the default value of False  # noqa: E501
            equal (float, none_type): Triggers alarm if attribute value equals this value. [optional]  # noqa: E501
            low (float, none_type): Triggers alarm if attribute value is less than value. [optional]  # noqa: E501
            high (float, none_type): Triggers alarm if attribute value is greater than value. [optional]  # noqa: E501
            message ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Texts for alarm. [optional]  # noqa: E501
            tags ([str], none_type): List of associated tags. [optional]  # noqa: E501
            subject (str, none_type): The subject for the alarm. [optional]  # noqa: E501
            urldoc (str, none_type): The url describing the alarm. [optional]  # noqa: E501
            notify_on (str, none_type): Notification. [optional]  # noqa: E501
            dont_mask (bool, none_type): Do not mask. [optional] if omitted the server will use the default value of False  # noqa: E501
            asset_info (Asset): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.asset_id = asset_id
        self.subtype = subtype
        self.attribute = attribute
        self.priority = priority
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

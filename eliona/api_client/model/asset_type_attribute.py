"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.  # noqa: E501

    The version of the OpenAPI document: 2.5.9
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
    from eliona.api_client.model.data_subtype import DataSubtype
    from eliona.api_client.model.translation import Translation
    from eliona.api_client.model.value_mapping import ValueMapping
    globals()['DataSubtype'] = DataSubtype
    globals()['Translation'] = Translation
    globals()['ValueMapping'] = ValueMapping


class AssetTypeAttribute(ModelNormal):
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
        ('type',): {
            'None': None,
            'AIR_QUALITY': "air_quality",
            'BATTERY-VOLTAGE': "battery-voltage",
            'BRIGHTNESS': "brightness",
            'CO2': "co2",
            'CURRENT': "current",
            'DEVICE-INFO': "device-info",
            'DEVICE-STATUS': "device-status",
            'ENERGY': "energy",
            'FLOW': "flow",
            'FREQUENCY': "frequency",
            'HUMIDITY': "humidity",
            'INPUTS-AND-SWITCHES': "inputs-and-switches",
            'LEVEL': "level",
            'MOTION': "motion",
            'OPERATING-STATUS': "operating-status",
            'PEOPLE-COUNT': "people-count",
            'POWER': "power",
            'PRESENCE': "presence",
            'PRESSURE': "pressure",
            'TEMPERATURE': "temperature",
            'VEHICLE-DETECTOR': "vehicle-detector",
            'VOLTAGE': "voltage",
            'WEATHER': "weather",
            'VOC': "voc",
        },
        ('aggregation_mode',): {
            'None': None,
            'AVG': "avg",
            'SUM': "sum",
            'CUSUM': "cusum",
            'AVG-ON-CHANGE': "avg-on-change",
        },
        ('aggregation_rasters',): {
            'S1': "S1",
            'S2': "S2",
            'S3': "S3",
            'S4': "S4",
            'S5': "S5",
            'S6': "S6",
            'S10': "S10",
            'S12': "S12",
            'S15': "S15",
            'S20': "S20",
            'S30': "S30",
            'M1': "M1",
            'M2': "M2",
            'M3': "M3",
            'M4': "M4",
            'M5': "M5",
            'M6': "M6",
            'M10': "M10",
            'M12': "M12",
            'M15': "M15",
            'M20': "M20",
            'M30': "M30",
            'H1': "H1",
            'H2': "H2",
            'H3': "H3",
            'H4': "H4",
            'H6': "H6",
            'H8': "H8",
            'H12': "H12",
            'DAY': "DAY",
            'WEEK': "WEEK",
            'MONTH': "MONTH",
            'QUARTER': "QUARTER",
            'YEAR': "YEAR",
            'DECADE': "DECADE",
            'CENTURY': "CENTURY",
        },
    }

    validations = {
        ('precision',): {
            'inclusive_maximum': 20,
            'inclusive_minimum': -20,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

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
            'name': (str,),  # noqa: E501
            'subtype': (DataSubtype,),  # noqa: E501
            'asset_type_name': (str, none_type,),  # noqa: E501
            'type': (str, none_type,),  # noqa: E501
            'enable': (bool,),  # noqa: E501
            'translation': (Translation,),  # noqa: E501
            'unit': (str, none_type,),  # noqa: E501
            'precision': (int, none_type,),  # noqa: E501
            'min': (float, none_type,),  # noqa: E501
            'max': (float, none_type,),  # noqa: E501
            'aggregation_mode': (str, none_type,),  # noqa: E501
            'aggregation_rasters': ([str],),  # noqa: E501
            'viewer': (bool, none_type,),  # noqa: E501
            'ar': (bool, none_type,),  # noqa: E501
            'sequence': (int, none_type,),  # noqa: E501
            'virtual': (bool, none_type,),  # noqa: E501
            'scale': (float, none_type,),  # noqa: E501
            'zero': (float, none_type,),  # noqa: E501
            'map': ([ValueMapping], none_type,),  # noqa: E501
            'source_path': ([str], none_type,),  # noqa: E501
            'is_digital': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'asset_type_name': 'assetTypeName',  # noqa: E501
        'type': 'type',  # noqa: E501
        'enable': 'enable',  # noqa: E501
        'translation': 'translation',  # noqa: E501
        'unit': 'unit',  # noqa: E501
        'precision': 'precision',  # noqa: E501
        'min': 'min',  # noqa: E501
        'max': 'max',  # noqa: E501
        'aggregation_mode': 'aggregationMode',  # noqa: E501
        'aggregation_rasters': 'aggregationRasters',  # noqa: E501
        'viewer': 'viewer',  # noqa: E501
        'ar': 'ar',  # noqa: E501
        'sequence': 'sequence',  # noqa: E501
        'virtual': 'virtual',  # noqa: E501
        'scale': 'scale',  # noqa: E501
        'zero': 'zero',  # noqa: E501
        'map': 'map',  # noqa: E501
        'source_path': 'sourcePath',  # noqa: E501
        'is_digital': 'isDigital',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, subtype, *args, **kwargs):  # noqa: E501
        """AssetTypeAttribute - a model defined in OpenAPI

        Args:
            name (str): Unique key of asset data
            subtype (DataSubtype):

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
            asset_type_name (str, none_type): The unique name for the asset type. [optional]  # noqa: E501
            type (str, none_type): Name of the type for this attribute. [optional]  # noqa: E501
            enable (bool): Is data active or not. [optional] if omitted the server will use the default value of True  # noqa: E501
            translation (Translation): [optional]  # noqa: E501
            unit (str, none_type): Physical unit of numeric data. [optional]  # noqa: E501
            precision (int, none_type): Number of decimal places. [optional]  # noqa: E501
            min (float, none_type): Lower limit. [optional]  # noqa: E501
            max (float, none_type): Upper limit. [optional]  # noqa: E501
            aggregation_mode (str, none_type): Aggregation calculation mode. [optional]  # noqa: E501
            aggregation_rasters ([str]): [optional]  # noqa: E501
            viewer (bool, none_type): Should the attribute be displayed in viewer. [optional] if omitted the server will use the default value of False  # noqa: E501
            ar (bool, none_type): Should the attribute be displayed in AR. [optional] if omitted the server will use the default value of False  # noqa: E501
            sequence (int, none_type): Sequence in AR display. [optional]  # noqa: E501
            virtual (bool, none_type): Is the attribute virtual or not. [optional]  # noqa: E501
            scale (float, none_type): value scale. [optional]  # noqa: E501
            zero (float, none_type): value scale. [optional]  # noqa: E501
            map ([ValueMapping], none_type): list of mapping between value and custom text. [optional]  # noqa: E501
            source_path ([str], none_type): source path for attribute value. [optional]  # noqa: E501
            is_digital (bool, none_type): is attribute digital. [optional]  # noqa: E501
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

        self.name = name
        self.subtype = subtype
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
    def __init__(self, name, subtype, *args, **kwargs):  # noqa: E501
        """AssetTypeAttribute - a model defined in OpenAPI

        Args:
            name (str): Unique key of asset data
            subtype (DataSubtype):

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
            asset_type_name (str, none_type): The unique name for the asset type. [optional]  # noqa: E501
            type (str, none_type): Name of the type for this attribute. [optional]  # noqa: E501
            enable (bool): Is data active or not. [optional] if omitted the server will use the default value of True  # noqa: E501
            translation (Translation): [optional]  # noqa: E501
            unit (str, none_type): Physical unit of numeric data. [optional]  # noqa: E501
            precision (int, none_type): Number of decimal places. [optional]  # noqa: E501
            min (float, none_type): Lower limit. [optional]  # noqa: E501
            max (float, none_type): Upper limit. [optional]  # noqa: E501
            aggregation_mode (str, none_type): Aggregation calculation mode. [optional]  # noqa: E501
            aggregation_rasters ([str]): [optional]  # noqa: E501
            viewer (bool, none_type): Should the attribute be displayed in viewer. [optional] if omitted the server will use the default value of False  # noqa: E501
            ar (bool, none_type): Should the attribute be displayed in AR. [optional] if omitted the server will use the default value of False  # noqa: E501
            sequence (int, none_type): Sequence in AR display. [optional]  # noqa: E501
            virtual (bool, none_type): Is the attribute virtual or not. [optional]  # noqa: E501
            scale (float, none_type): value scale. [optional]  # noqa: E501
            zero (float, none_type): value scale. [optional]  # noqa: E501
            map ([ValueMapping], none_type): list of mapping between value and custom text. [optional]  # noqa: E501
            source_path ([str], none_type): source path for attribute value. [optional]  # noqa: E501
            is_digital (bool, none_type): is attribute digital. [optional]  # noqa: E501
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

        self.name = name
        self.subtype = subtype
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

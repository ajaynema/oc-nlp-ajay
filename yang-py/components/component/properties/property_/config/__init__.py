# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/properties/property/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each property
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__value',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=[six.text_type,YANGBool,RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64),RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64),RestrictedPrecisionDecimalType(precision=2),], is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['components', 'component', 'properties', 'property', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /components/component/properties/property/config/name (string)

    YANG Description: System-supplied name of the property -- this is typically
non-configurable
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /components/component/properties/property/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: System-supplied name of the property -- this is typically
non-configurable
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /components/component/properties/property/config/value (union)

    YANG Description: Property values can take on a variety of types.  Signed and
unsigned integer types may be provided in smaller sizes,
e.g., int8, uint16, etc.
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /components/component/properties/property/config/value (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: Property values can take on a variety of types.  Signed and
unsigned integer types may be provided in smaller sizes,
e.g., int8, uint16, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[six.text_type,YANGBool,RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64),RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64),RestrictedPrecisionDecimalType(precision=2),], is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with union""",
          'defined-type': "openconfig-platform:union",
          'generated-type': """YANGDynClass(base=[six.text_type,YANGBool,RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64),RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64),RestrictedPrecisionDecimalType(precision=2),], is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=[six.text_type,YANGBool,RestrictedClassType(base_type=long, restriction_dict={'range': ['-9223372036854775808..9223372036854775807']}, int_size=64),RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64),RestrictedPrecisionDecimalType(precision=2),], is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  value = __builtin__.property(_get_value, _set_value)


  _pyangbind_elements = OrderedDict([('name', name), ('value', value), ])



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
  from YANG module openconfig-telemetry - based on the path /telemetry-system/sensor-groups/sensor-group/sensor-paths/sensor-path/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters to configure a set
of data model paths as a sensor grouping
  """
  __slots__ = ('_path_helper', '_extmethods', '__path','__exclude_filter',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    self.__exclude_filter = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)

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
      return ['telemetry-system', 'sensor-groups', 'sensor-group', 'sensor-paths', 'sensor-path', 'config']

  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/path (string)

    YANG Description: Path to a section of operational state of interest
(the sensor).
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.

    YANG Description: Path to a section of operational state of interest
(the sensor).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)


  def _get_exclude_filter(self):
    """
    Getter method for exclude_filter, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/exclude_filter (string)

    YANG Description: Filter to exclude certain values out of the state
values
    """
    return self.__exclude_filter
      
  def _set_exclude_filter(self, v, load=False):
    """
    Setter method for exclude_filter, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/exclude_filter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exclude_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exclude_filter() directly.

    YANG Description: Filter to exclude certain values out of the state
values
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exclude_filter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)""",
        })

    self.__exclude_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exclude_filter(self):
    self.__exclude_filter = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)

  path = __builtin__.property(_get_path, _set_path)
  exclude_filter = __builtin__.property(_get_exclude_filter, _set_exclude_filter)


  _pyangbind_elements = OrderedDict([('path', path), ('exclude_filter', exclude_filter), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/sensor-groups/sensor-group/sensor-paths/sensor-path/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters to configure a set
of data model paths as a sensor grouping
  """
  __slots__ = ('_path_helper', '_extmethods', '__path','__exclude_filter',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    self.__exclude_filter = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)

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
      return ['telemetry-system', 'sensor-groups', 'sensor-group', 'sensor-paths', 'sensor-path', 'config']

  def _get_path(self):
    """
    Getter method for path, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/path (string)

    YANG Description: Path to a section of operational state of interest
(the sensor).
    """
    return self.__path
      
  def _set_path(self, v, load=False):
    """
    Setter method for path, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/path (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path() directly.

    YANG Description: Path to a section of operational state of interest
(the sensor).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)""",
        })

    self.__path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path(self):
    self.__path = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)


  def _get_exclude_filter(self):
    """
    Getter method for exclude_filter, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/exclude_filter (string)

    YANG Description: Filter to exclude certain values out of the state
values
    """
    return self.__exclude_filter
      
  def _set_exclude_filter(self, v, load=False):
    """
    Setter method for exclude_filter, mapped from YANG variable /telemetry_system/sensor_groups/sensor_group/sensor_paths/sensor_path/config/exclude_filter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_exclude_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_exclude_filter() directly.

    YANG Description: Filter to exclude certain values out of the state
values
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """exclude_filter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)""",
        })

    self.__exclude_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_exclude_filter(self):
    self.__exclude_filter = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="exclude-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='string', is_config=True)

  path = __builtin__.property(_get_path, _set_path)
  exclude_filter = __builtin__.property(_get_exclude_filter, _set_exclude_filter)


  _pyangbind_elements = OrderedDict([('path', path), ('exclude_filter', exclude_filter), ])



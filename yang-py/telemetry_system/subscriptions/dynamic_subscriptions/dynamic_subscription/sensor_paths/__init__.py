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

from . import sensor_path
class sensor_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/dynamic-subscriptions/dynamic-subscription/sensor-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level container to hold a set of sensor
paths grouped together
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_path',)

  _yang_name = 'sensor-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_path = YANGDynClass(base=YANGListType("path",sensor_path.sensor_path, yang_name="sensor-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path', extensions=None), is_container='list', yang_name="sensor-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=False)

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
      return ['telemetry-system', 'subscriptions', 'dynamic-subscriptions', 'dynamic-subscription', 'sensor-paths']

  def _get_sensor_path(self):
    """
    Getter method for sensor_path, mapped from YANG variable /telemetry_system/subscriptions/dynamic_subscriptions/dynamic_subscription/sensor_paths/sensor_path (list)

    YANG Description: List of paths in the model which together
comprise a sensor grouping. Filters for each path
to exclude items are also provided.
    """
    return self.__sensor_path
      
  def _set_sensor_path(self, v, load=False):
    """
    Setter method for sensor_path, mapped from YANG variable /telemetry_system/subscriptions/dynamic_subscriptions/dynamic_subscription/sensor_paths/sensor_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_path() directly.

    YANG Description: List of paths in the model which together
comprise a sensor grouping. Filters for each path
to exclude items are also provided.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("path",sensor_path.sensor_path, yang_name="sensor-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path', extensions=None), is_container='list', yang_name="sensor-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("path",sensor_path.sensor_path, yang_name="sensor-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path', extensions=None), is_container='list', yang_name="sensor-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=False)""",
        })

    self.__sensor_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_path(self):
    self.__sensor_path = YANGDynClass(base=YANGListType("path",sensor_path.sensor_path, yang_name="sensor-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path', extensions=None), is_container='list', yang_name="sensor-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=False)

  sensor_path = __builtin__.property(_get_sensor_path)


  _pyangbind_elements = OrderedDict([('sensor_path', sensor_path), ])



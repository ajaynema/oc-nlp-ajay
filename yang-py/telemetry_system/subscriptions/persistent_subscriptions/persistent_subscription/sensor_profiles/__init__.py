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

from . import sensor_profile
class sensor_profiles(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions/persistent-subscriptions/persistent-subscription/sensor-profiles. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A sensor profile is a set of sensor groups or
individual sensor paths which are associated with a
telemetry subscription. This is the source of the
telemetry data for the subscription to send to the
defined collectors.
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_profile',)

  _yang_name = 'sensor-profiles'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_profile = YANGDynClass(base=YANGListType("sensor_group",sensor_profile.sensor_profile, yang_name="sensor-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sensor-group', extensions=None), is_container='list', yang_name="sensor-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=True)

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
      return ['telemetry-system', 'subscriptions', 'persistent-subscriptions', 'persistent-subscription', 'sensor-profiles']

  def _get_sensor_profile(self):
    """
    Getter method for sensor_profile, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile (list)

    YANG Description: List of telemetry sensor groups used
in the subscription
    """
    return self.__sensor_profile
      
  def _set_sensor_profile(self, v, load=False):
    """
    Setter method for sensor_profile, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions/persistent_subscription/sensor_profiles/sensor_profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_profile() directly.

    YANG Description: List of telemetry sensor groups used
in the subscription
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sensor_group",sensor_profile.sensor_profile, yang_name="sensor-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sensor-group', extensions=None), is_container='list', yang_name="sensor-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sensor_group",sensor_profile.sensor_profile, yang_name="sensor-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sensor-group', extensions=None), is_container='list', yang_name="sensor-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=True)""",
        })

    self.__sensor_profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_profile(self):
    self.__sensor_profile = YANGDynClass(base=YANGListType("sensor_group",sensor_profile.sensor_profile, yang_name="sensor-profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sensor-group', extensions=None), is_container='list', yang_name="sensor-profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='list', is_config=True)

  sensor_profile = __builtin__.property(_get_sensor_profile, _set_sensor_profile)


  _pyangbind_elements = OrderedDict([('sensor_profile', sensor_profile), ])


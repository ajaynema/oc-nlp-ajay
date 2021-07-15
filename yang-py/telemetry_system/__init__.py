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

from . import sensor_groups
from . import destination_groups
from . import subscriptions
class telemetry_system(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level configuration and state for the
device's telemetry system.
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_groups','__destination_groups','__subscriptions',)

  _yang_name = 'telemetry-system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_groups = YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__subscriptions = YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system']

  def _get_sensor_groups(self):
    """
    Getter method for sensor_groups, mapped from YANG variable /telemetry_system/sensor_groups (container)

    YANG Description: Top level container for sensor-groups.
    """
    return self.__sensor_groups
      
  def _set_sensor_groups(self, v, load=False):
    """
    Setter method for sensor_groups, mapped from YANG variable /telemetry_system/sensor_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_groups() directly.

    YANG Description: Top level container for sensor-groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__sensor_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_groups(self):
    self.__sensor_groups = YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destination_groups(self):
    """
    Getter method for destination_groups, mapped from YANG variable /telemetry_system/destination_groups (container)

    YANG Description: Top level container for destination group configuration
and state.
    """
    return self.__destination_groups
      
  def _set_destination_groups(self, v, load=False):
    """
    Setter method for destination_groups, mapped from YANG variable /telemetry_system/destination_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_groups() directly.

    YANG Description: Top level container for destination group configuration
and state.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destination_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_groups(self):
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_subscriptions(self):
    """
    Getter method for subscriptions, mapped from YANG variable /telemetry_system/subscriptions (container)

    YANG Description: This container holds information for both persistent
and dynamic telemetry subscriptions.
    """
    return self.__subscriptions
      
  def _set_subscriptions(self, v, load=False):
    """
    Setter method for subscriptions, mapped from YANG variable /telemetry_system/subscriptions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscriptions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscriptions() directly.

    YANG Description: This container holds information for both persistent
and dynamic telemetry subscriptions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscriptions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__subscriptions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscriptions(self):
    self.__subscriptions = YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  sensor_groups = __builtin__.property(_get_sensor_groups, _set_sensor_groups)
  destination_groups = __builtin__.property(_get_destination_groups, _set_destination_groups)
  subscriptions = __builtin__.property(_get_subscriptions, _set_subscriptions)


  _pyangbind_elements = OrderedDict([('sensor_groups', sensor_groups), ('destination_groups', destination_groups), ('subscriptions', subscriptions), ])


from . import sensor_groups
from . import destination_groups
from . import subscriptions
class telemetry_system(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level configuration and state for the
device's telemetry system.
  """
  __slots__ = ('_path_helper', '_extmethods', '__sensor_groups','__destination_groups','__subscriptions',)

  _yang_name = 'telemetry-system'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sensor_groups = YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__subscriptions = YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system']

  def _get_sensor_groups(self):
    """
    Getter method for sensor_groups, mapped from YANG variable /telemetry_system/sensor_groups (container)

    YANG Description: Top level container for sensor-groups.
    """
    return self.__sensor_groups
      
  def _set_sensor_groups(self, v, load=False):
    """
    Setter method for sensor_groups, mapped from YANG variable /telemetry_system/sensor_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sensor_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sensor_groups() directly.

    YANG Description: Top level container for sensor-groups.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sensor_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__sensor_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sensor_groups(self):
    self.__sensor_groups = YANGDynClass(base=sensor_groups.sensor_groups, is_container='container', yang_name="sensor-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destination_groups(self):
    """
    Getter method for destination_groups, mapped from YANG variable /telemetry_system/destination_groups (container)

    YANG Description: Top level container for destination group configuration
and state.
    """
    return self.__destination_groups
      
  def _set_destination_groups(self, v, load=False):
    """
    Setter method for destination_groups, mapped from YANG variable /telemetry_system/destination_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination_groups() directly.

    YANG Description: Top level container for destination group configuration
and state.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destination_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination_groups(self):
    self.__destination_groups = YANGDynClass(base=destination_groups.destination_groups, is_container='container', yang_name="destination-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_subscriptions(self):
    """
    Getter method for subscriptions, mapped from YANG variable /telemetry_system/subscriptions (container)

    YANG Description: This container holds information for both persistent
and dynamic telemetry subscriptions.
    """
    return self.__subscriptions
      
  def _set_subscriptions(self, v, load=False):
    """
    Setter method for subscriptions, mapped from YANG variable /telemetry_system/subscriptions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subscriptions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subscriptions() directly.

    YANG Description: This container holds information for both persistent
and dynamic telemetry subscriptions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subscriptions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__subscriptions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subscriptions(self):
    self.__subscriptions = YANGDynClass(base=subscriptions.subscriptions, is_container='container', yang_name="subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  sensor_groups = __builtin__.property(_get_sensor_groups, _set_sensor_groups)
  destination_groups = __builtin__.property(_get_destination_groups, _set_destination_groups)
  subscriptions = __builtin__.property(_get_subscriptions, _set_subscriptions)


  _pyangbind_elements = OrderedDict([('sensor_groups', sensor_groups), ('destination_groups', destination_groups), ('subscriptions', subscriptions), ])



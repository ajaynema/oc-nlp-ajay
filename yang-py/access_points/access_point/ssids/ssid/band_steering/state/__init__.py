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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/band-steering/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for band-steering state elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__band_steering','__steering_rssi',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__band_steering = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    self.__steering_rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'band-steering', 'state']

  def _get_band_steering(self):
    """
    Getter method for band_steering, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/band_steering (boolean)

    YANG Description: Enable/disable band-steering.
    """
    return self.__band_steering
      
  def _set_band_steering(self, v, load=False):
    """
    Setter method for band_steering, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/band_steering (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_band_steering is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_band_steering() directly.

    YANG Description: Enable/disable band-steering.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """band_steering must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)""",
        })

    self.__band_steering = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_band_steering(self):
    self.__band_steering = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)


  def _get_steering_rssi(self):
    """
    Getter method for steering_rssi, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/steering_rssi (int8)

    YANG Description: Minimum RSSI a dual-band Station's Probe Request
must be heard at on a 5GHz radio, in order for
band-steering to withhold 2.4GHz Probe Responses.
    """
    return self.__steering_rssi
      
  def _set_steering_rssi(self, v, load=False):
    """
    Setter method for steering_rssi, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/steering_rssi (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_steering_rssi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_steering_rssi() directly.

    YANG Description: Minimum RSSI a dual-band Station's Probe Request
must be heard at on a 5GHz radio, in order for
band-steering to withhold 2.4GHz Probe Responses.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """steering_rssi must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)""",
        })

    self.__steering_rssi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_steering_rssi(self):
    self.__steering_rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)

  band_steering = __builtin__.property(_get_band_steering)
  steering_rssi = __builtin__.property(_get_steering_rssi)


  _pyangbind_elements = OrderedDict([('band_steering', band_steering), ('steering_rssi', steering_rssi), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/band-steering/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for band-steering state elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__band_steering','__steering_rssi',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__band_steering = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    self.__steering_rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'band-steering', 'state']

  def _get_band_steering(self):
    """
    Getter method for band_steering, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/band_steering (boolean)

    YANG Description: Enable/disable band-steering.
    """
    return self.__band_steering
      
  def _set_band_steering(self, v, load=False):
    """
    Setter method for band_steering, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/band_steering (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_band_steering is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_band_steering() directly.

    YANG Description: Enable/disable band-steering.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """band_steering must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)""",
        })

    self.__band_steering = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_band_steering(self):
    self.__band_steering = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="band-steering", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)


  def _get_steering_rssi(self):
    """
    Getter method for steering_rssi, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/steering_rssi (int8)

    YANG Description: Minimum RSSI a dual-band Station's Probe Request
must be heard at on a 5GHz radio, in order for
band-steering to withhold 2.4GHz Probe Responses.
    """
    return self.__steering_rssi
      
  def _set_steering_rssi(self, v, load=False):
    """
    Setter method for steering_rssi, mapped from YANG variable /access_points/access_point/ssids/ssid/band_steering/state/steering_rssi (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_steering_rssi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_steering_rssi() directly.

    YANG Description: Minimum RSSI a dual-band Station's Probe Request
must be heard at on a 5GHz radio, in order for
band-steering to withhold 2.4GHz Probe Responses.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """steering_rssi must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)""",
        })

    self.__steering_rssi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_steering_rssi(self):
    self.__steering_rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="steering-rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)

  band_steering = __builtin__.property(_get_band_steering)
  steering_rssi = __builtin__.property(_get_steering_rssi)


  _pyangbind_elements = OrderedDict([('band_steering', band_steering), ('steering_rssi', steering_rssi), ])



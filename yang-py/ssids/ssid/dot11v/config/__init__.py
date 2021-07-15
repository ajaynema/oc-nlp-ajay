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
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/dot11v/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for 802.11v configuration elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__dot11v_dms','__dot11v_bssidle','__dot11v_bssidle_timeout','__dot11v_bsstransition',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dot11v_dms = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-dms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    self.__dot11v_bssidle = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bssidle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    self.__dot11v_bssidle_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11v-bssidle-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint16', is_config=True)
    self.__dot11v_bsstransition = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bsstransition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)

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
      return ['ssids', 'ssid', 'dot11v', 'config']

  def _get_dot11v_dms(self):
    """
    Getter method for dot11v_dms, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_dms (boolean)

    YANG Description: 802.11v Directed Multicast Service enabled/disabled.
    """
    return self.__dot11v_dms
      
  def _set_dot11v_dms(self, v, load=False):
    """
    Setter method for dot11v_dms, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_dms (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11v_dms is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11v_dms() directly.

    YANG Description: 802.11v Directed Multicast Service enabled/disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot11v-dms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11v_dms must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-dms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)""",
        })

    self.__dot11v_dms = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11v_dms(self):
    self.__dot11v_dms = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-dms", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)


  def _get_dot11v_bssidle(self):
    """
    Getter method for dot11v_bssidle, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bssidle (boolean)

    YANG Description: 802.11v BSS Max Idle enabled/disabled.
    """
    return self.__dot11v_bssidle
      
  def _set_dot11v_bssidle(self, v, load=False):
    """
    Setter method for dot11v_bssidle, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bssidle (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11v_bssidle is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11v_bssidle() directly.

    YANG Description: 802.11v BSS Max Idle enabled/disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot11v-bssidle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11v_bssidle must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bssidle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)""",
        })

    self.__dot11v_bssidle = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11v_bssidle(self):
    self.__dot11v_bssidle = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bssidle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)


  def _get_dot11v_bssidle_timeout(self):
    """
    Getter method for dot11v_bssidle_timeout, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bssidle_timeout (uint16)

    YANG Description: 802.11v BSS Max Idle timeout.
    """
    return self.__dot11v_bssidle_timeout
      
  def _set_dot11v_bssidle_timeout(self, v, load=False):
    """
    Setter method for dot11v_bssidle_timeout, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bssidle_timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11v_bssidle_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11v_bssidle_timeout() directly.

    YANG Description: 802.11v BSS Max Idle timeout.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11v-bssidle-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11v_bssidle_timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11v-bssidle-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint16', is_config=True)""",
        })

    self.__dot11v_bssidle_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11v_bssidle_timeout(self):
    self.__dot11v_bssidle_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11v-bssidle-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint16', is_config=True)


  def _get_dot11v_bsstransition(self):
    """
    Getter method for dot11v_bsstransition, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bsstransition (boolean)

    YANG Description: 802.11v BSS Transition enabled/disabled.
    """
    return self.__dot11v_bsstransition
      
  def _set_dot11v_bsstransition(self, v, load=False):
    """
    Setter method for dot11v_bsstransition, mapped from YANG variable /ssids/ssid/dot11v/config/dot11v_bsstransition (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11v_bsstransition is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11v_bsstransition() directly.

    YANG Description: 802.11v BSS Transition enabled/disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot11v-bsstransition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11v_bsstransition must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bsstransition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)""",
        })

    self.__dot11v_bsstransition = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11v_bsstransition(self):
    self.__dot11v_bsstransition = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11v-bsstransition", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)

  dot11v_dms = __builtin__.property(_get_dot11v_dms, _set_dot11v_dms)
  dot11v_bssidle = __builtin__.property(_get_dot11v_bssidle, _set_dot11v_bssidle)
  dot11v_bssidle_timeout = __builtin__.property(_get_dot11v_bssidle_timeout, _set_dot11v_bssidle_timeout)
  dot11v_bsstransition = __builtin__.property(_get_dot11v_bsstransition, _set_dot11v_bsstransition)


  _pyangbind_elements = OrderedDict([('dot11v_dms', dot11v_dms), ('dot11v_bssidle', dot11v_bssidle), ('dot11v_bssidle_timeout', dot11v_bssidle_timeout), ('dot11v_bsstransition', dot11v_bsstransition), ])



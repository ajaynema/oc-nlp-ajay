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

class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wifi-phy - based on the path /radios/radio/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A collection of radio-related statistics objects.
  """
  __slots__ = ('_path_helper', '_extmethods', '__failed_fcs_frames','__noise_floor',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__failed_fcs_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)
    self.__noise_floor = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)

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
      return ['radios', 'radio', 'state', 'counters']

  def _get_failed_fcs_frames(self):
    """
    Getter method for failed_fcs_frames, mapped from YANG variable /radios/radio/state/counters/failed_fcs_frames (oc-yang:counter64)

    YANG Description: Number of frames that failed the FCS
    """
    return self.__failed_fcs_frames
      
  def _set_failed_fcs_frames(self, v, load=False):
    """
    Setter method for failed_fcs_frames, mapped from YANG variable /radios/radio/state/counters/failed_fcs_frames (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_failed_fcs_frames is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_failed_fcs_frames() directly.

    YANG Description: Number of frames that failed the FCS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """failed_fcs_frames must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__failed_fcs_frames = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_failed_fcs_frames(self):
    self.__failed_fcs_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)


  def _get_noise_floor(self):
    """
    Getter method for noise_floor, mapped from YANG variable /radios/radio/state/counters/noise_floor (int8)

    YANG Description: Noise Floor, as measured by this radio.
    """
    return self.__noise_floor
      
  def _set_noise_floor(self, v, load=False):
    """
    Setter method for noise_floor, mapped from YANG variable /radios/radio/state/counters/noise_floor (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_noise_floor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_noise_floor() directly.

    YANG Description: Noise Floor, as measured by this radio.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """noise_floor must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)""",
        })

    self.__noise_floor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_noise_floor(self):
    self.__noise_floor = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)

  failed_fcs_frames = __builtin__.property(_get_failed_fcs_frames)
  noise_floor = __builtin__.property(_get_noise_floor)


  _pyangbind_elements = OrderedDict([('failed_fcs_frames', failed_fcs_frames), ('noise_floor', noise_floor), ])


class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wifi-phy - based on the path /radios/radio/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A collection of radio-related statistics objects.
  """
  __slots__ = ('_path_helper', '_extmethods', '__failed_fcs_frames','__noise_floor',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__failed_fcs_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)
    self.__noise_floor = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)

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
      return ['radios', 'radio', 'state', 'counters']

  def _get_failed_fcs_frames(self):
    """
    Getter method for failed_fcs_frames, mapped from YANG variable /radios/radio/state/counters/failed_fcs_frames (oc-yang:counter64)

    YANG Description: Number of frames that failed the FCS
    """
    return self.__failed_fcs_frames
      
  def _set_failed_fcs_frames(self, v, load=False):
    """
    Setter method for failed_fcs_frames, mapped from YANG variable /radios/radio/state/counters/failed_fcs_frames (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_failed_fcs_frames is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_failed_fcs_frames() directly.

    YANG Description: Number of frames that failed the FCS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """failed_fcs_frames must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__failed_fcs_frames = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_failed_fcs_frames(self):
    self.__failed_fcs_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="failed-fcs-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='oc-yang:counter64', is_config=False)


  def _get_noise_floor(self):
    """
    Getter method for noise_floor, mapped from YANG variable /radios/radio/state/counters/noise_floor (int8)

    YANG Description: Noise Floor, as measured by this radio.
    """
    return self.__noise_floor
      
  def _set_noise_floor(self, v, load=False):
    """
    Setter method for noise_floor, mapped from YANG variable /radios/radio/state/counters/noise_floor (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_noise_floor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_noise_floor() directly.

    YANG Description: Noise Floor, as measured by this radio.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """noise_floor must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)""",
        })

    self.__noise_floor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_noise_floor(self):
    self.__noise_floor = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="noise-floor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-phy', defining_module='openconfig-wifi-phy', yang_type='int8', is_config=False)

  failed_fcs_frames = __builtin__.property(_get_failed_fcs_frames)
  noise_floor = __builtin__.property(_get_noise_floor)


  _pyangbind_elements = OrderedDict([('failed_fcs_frames', failed_fcs_frames), ('noise_floor', noise_floor), ])



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

class in_distribution(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/state/counters/in-distribution. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The size distribution of the received frames.
  """
  __slots__ = ('_path_helper', '_extmethods', '__in_frames_64_octets','__in_frames_65_127_octets','__in_frames_128_255_octets','__in_frames_256_511_octets','__in_frames_512_1023_octets','__in_frames_1024_1518_octets',)

  _yang_name = 'in-distribution'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__in_frames_64_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-64-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    self.__in_frames_65_127_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-65-127-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    self.__in_frames_128_255_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-128-255-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    self.__in_frames_256_511_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-256-511-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    self.__in_frames_512_1023_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-512-1023-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    self.__in_frames_1024_1518_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-1024-1518-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)

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
      return ['interfaces', 'interface', 'ethernet', 'state', 'counters', 'in-distribution']

  def _get_in_frames_64_octets(self):
    """
    Getter method for in_frames_64_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_64_octets (oc-yang:counter64)

    YANG Description: Number of packets (including bad packets) received that
were 64 bytes in length (excluding framing bits but
including FCS bytes).
    """
    return self.__in_frames_64_octets
      
  def _set_in_frames_64_octets(self, v, load=False):
    """
    Setter method for in_frames_64_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_64_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_64_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_64_octets() directly.

    YANG Description: Number of packets (including bad packets) received that
were 64 bytes in length (excluding framing bits but
including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-64-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_64_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-64-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_64_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_64_octets(self):
    self.__in_frames_64_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-64-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_frames_65_127_octets(self):
    """
    Getter method for in_frames_65_127_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_65_127_octets (oc-yang:counter64)

    YANG Description: Number of good and bad packets received that were
between 65 and 127 bytes in length (excluding framing bits
but including FCS bytes).
    """
    return self.__in_frames_65_127_octets
      
  def _set_in_frames_65_127_octets(self, v, load=False):
    """
    Setter method for in_frames_65_127_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_65_127_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_65_127_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_65_127_octets() directly.

    YANG Description: Number of good and bad packets received that were
between 65 and 127 bytes in length (excluding framing bits
but including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-65-127-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_65_127_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-65-127-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_65_127_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_65_127_octets(self):
    self.__in_frames_65_127_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-65-127-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_frames_128_255_octets(self):
    """
    Getter method for in_frames_128_255_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_128_255_octets (oc-yang:counter64)

    YANG Description: Number of good and bad packets received that were
between 128 and 255 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    return self.__in_frames_128_255_octets
      
  def _set_in_frames_128_255_octets(self, v, load=False):
    """
    Setter method for in_frames_128_255_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_128_255_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_128_255_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_128_255_octets() directly.

    YANG Description: Number of good and bad packets received that were
between 128 and 255 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-128-255-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_128_255_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-128-255-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_128_255_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_128_255_octets(self):
    self.__in_frames_128_255_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-128-255-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_frames_256_511_octets(self):
    """
    Getter method for in_frames_256_511_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_256_511_octets (oc-yang:counter64)

    YANG Description: Number of good and bad packets received that were
between 256 and 511 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    return self.__in_frames_256_511_octets
      
  def _set_in_frames_256_511_octets(self, v, load=False):
    """
    Setter method for in_frames_256_511_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_256_511_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_256_511_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_256_511_octets() directly.

    YANG Description: Number of good and bad packets received that were
between 256 and 511 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-256-511-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_256_511_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-256-511-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_256_511_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_256_511_octets(self):
    self.__in_frames_256_511_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-256-511-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_frames_512_1023_octets(self):
    """
    Getter method for in_frames_512_1023_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_512_1023_octets (oc-yang:counter64)

    YANG Description: Number of good and bad packets received that were
between 512 and 1023 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    return self.__in_frames_512_1023_octets
      
  def _set_in_frames_512_1023_octets(self, v, load=False):
    """
    Setter method for in_frames_512_1023_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_512_1023_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_512_1023_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_512_1023_octets() directly.

    YANG Description: Number of good and bad packets received that were
between 512 and 1023 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-512-1023-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_512_1023_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-512-1023-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_512_1023_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_512_1023_octets(self):
    self.__in_frames_512_1023_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-512-1023-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)


  def _get_in_frames_1024_1518_octets(self):
    """
    Getter method for in_frames_1024_1518_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_1024_1518_octets (oc-yang:counter64)

    YANG Description: Number of good and bad packets received that were
between 1024 and 1518 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    return self.__in_frames_1024_1518_octets
      
  def _set_in_frames_1024_1518_octets(self, v, load=False):
    """
    Setter method for in_frames_1024_1518_octets, mapped from YANG variable /interfaces/interface/ethernet/state/counters/in_distribution/in_frames_1024_1518_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_frames_1024_1518_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_frames_1024_1518_octets() directly.

    YANG Description: Number of good and bad packets received that were
between 1024 and 1518 bytes in length inclusive
(excluding framing bits but including FCS bytes).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-1024-1518-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_frames_1024_1518_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-1024-1518-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__in_frames_1024_1518_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_frames_1024_1518_octets(self):
    self.__in_frames_1024_1518_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-frames-1024-1518-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ethernet-ext', defining_module='openconfig-if-ethernet-ext', yang_type='oc-yang:counter64', is_config=False)

  in_frames_64_octets = __builtin__.property(_get_in_frames_64_octets)
  in_frames_65_127_octets = __builtin__.property(_get_in_frames_65_127_octets)
  in_frames_128_255_octets = __builtin__.property(_get_in_frames_128_255_octets)
  in_frames_256_511_octets = __builtin__.property(_get_in_frames_256_511_octets)
  in_frames_512_1023_octets = __builtin__.property(_get_in_frames_512_1023_octets)
  in_frames_1024_1518_octets = __builtin__.property(_get_in_frames_1024_1518_octets)


  _pyangbind_elements = OrderedDict([('in_frames_64_octets', in_frames_64_octets), ('in_frames_65_127_octets', in_frames_65_127_octets), ('in_frames_128_255_octets', in_frames_128_255_octets), ('in_frames_256_511_octets', in_frames_256_511_octets), ('in_frames_512_1023_octets', in_frames_512_1023_octets), ('in_frames_1024_1518_octets', in_frames_1024_1518_octets), ])



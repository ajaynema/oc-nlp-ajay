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

class rx_data_wmm(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/bssids/bssid/state/counters/rx-data-wmm. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Received 802.11 Data frames, per WMM Access Category.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vi','__vo','__be','__bk',)

  _yang_name = 'rx-data-wmm'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__vo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__be = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__bk = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'bssids', 'bssid', 'state', 'counters', 'rx-data-wmm']

  def _get_vi(self):
    """
    Getter method for vi, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vi (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Video.
    """
    return self.__vi
      
  def _set_vi(self, v, load=False):
    """
    Setter method for vi, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vi (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vi() directly.

    YANG Description: Rx Data frames marked as Access Category Video.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vi must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__vi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vi(self):
    self.__vi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_vo(self):
    """
    Getter method for vo, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vo (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Voice.
    """
    return self.__vo
      
  def _set_vo(self, v, load=False):
    """
    Setter method for vo, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vo (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vo() directly.

    YANG Description: Rx Data frames marked as Access Category Voice.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vo must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__vo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vo(self):
    self.__vo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_be(self):
    """
    Getter method for be, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/be (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Best Effort.
    """
    return self.__be
      
  def _set_be(self, v, load=False):
    """
    Setter method for be, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/be (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_be is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_be() directly.

    YANG Description: Rx Data frames marked as Access Category Best Effort.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """be must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__be = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_be(self):
    self.__be = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_bk(self):
    """
    Getter method for bk, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/bk (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Background.
    """
    return self.__bk
      
  def _set_bk(self, v, load=False):
    """
    Setter method for bk, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/bk (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bk() directly.

    YANG Description: Rx Data frames marked as Access Category Background.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bk must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__bk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bk(self):
    self.__bk = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

  vi = __builtin__.property(_get_vi)
  vo = __builtin__.property(_get_vo)
  be = __builtin__.property(_get_be)
  bk = __builtin__.property(_get_bk)


  _pyangbind_elements = OrderedDict([('vi', vi), ('vo', vo), ('be', be), ('bk', bk), ])


class rx_data_wmm(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/bssids/bssid/state/counters/rx-data-wmm. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Received 802.11 Data frames, per WMM Access Category.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vi','__vo','__be','__bk',)

  _yang_name = 'rx-data-wmm'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__vo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__be = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__bk = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'bssids', 'bssid', 'state', 'counters', 'rx-data-wmm']

  def _get_vi(self):
    """
    Getter method for vi, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vi (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Video.
    """
    return self.__vi
      
  def _set_vi(self, v, load=False):
    """
    Setter method for vi, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vi (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vi() directly.

    YANG Description: Rx Data frames marked as Access Category Video.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vi must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__vi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vi(self):
    self.__vi = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_vo(self):
    """
    Getter method for vo, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vo (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Voice.
    """
    return self.__vo
      
  def _set_vo(self, v, load=False):
    """
    Setter method for vo, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/vo (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vo is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vo() directly.

    YANG Description: Rx Data frames marked as Access Category Voice.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vo must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__vo = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vo(self):
    self.__vo = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="vo", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_be(self):
    """
    Getter method for be, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/be (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Best Effort.
    """
    return self.__be
      
  def _set_be(self, v, load=False):
    """
    Setter method for be, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/be (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_be is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_be() directly.

    YANG Description: Rx Data frames marked as Access Category Best Effort.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """be must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__be = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_be(self):
    self.__be = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="be", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_bk(self):
    """
    Getter method for bk, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/bk (oc-yang:counter64)

    YANG Description: Rx Data frames marked as Access Category Background.
    """
    return self.__bk
      
  def _set_bk(self, v, load=False):
    """
    Setter method for bk, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid/state/counters/rx_data_wmm/bk (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bk() directly.

    YANG Description: Rx Data frames marked as Access Category Background.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bk must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__bk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bk(self):
    self.__bk = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

  vi = __builtin__.property(_get_vi)
  vo = __builtin__.property(_get_vo)
  be = __builtin__.property(_get_be)
  bk = __builtin__.property(_get_bk)


  _pyangbind_elements = OrderedDict([('vi', vi), ('vo', vo), ('be', be), ('bk', bk), ])



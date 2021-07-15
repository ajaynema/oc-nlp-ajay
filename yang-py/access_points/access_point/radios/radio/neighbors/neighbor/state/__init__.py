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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/radios/radio/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State container for RF neighbors.
  """
  __slots__ = ('_path_helper', '_extmethods', '__bssid','__ssid','__rssi','__channel','__primary_channel','__last_seen','__opmode',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bssid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)
    self.__ssid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)
    self.__rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)
    self.__channel = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    self.__primary_channel = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="primary-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    self.__last_seen = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-seen", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:timeticks64', is_config=False)
    self.__opmode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OPEN': {}, 'WPA2_PERSONAL': {}, 'WPA2_ENTERPRISE': {}, 'WPA_PERSONAL': {}, 'WPA_ENTERPRISE': {}, 'WEP': {}},), is_leaf=True, yang_name="opmode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)

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
      return ['access-points', 'access-point', 'radios', 'radio', 'neighbors', 'neighbor', 'state']

  def _get_bssid(self):
    """
    Getter method for bssid, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/bssid (oc-yang:mac-address)

    YANG Description: Neighboring BSSID.
    """
    return self.__bssid
      
  def _set_bssid(self, v, load=False):
    """
    Setter method for bssid, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/bssid (oc-yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bssid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bssid() directly.

    YANG Description: Neighboring BSSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bssid must be of a type compatible with oc-yang:mac-address""",
          'defined-type': "oc-yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)""",
        })

    self.__bssid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bssid(self):
    self.__bssid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:mac-address', is_config=False)


  def _get_ssid(self):
    """
    Getter method for ssid, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/ssid (string)

    YANG Description: The SSID of this neighboring BSSID.
    """
    return self.__ssid
      
  def _set_ssid(self, v, load=False):
    """
    Setter method for ssid, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/ssid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssid() directly.

    YANG Description: The SSID of this neighboring BSSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="ssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)""",
        })

    self.__ssid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssid(self):
    self.__ssid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)


  def _get_rssi(self):
    """
    Getter method for rssi, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/rssi (int8)

    YANG Description: The RSSI of this neighboring BSSID.
    """
    return self.__rssi
      
  def _set_rssi(self, v, load=False):
    """
    Setter method for rssi, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/rssi (int8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rssi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rssi() directly.

    YANG Description: The RSSI of this neighboring BSSID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rssi must be of a type compatible with int8""",
          'defined-type': "int8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)""",
        })

    self.__rssi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rssi(self):
    self.__rssi = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['-128..127']}, int_size=8), is_leaf=True, yang_name="rssi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='int8', is_config=False)


  def _get_channel(self):
    """
    Getter method for channel, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/channel (uint16)

    YANG Description: The channel of this neighboring BSSID. This is to utilize
802.11ac nomenclature. For example, 40MHz channel 36-40
represented as channel 38. The primary-channel leaf is used to
identify the primary 20MHz channel of a bonded channel.
    """
    return self.__channel
      
  def _set_channel(self, v, load=False):
    """
    Setter method for channel, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/channel (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_channel() directly.

    YANG Description: The channel of this neighboring BSSID. This is to utilize
802.11ac nomenclature. For example, 40MHz channel 36-40
represented as channel 38. The primary-channel leaf is used to
identify the primary 20MHz channel of a bonded channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """channel must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_channel(self):
    self.__channel = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)


  def _get_primary_channel(self):
    """
    Getter method for primary_channel, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/primary_channel (uint16)

    YANG Description: The primary 20MHz channel, if the neighbor is operating on
bonded channel.
    """
    return self.__primary_channel
      
  def _set_primary_channel(self, v, load=False):
    """
    Setter method for primary_channel, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/primary_channel (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_primary_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_primary_channel() directly.

    YANG Description: The primary 20MHz channel, if the neighbor is operating on
bonded channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="primary-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """primary_channel must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="primary-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__primary_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_primary_channel(self):
    self.__primary_channel = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="primary-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)


  def _get_last_seen(self):
    """
    Getter method for last_seen, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/last_seen (oc-types:timeticks64)

    YANG Description: Reports the time this reading was taken, indicating when
this neighbor was last seen. If a cache is used, it MUST be
updated instantly when a neighbor BSS changes channels, or a
new BSS is seen. The value is the timestamp in nanoseconds
relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    return self.__last_seen
      
  def _set_last_seen(self, v, load=False):
    """
    Setter method for last_seen, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/last_seen (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_seen is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_seen() directly.

    YANG Description: Reports the time this reading was taken, indicating when
this neighbor was last seen. If a cache is used, it MUST be
updated instantly when a neighbor BSS changes channels, or a
new BSS is seen. The value is the timestamp in nanoseconds
relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-seen", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_seen must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-seen", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__last_seen = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_seen(self):
    self.__last_seen = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-seen", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-types:timeticks64', is_config=False)


  def _get_opmode(self):
    """
    Getter method for opmode, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/opmode (enumeration)

    YANG Description: Operating mode of the BSS.
    """
    return self.__opmode
      
  def _set_opmode(self, v, load=False):
    """
    Setter method for opmode, mapped from YANG variable /access_points/access_point/radios/radio/neighbors/neighbor/state/opmode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_opmode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_opmode() directly.

    YANG Description: Operating mode of the BSS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OPEN': {}, 'WPA2_PERSONAL': {}, 'WPA2_ENTERPRISE': {}, 'WPA_PERSONAL': {}, 'WPA_ENTERPRISE': {}, 'WEP': {}},), is_leaf=True, yang_name="opmode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """opmode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-access-points:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OPEN': {}, 'WPA2_PERSONAL': {}, 'WPA2_ENTERPRISE': {}, 'WPA_PERSONAL': {}, 'WPA_ENTERPRISE': {}, 'WEP': {}},), is_leaf=True, yang_name="opmode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)""",
        })

    self.__opmode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_opmode(self):
    self.__opmode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OPEN': {}, 'WPA2_PERSONAL': {}, 'WPA2_ENTERPRISE': {}, 'WPA_PERSONAL': {}, 'WPA_ENTERPRISE': {}, 'WEP': {}},), is_leaf=True, yang_name="opmode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)

  bssid = __builtin__.property(_get_bssid)
  ssid = __builtin__.property(_get_ssid)
  rssi = __builtin__.property(_get_rssi)
  channel = __builtin__.property(_get_channel)
  primary_channel = __builtin__.property(_get_primary_channel)
  last_seen = __builtin__.property(_get_last_seen)
  opmode = __builtin__.property(_get_opmode)


  _pyangbind_elements = OrderedDict([('bssid', bssid), ('ssid', ssid), ('rssi', rssi), ('channel', channel), ('primary_channel', primary_channel), ('last_seen', last_seen), ('opmode', opmode), ])



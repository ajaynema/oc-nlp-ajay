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
  from YANG module openconfig-acl - based on the path /acl/acl-sets/acl-set/acl-entries/acl-entry/mpls/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to fields within
the MPLS header.
  """
  __slots__ = ('_path_helper', '_extmethods', '__traffic_class','__start_label_value','__end_label_value','__ttl_value',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-tc', is_config=True)
    self.__start_label_value = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="start-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)
    self.__end_label_value = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="end-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)
    self.__ttl_value = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="ttl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint8', is_config=True)

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
      return ['acl', 'acl-sets', 'acl-set', 'acl-entries', 'acl-entry', 'mpls', 'config']

  def _get_traffic_class(self):
    """
    Getter method for traffic_class, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/traffic_class (oc-mpls:mpls-tc)

    YANG Description: The value of the MPLS traffic class (TC) bits,
formerly known as the EXP bits.
    """
    return self.__traffic_class
      
  def _set_traffic_class(self, v, load=False):
    """
    Setter method for traffic_class, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/traffic_class (oc-mpls:mpls-tc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_traffic_class() directly.

    YANG Description: The value of the MPLS traffic class (TC) bits,
formerly known as the EXP bits.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-tc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """traffic_class must be of a type compatible with oc-mpls:mpls-tc""",
          'defined-type': "oc-mpls:mpls-tc",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-tc', is_config=True)""",
        })

    self.__traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_traffic_class(self):
    self.__traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..7']}), is_leaf=True, yang_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-tc', is_config=True)


  def _get_start_label_value(self):
    """
    Getter method for start_label_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/start_label_value (oc-mpls:mpls-label)

    YANG Description: Match MPLS label value on the MPLS header.
The usage of this field indicated the upper
range value in the top of the stack.
The range that is used is inclusive. The match that
is done for a particular received pkt_label is:
start-label-value <= pkt_label <= end-label-value.
The 20-bit label value in an MPLS label
stack as specified in RFC 3032.
This label value does not include the
encodings of Traffic Class and TTL.
    """
    return self.__start_label_value
      
  def _set_start_label_value(self, v, load=False):
    """
    Setter method for start_label_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/start_label_value (oc-mpls:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_label_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_label_value() directly.

    YANG Description: Match MPLS label value on the MPLS header.
The usage of this field indicated the upper
range value in the top of the stack.
The range that is used is inclusive. The match that
is done for a particular received pkt_label is:
start-label-value <= pkt_label <= end-label-value.
The 20-bit label value in an MPLS label
stack as specified in RFC 3032.
This label value does not include the
encodings of Traffic Class and TTL.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="start-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_label_value must be of a type compatible with oc-mpls:mpls-label""",
          'defined-type': "oc-mpls:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="start-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)""",
        })

    self.__start_label_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_label_value(self):
    self.__start_label_value = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="start-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)


  def _get_end_label_value(self):
    """
    Getter method for end_label_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/end_label_value (oc-mpls:mpls-label)

    YANG Description: Match MPLS label value on the MPLS header.
The usage of this field indicated the upper
range value in the top of the stack.
The range that is used is inclusive. The match that
is done for a particular received pkt_label is:
start-label-value <= pkt_label <= end-label-value.
The 20-bit label value in an MPLS label
stack as specified in RFC 3032.
This label value does not include the
encodings of Traffic Class and TTL.
    """
    return self.__end_label_value
      
  def _set_end_label_value(self, v, load=False):
    """
    Setter method for end_label_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/end_label_value (oc-mpls:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_end_label_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_end_label_value() directly.

    YANG Description: Match MPLS label value on the MPLS header.
The usage of this field indicated the upper
range value in the top of the stack.
The range that is used is inclusive. The match that
is done for a particular received pkt_label is:
start-label-value <= pkt_label <= end-label-value.
The 20-bit label value in an MPLS label
stack as specified in RFC 3032.
This label value does not include the
encodings of Traffic Class and TTL.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="end-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """end_label_value must be of a type compatible with oc-mpls:mpls-label""",
          'defined-type': "oc-mpls:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="end-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)""",
        })

    self.__end_label_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_end_label_value(self):
    self.__end_label_value = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="end-label-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='oc-mpls:mpls-label', is_config=True)


  def _get_ttl_value(self):
    """
    Getter method for ttl_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/ttl_value (uint8)

    YANG Description: Time-to-live MPLS packet value match.
    """
    return self.__ttl_value
      
  def _set_ttl_value(self, v, load=False):
    """
    Setter method for ttl_value, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/mpls/config/ttl_value (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ttl_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ttl_value() directly.

    YANG Description: Time-to-live MPLS packet value match.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="ttl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ttl_value must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="ttl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint8', is_config=True)""",
        })

    self.__ttl_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ttl_value(self):
    self.__ttl_value = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="ttl-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint8', is_config=True)

  traffic_class = __builtin__.property(_get_traffic_class, _set_traffic_class)
  start_label_value = __builtin__.property(_get_start_label_value, _set_start_label_value)
  end_label_value = __builtin__.property(_get_end_label_value, _set_end_label_value)
  ttl_value = __builtin__.property(_get_ttl_value, _set_ttl_value)


  _pyangbind_elements = OrderedDict([('traffic_class', traffic_class), ('start_label_value', start_label_value), ('end_label_value', end_label_value), ('ttl_value', ttl_value), ])



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
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/wmm/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for WMM configuration elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__trust_dscp','__wmm_vo_remark','__wmm_vi_remark','__wmm_be_remark','__wmm_bk_remark',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__trust_dscp = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    self.__wmm_vo_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_vi_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_be_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_bk_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)

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
      return ['ssids', 'ssid', 'wmm', 'config']

  def _get_trust_dscp(self):
    """
    Getter method for trust_dscp, mapped from YANG variable /ssids/ssid/wmm/config/trust_dscp (boolean)

    YANG Description: The AP should trust DSCP on 802.11 frames received
in this BSS.
    """
    return self.__trust_dscp
      
  def _set_trust_dscp(self, v, load=False):
    """
    Setter method for trust_dscp, mapped from YANG variable /ssids/ssid/wmm/config/trust_dscp (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust_dscp() directly.

    YANG Description: The AP should trust DSCP on 802.11 frames received
in this BSS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust_dscp must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)""",
        })

    self.__trust_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust_dscp(self):
    self.__trust_dscp = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)


  def _get_wmm_vo_remark(self):
    """
    Getter method for wmm_vo_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vo_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_VO. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_vo_remark
      
  def _set_wmm_vo_remark(self, v, load=False):
    """
    Setter method for wmm_vo_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vo_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_vo_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_vo_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_VO. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_vo_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_vo_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_vo_remark(self):
    self.__wmm_vo_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_vi_remark(self):
    """
    Getter method for wmm_vi_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vi_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_VI. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_vi_remark
      
  def _set_wmm_vi_remark(self, v, load=False):
    """
    Setter method for wmm_vi_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vi_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_vi_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_vi_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_VI. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_vi_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_vi_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_vi_remark(self):
    self.__wmm_vi_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_be_remark(self):
    """
    Getter method for wmm_be_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_be_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_BE. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_be_remark
      
  def _set_wmm_be_remark(self, v, load=False):
    """
    Setter method for wmm_be_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_be_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_be_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_be_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_BE. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_be_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_be_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_be_remark(self):
    self.__wmm_be_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_bk_remark(self):
    """
    Getter method for wmm_bk_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_bk_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_BK. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_bk_remark
      
  def _set_wmm_bk_remark(self, v, load=False):
    """
    Setter method for wmm_bk_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_bk_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_bk_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_bk_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_BK. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_bk_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_bk_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_bk_remark(self):
    self.__wmm_bk_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)

  trust_dscp = __builtin__.property(_get_trust_dscp, _set_trust_dscp)
  wmm_vo_remark = __builtin__.property(_get_wmm_vo_remark, _set_wmm_vo_remark)
  wmm_vi_remark = __builtin__.property(_get_wmm_vi_remark, _set_wmm_vi_remark)
  wmm_be_remark = __builtin__.property(_get_wmm_be_remark, _set_wmm_be_remark)
  wmm_bk_remark = __builtin__.property(_get_wmm_bk_remark, _set_wmm_bk_remark)


  _pyangbind_elements = OrderedDict([('trust_dscp', trust_dscp), ('wmm_vo_remark', wmm_vo_remark), ('wmm_vi_remark', wmm_vi_remark), ('wmm_be_remark', wmm_be_remark), ('wmm_bk_remark', wmm_bk_remark), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/wmm/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for WMM configuration elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__trust_dscp','__wmm_vo_remark','__wmm_vi_remark','__wmm_be_remark','__wmm_bk_remark',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__trust_dscp = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    self.__wmm_vo_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_vi_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_be_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    self.__wmm_bk_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)

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
      return ['ssids', 'ssid', 'wmm', 'config']

  def _get_trust_dscp(self):
    """
    Getter method for trust_dscp, mapped from YANG variable /ssids/ssid/wmm/config/trust_dscp (boolean)

    YANG Description: The AP should trust DSCP on 802.11 frames received
in this BSS.
    """
    return self.__trust_dscp
      
  def _set_trust_dscp(self, v, load=False):
    """
    Setter method for trust_dscp, mapped from YANG variable /ssids/ssid/wmm/config/trust_dscp (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust_dscp() directly.

    YANG Description: The AP should trust DSCP on 802.11 frames received
in this BSS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust_dscp must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)""",
        })

    self.__trust_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust_dscp(self):
    self.__trust_dscp = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="trust-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='boolean', is_config=True)


  def _get_wmm_vo_remark(self):
    """
    Getter method for wmm_vo_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vo_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_VO. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_vo_remark
      
  def _set_wmm_vo_remark(self, v, load=False):
    """
    Setter method for wmm_vo_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vo_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_vo_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_vo_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_VO. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_vo_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_vo_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_vo_remark(self):
    self.__wmm_vo_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vo-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_vi_remark(self):
    """
    Getter method for wmm_vi_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vi_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_VI. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_vi_remark
      
  def _set_wmm_vi_remark(self, v, load=False):
    """
    Setter method for wmm_vi_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_vi_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_vi_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_vi_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_VI. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_vi_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_vi_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_vi_remark(self):
    self.__wmm_vi_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-vi-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_be_remark(self):
    """
    Getter method for wmm_be_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_be_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_BE. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_be_remark
      
  def _set_wmm_be_remark(self, v, load=False):
    """
    Setter method for wmm_be_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_be_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_be_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_be_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_BE. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_be_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_be_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_be_remark(self):
    self.__wmm_be_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-be-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)


  def _get_wmm_bk_remark(self):
    """
    Getter method for wmm_bk_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_bk_remark (uint8)

    YANG Description: Allowed DSCP markings for WMM AC_BK. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    return self.__wmm_bk_remark
      
  def _set_wmm_bk_remark(self, v, load=False):
    """
    Setter method for wmm_bk_remark, mapped from YANG variable /ssids/ssid/wmm/config/wmm_bk_remark (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_wmm_bk_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_wmm_bk_remark() directly.

    YANG Description: Allowed DSCP markings for WMM AC_BK. Remark to lowest in this
list if DSCP marking falls outside of these allowed markings.

From 1 (min) to 8 (max) integers.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """wmm_bk_remark must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)""",
        })

    self.__wmm_bk_remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_wmm_bk_remark(self):
    self.__wmm_bk_remark = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="wmm-bk-remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=True)

  trust_dscp = __builtin__.property(_get_trust_dscp, _set_trust_dscp)
  wmm_vo_remark = __builtin__.property(_get_wmm_vo_remark, _set_wmm_vo_remark)
  wmm_vi_remark = __builtin__.property(_get_wmm_vi_remark, _set_wmm_vi_remark)
  wmm_be_remark = __builtin__.property(_get_wmm_be_remark, _set_wmm_be_remark)
  wmm_bk_remark = __builtin__.property(_get_wmm_bk_remark, _set_wmm_bk_remark)


  _pyangbind_elements = OrderedDict([('trust_dscp', trust_dscp), ('wmm_vo_remark', wmm_vo_remark), ('wmm_vi_remark', wmm_vi_remark), ('wmm_be_remark', wmm_be_remark), ('wmm_bk_remark', wmm_bk_remark), ])



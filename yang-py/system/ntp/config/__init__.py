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
  from YANG module openconfig-system - based on the path /system/ntp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for NTP client.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__ntp_source_address','__enable_ntp_auth',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)
    self.__ntp_source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="ntp-source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:ip-address', is_config=True)
    self.__enable_ntp_auth = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-ntp-auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)

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
      return ['system', 'ntp', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /system/ntp/config/enabled (boolean)

    YANG Description: Enables the NTP protocol and indicates that the system should
attempt to synchronize the system clock with an NTP server
from the servers defined in the 'ntp/server' list.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /system/ntp/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enables the NTP protocol and indicates that the system should
attempt to synchronize the system clock with an NTP server
from the servers defined in the 'ntp/server' list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)


  def _get_ntp_source_address(self):
    """
    Getter method for ntp_source_address, mapped from YANG variable /system/ntp/config/ntp_source_address (oc-inet:ip-address)

    YANG Description: Source address to use on outgoing NTP packets
    """
    return self.__ntp_source_address
      
  def _set_ntp_source_address(self, v, load=False):
    """
    Setter method for ntp_source_address, mapped from YANG variable /system/ntp/config/ntp_source_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ntp_source_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ntp_source_address() directly.

    YANG Description: Source address to use on outgoing NTP packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="ntp-source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ntp_source_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="ntp-source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:ip-address', is_config=True)""",
        })

    self.__ntp_source_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ntp_source_address(self):
    self.__ntp_source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="ntp-source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:ip-address', is_config=True)


  def _get_enable_ntp_auth(self):
    """
    Getter method for enable_ntp_auth, mapped from YANG variable /system/ntp/config/enable_ntp_auth (boolean)

    YANG Description: Enable or disable NTP authentication -- when enabled, the
system will only use packets containing a trusted
authentication key to synchronize the time.
    """
    return self.__enable_ntp_auth
      
  def _set_enable_ntp_auth(self, v, load=False):
    """
    Setter method for enable_ntp_auth, mapped from YANG variable /system/ntp/config/enable_ntp_auth (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_ntp_auth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_ntp_auth() directly.

    YANG Description: Enable or disable NTP authentication -- when enabled, the
system will only use packets containing a trusted
authentication key to synchronize the time.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-ntp-auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_ntp_auth must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-ntp-auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)""",
        })

    self.__enable_ntp_auth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_ntp_auth(self):
    self.__enable_ntp_auth = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-ntp-auth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  ntp_source_address = __builtin__.property(_get_ntp_source_address, _set_ntp_source_address)
  enable_ntp_auth = __builtin__.property(_get_enable_ntp_auth, _set_enable_ntp_auth)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('ntp_source_address', ntp_source_address), ('enable_ntp_auth', enable_ntp_auth), ])



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
  from YANG module openconfig-system - based on the path /system/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global configuration data for the system
  """
  __slots__ = ('_path_helper', '_extmethods', '__hostname','__domain_name','__login_banner','__motd_banner',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hostname = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)
    self.__domain_name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)
    self.__login_banner = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    self.__motd_banner = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="motd-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)

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
      return ['system', 'config']

  def _get_hostname(self):
    """
    Getter method for hostname, mapped from YANG variable /system/config/hostname (oc-inet:domain-name)

    YANG Description: The hostname of the device -- should be a single domain
label, without the domain.
    """
    return self.__hostname
      
  def _set_hostname(self, v, load=False):
    """
    Setter method for hostname, mapped from YANG variable /system/config/hostname (oc-inet:domain-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname() directly.

    YANG Description: The hostname of the device -- should be a single domain
label, without the domain.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname must be of a type compatible with oc-inet:domain-name""",
          'defined-type': "oc-inet:domain-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)""",
        })

    self.__hostname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname(self):
    self.__hostname = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)


  def _get_domain_name(self):
    """
    Getter method for domain_name, mapped from YANG variable /system/config/domain_name (oc-inet:domain-name)

    YANG Description: Specifies the domain name used to form fully qualified name
for unqualified hostnames.
    """
    return self.__domain_name
      
  def _set_domain_name(self, v, load=False):
    """
    Setter method for domain_name, mapped from YANG variable /system/config/domain_name (oc-inet:domain-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name() directly.

    YANG Description: Specifies the domain name used to form fully qualified name
for unqualified hostnames.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name must be of a type compatible with oc-inet:domain-name""",
          'defined-type': "oc-inet:domain-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)""",
        })

    self.__domain_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name(self):
    self.__domain_name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.)', 'length': ['1..253']}), is_leaf=True, yang_name="domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-inet:domain-name', is_config=True)


  def _get_login_banner(self):
    """
    Getter method for login_banner, mapped from YANG variable /system/config/login_banner (string)

    YANG Description: The console login message displayed before the login prompt,
i.e., before a user logs into the system.
    """
    return self.__login_banner
      
  def _set_login_banner(self, v, load=False):
    """
    Setter method for login_banner, mapped from YANG variable /system/config/login_banner (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_login_banner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_login_banner() directly.

    YANG Description: The console login message displayed before the login prompt,
i.e., before a user logs into the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="login-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """login_banner must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__login_banner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_login_banner(self):
    self.__login_banner = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="login-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_motd_banner(self):
    """
    Getter method for motd_banner, mapped from YANG variable /system/config/motd_banner (string)

    YANG Description: The console message displayed after a user logs into the
system.  They system may append additional standard
information such as the current system date and time, uptime,
last login timestamp, etc.
    """
    return self.__motd_banner
      
  def _set_motd_banner(self, v, load=False):
    """
    Setter method for motd_banner, mapped from YANG variable /system/config/motd_banner (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_motd_banner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_motd_banner() directly.

    YANG Description: The console message displayed after a user logs into the
system.  They system may append additional standard
information such as the current system date and time, uptime,
last login timestamp, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="motd-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """motd_banner must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="motd-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__motd_banner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_motd_banner(self):
    self.__motd_banner = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="motd-banner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)

  hostname = __builtin__.property(_get_hostname, _set_hostname)
  domain_name = __builtin__.property(_get_domain_name, _set_domain_name)
  login_banner = __builtin__.property(_get_login_banner, _set_login_banner)
  motd_banner = __builtin__.property(_get_motd_banner, _set_motd_banner)


  _pyangbind_elements = OrderedDict([('hostname', hostname), ('domain_name', domain_name), ('login_banner', login_banner), ('motd_banner', motd_banner), ])



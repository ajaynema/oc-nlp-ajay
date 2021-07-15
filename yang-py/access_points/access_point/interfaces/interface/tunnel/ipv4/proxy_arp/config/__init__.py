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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv4/proxy-arp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for proxy ARP
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv4', 'proxy-arp', 'config']

  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv4/proxy_arp/config/mode (enumeration)

    YANG Description: When set to a value other than DISABLE, the local system should
respond to ARP requests that are for target addresses other than
those that are configured on the local subinterface using its own
MAC address as the target hardware address. If the REMOTE_ONLY
value is specified, replies are only sent when the target address
falls outside the locally configured subnets on the interface,
whereas with the ALL value, all requests, regardless of their
target address are replied to.
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv4/proxy_arp/config/mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: When set to a value other than DISABLE, the local system should
respond to ARP requests that are for target addresses other than
those that are configured on the local subinterface using its own
MAC address as the target hardware address. If the REMOTE_ONLY
value is specified, replies are only sent when the target address
falls outside the locally configured subnets on the interface,
whereas with the ALL value, all requests, regardless of their
target address are replied to.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)

  mode = __builtin__.property(_get_mode, _set_mode)


  _pyangbind_elements = OrderedDict([('mode', mode), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv4/proxy-arp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters for proxy ARP
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv4', 'proxy-arp', 'config']

  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv4/proxy_arp/config/mode (enumeration)

    YANG Description: When set to a value other than DISABLE, the local system should
respond to ARP requests that are for target addresses other than
those that are configured on the local subinterface using its own
MAC address as the target hardware address. If the REMOTE_ONLY
value is specified, replies are only sent when the target address
falls outside the locally configured subnets on the interface,
whereas with the ALL value, all requests, regardless of their
target address are replied to.
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv4/proxy_arp/config/mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: When set to a value other than DISABLE, the local system should
respond to ARP requests that are for target addresses other than
those that are configured on the local subinterface using its own
MAC address as the target hardware address. If the REMOTE_ONLY
value is specified, replies are only sent when the target address
falls outside the locally configured subnets on the interface,
whereas with the ALL value, all requests, regardless of their
target address are replied to.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-ap-interfaces:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'DISABLE': {}, 'REMOTE_ONLY': {}, 'ALL': {}},), default=six.text_type("DISABLE"), is_leaf=True, yang_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='enumeration', is_config=True)

  mode = __builtin__.property(_get_mode, _set_mode)


  _pyangbind_elements = OrderedDict([('mode', mode), ])



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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/as-path-options/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to AS_PATH manipulation
for the BGP peer or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__allow_own_as','__replace_peer_as','__disable_peer_as_filter',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__allow_own_as = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)
    self.__replace_peer_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__disable_peer_as_filter = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'neighbors', 'neighbor', 'as-path-options', 'config']

  def _get_allow_own_as(self):
    """
    Getter method for allow_own_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/allow_own_as (uint8)

    YANG Description: Specify the number of occurrences of the local BGP speaker's
AS that can occur within the AS_PATH before it is rejected.
    """
    return self.__allow_own_as
      
  def _set_allow_own_as(self, v, load=False):
    """
    Setter method for allow_own_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/allow_own_as (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_own_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_own_as() directly.

    YANG Description: Specify the number of occurrences of the local BGP speaker's
AS that can occur within the AS_PATH before it is rejected.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_own_as must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
        })

    self.__allow_own_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_own_as(self):
    self.__allow_own_as = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)


  def _get_replace_peer_as(self):
    """
    Getter method for replace_peer_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/replace_peer_as (boolean)

    YANG Description: Replace occurrences of the peer's AS in the AS_PATH
with the local autonomous system number
    """
    return self.__replace_peer_as
      
  def _set_replace_peer_as(self, v, load=False):
    """
    Setter method for replace_peer_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/replace_peer_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_replace_peer_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_replace_peer_as() directly.

    YANG Description: Replace occurrences of the peer's AS in the AS_PATH
with the local autonomous system number
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """replace_peer_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__replace_peer_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_replace_peer_as(self):
    self.__replace_peer_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_disable_peer_as_filter(self):
    """
    Getter method for disable_peer_as_filter, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/disable_peer_as_filter (boolean)

    YANG Description: When set to true, the system advertises routes to a peer
even if the peer's AS was in the AS path.  The default
behavior (false) suppresses advertisements to peers if
their AS number is in the AS path of the route.
    """
    return self.__disable_peer_as_filter
      
  def _set_disable_peer_as_filter(self, v, load=False):
    """
    Setter method for disable_peer_as_filter, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/disable_peer_as_filter (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable_peer_as_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable_peer_as_filter() directly.

    YANG Description: When set to true, the system advertises routes to a peer
even if the peer's AS was in the AS path.  The default
behavior (false) suppresses advertisements to peers if
their AS number is in the AS path of the route.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable_peer_as_filter must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__disable_peer_as_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable_peer_as_filter(self):
    self.__disable_peer_as_filter = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  allow_own_as = __builtin__.property(_get_allow_own_as, _set_allow_own_as)
  replace_peer_as = __builtin__.property(_get_replace_peer_as, _set_replace_peer_as)
  disable_peer_as_filter = __builtin__.property(_get_disable_peer_as_filter, _set_disable_peer_as_filter)


  _pyangbind_elements = OrderedDict([('allow_own_as', allow_own_as), ('replace_peer_as', replace_peer_as), ('disable_peer_as_filter', disable_peer_as_filter), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/as-path-options/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to AS_PATH manipulation
for the BGP peer or group
  """
  __slots__ = ('_path_helper', '_extmethods', '__allow_own_as','__replace_peer_as','__disable_peer_as_filter',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__allow_own_as = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)
    self.__replace_peer_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__disable_peer_as_filter = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'neighbors', 'neighbor', 'as-path-options', 'config']

  def _get_allow_own_as(self):
    """
    Getter method for allow_own_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/allow_own_as (uint8)

    YANG Description: Specify the number of occurrences of the local BGP speaker's
AS that can occur within the AS_PATH before it is rejected.
    """
    return self.__allow_own_as
      
  def _set_allow_own_as(self, v, load=False):
    """
    Setter method for allow_own_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/allow_own_as (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_own_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_own_as() directly.

    YANG Description: Specify the number of occurrences of the local BGP speaker's
AS that can occur within the AS_PATH before it is rejected.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_own_as must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
        })

    self.__allow_own_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_own_as(self):
    self.__allow_own_as = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="allow-own-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)


  def _get_replace_peer_as(self):
    """
    Getter method for replace_peer_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/replace_peer_as (boolean)

    YANG Description: Replace occurrences of the peer's AS in the AS_PATH
with the local autonomous system number
    """
    return self.__replace_peer_as
      
  def _set_replace_peer_as(self, v, load=False):
    """
    Setter method for replace_peer_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/replace_peer_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_replace_peer_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_replace_peer_as() directly.

    YANG Description: Replace occurrences of the peer's AS in the AS_PATH
with the local autonomous system number
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """replace_peer_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__replace_peer_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_replace_peer_as(self):
    self.__replace_peer_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="replace-peer-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_disable_peer_as_filter(self):
    """
    Getter method for disable_peer_as_filter, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/disable_peer_as_filter (boolean)

    YANG Description: When set to true, the system advertises routes to a peer
even if the peer's AS was in the AS path.  The default
behavior (false) suppresses advertisements to peers if
their AS number is in the AS path of the route.
    """
    return self.__disable_peer_as_filter
      
  def _set_disable_peer_as_filter(self, v, load=False):
    """
    Setter method for disable_peer_as_filter, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/as_path_options/config/disable_peer_as_filter (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable_peer_as_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable_peer_as_filter() directly.

    YANG Description: When set to true, the system advertises routes to a peer
even if the peer's AS was in the AS path.  The default
behavior (false) suppresses advertisements to peers if
their AS number is in the AS path of the route.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable_peer_as_filter must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__disable_peer_as_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable_peer_as_filter(self):
    self.__disable_peer_as_filter = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="disable-peer-as-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  allow_own_as = __builtin__.property(_get_allow_own_as, _set_allow_own_as)
  replace_peer_as = __builtin__.property(_get_replace_peer_as, _set_replace_peer_as)
  disable_peer_as_filter = __builtin__.property(_get_disable_peer_as_filter, _set_disable_peer_as_filter)


  _pyangbind_elements = OrderedDict([('allow_own_as', allow_own_as), ('replace_peer_as', replace_peer_as), ('disable_peer_as_filter', disable_peer_as_filter), ])



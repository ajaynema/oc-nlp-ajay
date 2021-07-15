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
  from YANG module openconfig-fw-high-availability - based on the path /ha-groups/ha-group/data-link/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters related to primary HA data
link
  """
  __slots__ = ('_path_helper', '_extmethods', '__data_link_interface','__data_link_port','__data_link_ipv4','__data_link_gateway','__data_link_ipv6','__data_link_ipv6_gateway','__data_link_peer_ipv4','__data_link_peer_ipv6',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__data_link_interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="data-link-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-if:base-interface-ref', is_config=False)
    self.__data_link_port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="data-link-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:port-number', is_config=False)
    self.__data_link_ipv4 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)
    self.__data_link_gateway = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="data-link-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-address', is_config=False)
    self.__data_link_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)
    self.__data_link_ipv6_gateway = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="data-link-ipv6-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-address', is_config=False)
    self.__data_link_peer_ipv4 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-peer-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)
    self.__data_link_peer_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-peer-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)

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
      return ['ha-groups', 'ha-group', 'data-link', 'state']

  def _get_data_link_interface(self):
    """
    Getter method for data_link_interface, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_interface (oc-if:base-interface-ref)

    YANG Description: Specify which interface will be used to sync session tables,
forwarding tables, ARP tables, IPSEC SAs and any other
messages that MUST be exchanged to facilitate seamless traffic
handling during a failover event
    """
    return self.__data_link_interface
      
  def _set_data_link_interface(self, v, load=False):
    """
    Setter method for data_link_interface, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_interface (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_interface() directly.

    YANG Description: Specify which interface will be used to sync session tables,
forwarding tables, ARP tables, IPSEC SAs and any other
messages that MUST be exchanged to facilitate seamless traffic
handling during a failover event
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="data-link-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_interface must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="data-link-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__data_link_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_interface(self):
    self.__data_link_interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="data-link-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-if:base-interface-ref', is_config=False)


  def _get_data_link_port(self):
    """
    Getter method for data_link_port, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_port (oc-inet:port-number)

    YANG Description: Specify which TCP/UDP port will be used to exchange data link
messages
    """
    return self.__data_link_port
      
  def _set_data_link_port(self, v, load=False):
    """
    Setter method for data_link_port, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_port (oc-inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_port() directly.

    YANG Description: Specify which TCP/UDP port will be used to exchange data link
messages
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="data-link-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:port-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_port must be of a type compatible with oc-inet:port-number""",
          'defined-type': "oc-inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="data-link-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:port-number', is_config=False)""",
        })

    self.__data_link_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_port(self):
    self.__data_link_port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="data-link-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:port-number', is_config=False)


  def _get_data_link_ipv4(self):
    """
    Getter method for data_link_ipv4, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv4 (oc-inet:ipv4-prefix)

    YANG Description: If data link is layer 3, specify the local unit's ipv4
address
    """
    return self.__data_link_ipv4
      
  def _set_data_link_ipv4(self, v, load=False):
    """
    Setter method for data_link_ipv4, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv4 (oc-inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_ipv4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_ipv4() directly.

    YANG Description: If data link is layer 3, specify the local unit's ipv4
address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_ipv4 must be of a type compatible with oc-inet:ipv4-prefix""",
          'defined-type': "oc-inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)""",
        })

    self.__data_link_ipv4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_ipv4(self):
    self.__data_link_ipv4 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)


  def _get_data_link_gateway(self):
    """
    Getter method for data_link_gateway, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_gateway (oc-inet:ipv4-address)

    YANG Description: If peer data ip is in a different subnet, specify the gateway
ip here to provide reachability
    """
    return self.__data_link_gateway
      
  def _set_data_link_gateway(self, v, load=False):
    """
    Setter method for data_link_gateway, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_gateway (oc-inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_gateway() directly.

    YANG Description: If peer data ip is in a different subnet, specify the gateway
ip here to provide reachability
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="data-link-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_gateway must be of a type compatible with oc-inet:ipv4-address""",
          'defined-type': "oc-inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="data-link-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-address', is_config=False)""",
        })

    self.__data_link_gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_gateway(self):
    self.__data_link_gateway = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="data-link-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-address', is_config=False)


  def _get_data_link_ipv6(self):
    """
    Getter method for data_link_ipv6, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv6 (oc-inet:ipv6-prefix)

    YANG Description: If data link is layer 3, specify the local unit's ipv6
address
    """
    return self.__data_link_ipv6
      
  def _set_data_link_ipv6(self, v, load=False):
    """
    Setter method for data_link_ipv6, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv6 (oc-inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_ipv6() directly.

    YANG Description: If data link is layer 3, specify the local unit's ipv6
address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_ipv6 must be of a type compatible with oc-inet:ipv6-prefix""",
          'defined-type': "oc-inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)""",
        })

    self.__data_link_ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_ipv6(self):
    self.__data_link_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)


  def _get_data_link_ipv6_gateway(self):
    """
    Getter method for data_link_ipv6_gateway, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv6_gateway (oc-inet:ipv6-address)

    YANG Description: If peer data ipv6 is in a different subnet, specify the
gateway ipv6 here to provide reachability
    """
    return self.__data_link_ipv6_gateway
      
  def _set_data_link_ipv6_gateway(self, v, load=False):
    """
    Setter method for data_link_ipv6_gateway, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_ipv6_gateway (oc-inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_ipv6_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_ipv6_gateway() directly.

    YANG Description: If peer data ipv6 is in a different subnet, specify the
gateway ipv6 here to provide reachability
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="data-link-ipv6-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_ipv6_gateway must be of a type compatible with oc-inet:ipv6-address""",
          'defined-type': "oc-inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="data-link-ipv6-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-address', is_config=False)""",
        })

    self.__data_link_ipv6_gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_ipv6_gateway(self):
    self.__data_link_ipv6_gateway = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}), is_leaf=True, yang_name="data-link-ipv6-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-address', is_config=False)


  def _get_data_link_peer_ipv4(self):
    """
    Getter method for data_link_peer_ipv4, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_peer_ipv4 (oc-inet:ipv4-prefix)

    YANG Description: If data link is layer 3, specify the peer's ipv4 address
    """
    return self.__data_link_peer_ipv4
      
  def _set_data_link_peer_ipv4(self, v, load=False):
    """
    Setter method for data_link_peer_ipv4, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_peer_ipv4 (oc-inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_peer_ipv4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_peer_ipv4() directly.

    YANG Description: If data link is layer 3, specify the peer's ipv4 address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-peer-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_peer_ipv4 must be of a type compatible with oc-inet:ipv4-prefix""",
          'defined-type': "oc-inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-peer-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)""",
        })

    self.__data_link_peer_ipv4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_peer_ipv4(self):
    self.__data_link_peer_ipv4 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="data-link-peer-ipv4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv4-prefix', is_config=False)


  def _get_data_link_peer_ipv6(self):
    """
    Getter method for data_link_peer_ipv6, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_peer_ipv6 (oc-inet:ipv6-prefix)

    YANG Description: If data link is layer 3, specify the peer's ipv6 address
    """
    return self.__data_link_peer_ipv6
      
  def _set_data_link_peer_ipv6(self, v, load=False):
    """
    Setter method for data_link_peer_ipv6, mapped from YANG variable /ha_groups/ha_group/data_link/state/data_link_peer_ipv6 (oc-inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link_peer_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link_peer_ipv6() directly.

    YANG Description: If data link is layer 3, specify the peer's ipv6 address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-peer-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link_peer_ipv6 must be of a type compatible with oc-inet:ipv6-prefix""",
          'defined-type': "oc-inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-peer-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)""",
        })

    self.__data_link_peer_ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link_peer_ipv6(self):
    self.__data_link_peer_ipv6 = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}), is_leaf=True, yang_name="data-link-peer-ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='oc-inet:ipv6-prefix', is_config=False)

  data_link_interface = __builtin__.property(_get_data_link_interface)
  data_link_port = __builtin__.property(_get_data_link_port)
  data_link_ipv4 = __builtin__.property(_get_data_link_ipv4)
  data_link_gateway = __builtin__.property(_get_data_link_gateway)
  data_link_ipv6 = __builtin__.property(_get_data_link_ipv6)
  data_link_ipv6_gateway = __builtin__.property(_get_data_link_ipv6_gateway)
  data_link_peer_ipv4 = __builtin__.property(_get_data_link_peer_ipv4)
  data_link_peer_ipv6 = __builtin__.property(_get_data_link_peer_ipv6)


  _pyangbind_elements = OrderedDict([('data_link_interface', data_link_interface), ('data_link_port', data_link_port), ('data_link_ipv4', data_link_ipv4), ('data_link_gateway', data_link_gateway), ('data_link_ipv6', data_link_ipv6), ('data_link_ipv6_gateway', data_link_ipv6_gateway), ('data_link_peer_ipv4', data_link_peer_ipv4), ('data_link_peer_ipv6', data_link_peer_ipv6), ])



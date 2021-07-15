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
  from YANG module openconfig-sampling-sflow - based on the path /sampling/sflow/collectors/collector/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for sFlow collectors.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address','__port','__network_instance','__packets_sent',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(6343), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:port-number', is_config=False)
    self.__network_instance = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="network-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-netinst:network-instance-ref', is_config=False)
    self.__packets_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-yang:counter64', is_config=False)

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
      return ['sampling', 'sflow', 'collectors', 'collector', 'state']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /sampling/sflow/collectors/collector/state/address (oc-inet:ip-address)

    YANG Description: IP address of the sFlow collector.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /sampling/sflow/collectors/collector/state/address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: IP address of the sFlow collector.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /sampling/sflow/collectors/collector/state/port (oc-inet:port-number)

    YANG Description: UDP port number for the sFlow collector.
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /sampling/sflow/collectors/collector/state/port (oc-inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: UDP port number for the sFlow collector.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(6343), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:port-number', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with oc-inet:port-number""",
          'defined-type': "oc-inet:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(6343), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:port-number', is_config=False)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(6343), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:port-number', is_config=False)


  def _get_network_instance(self):
    """
    Getter method for network_instance, mapped from YANG variable /sampling/sflow/collectors/collector/state/network_instance (oc-netinst:network-instance-ref)

    YANG Description: Reference to the network instance used to reach the
sFlow collector.  If uspecified, the collector destination
is reachable in the default network instance.
    """
    return self.__network_instance
      
  def _set_network_instance(self, v, load=False):
    """
    Setter method for network_instance, mapped from YANG variable /sampling/sflow/collectors/collector/state/network_instance (oc-netinst:network-instance-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_instance() directly.

    YANG Description: Reference to the network instance used to reach the
sFlow collector.  If uspecified, the collector destination
is reachable in the default network instance.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="network-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-netinst:network-instance-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_instance must be of a type compatible with oc-netinst:network-instance-ref""",
          'defined-type': "oc-netinst:network-instance-ref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="network-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-netinst:network-instance-ref', is_config=False)""",
        })

    self.__network_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_instance(self):
    self.__network_instance = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="network-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-netinst:network-instance-ref', is_config=False)


  def _get_packets_sent(self):
    """
    Getter method for packets_sent, mapped from YANG variable /sampling/sflow/collectors/collector/state/packets_sent (oc-yang:counter64)

    YANG Description: The total number of packets sampled and sent to the
collector.
    """
    return self.__packets_sent
      
  def _set_packets_sent(self, v, load=False):
    """
    Setter method for packets_sent, mapped from YANG variable /sampling/sflow/collectors/collector/state/packets_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_packets_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_packets_sent() directly.

    YANG Description: The total number of packets sampled and sent to the
collector.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """packets_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__packets_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_packets_sent(self):
    self.__packets_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="packets-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-yang:counter64', is_config=False)

  address = __builtin__.property(_get_address)
  port = __builtin__.property(_get_port)
  network_instance = __builtin__.property(_get_network_instance)
  packets_sent = __builtin__.property(_get_packets_sent)


  _pyangbind_elements = OrderedDict([('address', address), ('port', port), ('network_instance', network_instance), ('packets_sent', packets_sent), ])



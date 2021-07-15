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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/dynamic-neighbor-prefixes/dynamic-neighbor-prefix/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the source prefix
for the dynamic BGP neighbor connections.
  """
  __slots__ = ('_path_helper', '_extmethods', '__prefix','__peer_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)
    self.__peer_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'dynamic-neighbor-prefixes', 'dynamic-neighbor-prefix', 'config']

  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/prefix (oc-inet:ip-prefix)

    YANG Description: The IP prefix within which the source address of the remote
BGP speaker must fall to be considered eligible to the
dynamically configured.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/prefix (oc-inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: The IP prefix within which the source address of the remote
BGP speaker must fall to be considered eligible to the
dynamically configured.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with oc-inet:ip-prefix""",
          'defined-type': "oc-inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)


  def _get_peer_group(self):
    """
    Getter method for peer_group, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/peer_group (leafref)

    YANG Description: The peer-group within which the dynamic neighbor will be
configured.  The configuration parameters used for the dynamic
neighbor are those specified within the referenced peer
group.
    """
    return self.__peer_group
      
  def _set_peer_group(self, v, load=False):
    """
    Setter method for peer_group, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/peer_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_group() directly.

    YANG Description: The peer-group within which the dynamic neighbor will be
configured.  The configuration parameters used for the dynamic
neighbor are those specified within the referenced peer
group.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_group(self):
    self.__peer_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

  prefix = __builtin__.property(_get_prefix, _set_prefix)
  peer_group = __builtin__.property(_get_peer_group, _set_peer_group)


  _pyangbind_elements = OrderedDict([('prefix', prefix), ('peer_group', peer_group), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/dynamic-neighbor-prefixes/dynamic-neighbor-prefix/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the source prefix
for the dynamic BGP neighbor connections.
  """
  __slots__ = ('_path_helper', '_extmethods', '__prefix','__peer_group',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)
    self.__peer_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'dynamic-neighbor-prefixes', 'dynamic-neighbor-prefix', 'config']

  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/prefix (oc-inet:ip-prefix)

    YANG Description: The IP prefix within which the source address of the remote
BGP speaker must fall to be considered eligible to the
dynamically configured.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/prefix (oc-inet:ip-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: The IP prefix within which the source address of the remote
BGP speaker must fall to be considered eligible to the
dynamically configured.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with oc-inet:ip-prefix""",
          'defined-type': "oc-inet:ip-prefix",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9])'}),], is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-inet:ip-prefix', is_config=True)


  def _get_peer_group(self):
    """
    Getter method for peer_group, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/peer_group (leafref)

    YANG Description: The peer-group within which the dynamic neighbor will be
configured.  The configuration parameters used for the dynamic
neighbor are those specified within the referenced peer
group.
    """
    return self.__peer_group
      
  def _set_peer_group(self, v, load=False):
    """
    Setter method for peer_group, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/dynamic_neighbor_prefixes/dynamic_neighbor_prefix/config/peer_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_group() directly.

    YANG Description: The peer-group within which the dynamic neighbor will be
configured.  The configuration parameters used for the dynamic
neighbor are those specified within the referenced peer
group.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__peer_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_group(self):
    self.__peer_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="peer-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

  prefix = __builtin__.property(_get_prefix, _set_prefix)
  peer_group = __builtin__.property(_get_peer_group, _set_peer_group)


  _pyangbind_elements = OrderedDict([('prefix', prefix), ('peer_group', peer_group), ])



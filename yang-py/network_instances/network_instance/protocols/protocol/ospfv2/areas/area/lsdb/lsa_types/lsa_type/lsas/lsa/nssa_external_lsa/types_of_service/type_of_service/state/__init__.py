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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/nssa-external-lsa/types-of-service/type-of-service/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-TOS parameters for the LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_address','__external_route_tag','__tos','__metric',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'nssa-external-lsa', 'types-of-service', 'type-of-service', 'state']

  def _get_forwarding_address(self):
    """
    Getter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/forwarding_address (inet:ipv4-address-no-zone)

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    return self.__forwarding_address
      
  def _set_forwarding_address(self, v, load=False):
    """
    Setter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/forwarding_address (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_address() directly.

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_address must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)""",
        })

    self.__forwarding_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_address(self):
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)


  def _get_external_route_tag(self):
    """
    Getter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/external_route_tag (uint32)

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    return self.__external_route_tag
      
  def _set_external_route_tag(self, v, load=False):
    """
    Setter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/external_route_tag (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_tag() directly.

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_tag must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__external_route_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_tag(self):
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_tos(self):
    """
    Getter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/tos (uint8)

    YANG Description: OSPF encoding of the type of service referred to by this
LSA. Encoding for OSPF TOS are described in RFC2328.
    """
    return self.__tos
      
  def _set_tos(self, v, load=False):
    """
    Setter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/tos (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tos() directly.

    YANG Description: OSPF encoding of the type of service referred to by this
LSA. Encoding for OSPF TOS are described in RFC2328.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tos must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__tos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tos(self):
    self.__tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/metric (oc-ospf-types:ospf-metric)

    YANG Description: The metric value to be used for the TOS specified. This value
represents the cost of use of the link for the specific type
of service.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/metric (oc-ospf-types:ospf-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: The metric value to be used for the TOS specified. This value
represents the cost of use of the link for the specific type
of service.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-ospf-types:ospf-metric""",
          'defined-type': "oc-ospf-types:ospf-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)

  forwarding_address = __builtin__.property(_get_forwarding_address)
  external_route_tag = __builtin__.property(_get_external_route_tag)
  tos = __builtin__.property(_get_tos)
  metric = __builtin__.property(_get_metric)


  _pyangbind_elements = OrderedDict([('forwarding_address', forwarding_address), ('external_route_tag', external_route_tag), ('tos', tos), ('metric', metric), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/nssa-external-lsa/types-of-service/type-of-service/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-TOS parameters for the LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__forwarding_address','__external_route_tag','__tos','__metric',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'nssa-external-lsa', 'types-of-service', 'type-of-service', 'state']

  def _get_forwarding_address(self):
    """
    Getter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/forwarding_address (inet:ipv4-address-no-zone)

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    return self.__forwarding_address
      
  def _set_forwarding_address(self, v, load=False):
    """
    Setter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/forwarding_address (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_address() directly.

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_address must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)""",
        })

    self.__forwarding_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_address(self):
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)


  def _get_external_route_tag(self):
    """
    Getter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/external_route_tag (uint32)

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    return self.__external_route_tag
      
  def _set_external_route_tag(self, v, load=False):
    """
    Setter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/external_route_tag (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_tag() directly.

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_tag must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__external_route_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_tag(self):
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_tos(self):
    """
    Getter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/tos (uint8)

    YANG Description: OSPF encoding of the type of service referred to by this
LSA. Encoding for OSPF TOS are described in RFC2328.
    """
    return self.__tos
      
  def _set_tos(self, v, load=False):
    """
    Setter method for tos, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/tos (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tos() directly.

    YANG Description: OSPF encoding of the type of service referred to by this
LSA. Encoding for OSPF TOS are described in RFC2328.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tos must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__tos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tos(self):
    self.__tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/metric (oc-ospf-types:ospf-metric)

    YANG Description: The metric value to be used for the TOS specified. This value
represents the cost of use of the link for the specific type
of service.
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/nssa_external_lsa/types_of_service/type_of_service/state/metric (oc-ospf-types:ospf-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: The metric value to be used for the TOS specified. This value
represents the cost of use of the link for the specific type
of service.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-ospf-types:ospf-metric""",
          'defined-type': "oc-ospf-types:ospf-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)

  forwarding_address = __builtin__.property(_get_forwarding_address)
  external_route_tag = __builtin__.property(_get_external_route_tag)
  tos = __builtin__.property(_get_tos)
  metric = __builtin__.property(_get_metric)


  _pyangbind_elements = OrderedDict([('forwarding_address', forwarding_address), ('external_route_tag', external_route_tag), ('tos', tos), ('metric', metric), ])



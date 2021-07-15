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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-link/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the Extended Link LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__link_type','__link_id','__link_data',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__link_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    self.__link_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)
    self.__link_data = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-link', 'state']

  def _get_link_type(self):
    """
    Getter method for link_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_type (identityref)

    YANG Description: The type of link with which extended attributes are associated
    """
    return self.__link_type
      
  def _set_link_type(self, v, load=False):
    """
    Setter method for link_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_type() directly.

    YANG Description: The type of link with which extended attributes are associated
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__link_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_type(self):
    self.__link_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)


  def _get_link_id(self):
    """
    Getter method for link_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_id (yang:dotted-quad)

    YANG Description: The identifier for the link specified. The value of the link
identifier is dependent upon the type of the LSA. The value is
specified to be, per sub-type:
 1) Neighbouring router's router ID.
 2) IP address of DR.
 3) IP network address.
 4) Neighbouring router router's ID.
    """
    return self.__link_id
      
  def _set_link_id(self, v, load=False):
    """
    Setter method for link_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_id (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_id() directly.

    YANG Description: The identifier for the link specified. The value of the link
identifier is dependent upon the type of the LSA. The value is
specified to be, per sub-type:
 1) Neighbouring router's router ID.
 2) IP address of DR.
 3) IP network address.
 4) Neighbouring router router's ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_id must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)""",
        })

    self.__link_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_id(self):
    self.__link_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)


  def _get_link_data(self):
    """
    Getter method for link_data, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_data (union)

    YANG Description: The data associated with the link type. The value is
dependent upon the subtype of the LSA. When the connection is
to a stub network it represents the mask; for p2p connections
that are unnumbered it represents the ifIndex value of the
router's interface; for all other connections it represents
the local system's IP address
    """
    return self.__link_data
      
  def _set_link_data(self, v, load=False):
    """
    Setter method for link_data, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_data (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_data() directly.

    YANG Description: The data associated with the link type. The value is
dependent upon the subtype of the LSA. When the connection is
to a stub network it represents the mask; for p2p connections
that are unnumbered it represents the ifIndex value of the
router's interface; for all other connections it represents
the local system's IP address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_data must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__link_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_data(self):
    self.__link_data = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  link_type = __builtin__.property(_get_link_type)
  link_id = __builtin__.property(_get_link_id)
  link_data = __builtin__.property(_get_link_data)


  _pyangbind_elements = OrderedDict([('link_type', link_type), ('link_id', link_id), ('link_data', link_data), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-link/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the Extended Link LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__link_type','__link_id','__link_data',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__link_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    self.__link_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)
    self.__link_data = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-link', 'state']

  def _get_link_type(self):
    """
    Getter method for link_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_type (identityref)

    YANG Description: The type of link with which extended attributes are associated
    """
    return self.__link_type
      
  def _set_link_type(self, v, load=False):
    """
    Setter method for link_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_type() directly.

    YANG Description: The type of link with which extended attributes are associated
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__link_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_type(self):
    self.__link_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:POINT_TO_POINT_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:TRANSIT_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:STUB_NETWORK_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospf-types:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}, 'oc-ospft:VIRTUAL_LINK': {'@module': 'openconfig-ospf-types', '@namespace': 'http://openconfig.net/yang/ospf-types'}},), is_leaf=True, yang_name="link-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)


  def _get_link_id(self):
    """
    Getter method for link_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_id (yang:dotted-quad)

    YANG Description: The identifier for the link specified. The value of the link
identifier is dependent upon the type of the LSA. The value is
specified to be, per sub-type:
 1) Neighbouring router's router ID.
 2) IP address of DR.
 3) IP network address.
 4) Neighbouring router router's ID.
    """
    return self.__link_id
      
  def _set_link_id(self, v, load=False):
    """
    Setter method for link_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_id (yang:dotted-quad)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_id() directly.

    YANG Description: The identifier for the link specified. The value of the link
identifier is dependent upon the type of the LSA. The value is
specified to be, per sub-type:
 1) Neighbouring router's router ID.
 2) IP address of DR.
 3) IP network address.
 4) Neighbouring router router's ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_id must be of a type compatible with yang:dotted-quad""",
          'defined-type': "yang:dotted-quad",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)""",
        })

    self.__link_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_id(self):
    self.__link_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}), is_leaf=True, yang_name="link-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:dotted-quad', is_config=False)


  def _get_link_data(self):
    """
    Getter method for link_data, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_data (union)

    YANG Description: The data associated with the link type. The value is
dependent upon the subtype of the LSA. When the connection is
to a stub network it represents the mask; for p2p connections
that are unnumbered it represents the ifIndex value of the
router's interface; for all other connections it represents
the local system's IP address
    """
    return self.__link_data
      
  def _set_link_data(self, v, load=False):
    """
    Setter method for link_data, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_link/state/link_data (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_data() directly.

    YANG Description: The data associated with the link type. The value is
dependent upon the subtype of the LSA. When the connection is
to a stub network it represents the mask; for p2p connections
that are unnumbered it represents the ifIndex value of the
router's interface; for all other connections it represents
the local system's IP address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_data must be of a type compatible with union""",
          'defined-type': "openconfig-network-instance:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)""",
        })

    self.__link_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_data(self):
    self.__link_data = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),], is_leaf=True, yang_name="link-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='union', is_config=False)

  link_type = __builtin__.property(_get_link_type)
  link_id = __builtin__.property(_get_link_id)
  link_data = __builtin__.property(_get_link_data)


  _pyangbind_elements = OrderedDict([('link_type', link_type), ('link_id', link_id), ('link_data', link_data), ])



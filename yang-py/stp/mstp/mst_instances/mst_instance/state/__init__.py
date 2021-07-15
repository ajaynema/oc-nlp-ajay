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
  from YANG module openconfig-spanning-tree - based on the path /stp/mstp/mst-instances/mst-instance/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational data for MSTP instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__mst_id','__vlan','__bridge_priority','__bridge_address','__designated_root_priority','__designated_root_address','__root_port','__root_cost','__hold_time','__topology_changes','__last_topology_change',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mst_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="mst-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)
    self.__vlan = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])$'}),]), is_leaf=False, yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='union', is_config=False)
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)
    self.__bridge_address = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bridge-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)
    self.__designated_root_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="designated-root-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)
    self.__designated_root_address = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="designated-root-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)
    self.__root_port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="root-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)
    self.__root_cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="root-cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=False)
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)
    self.__topology_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="topology-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)
    self.__last_topology_change = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-topology-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-types:timeticks64', is_config=False)

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
      return ['stp', 'mstp', 'mst-instances', 'mst-instance', 'state']

  def _get_mst_id(self):
    """
    Getter method for mst_id, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/mst_id (uint16)

    YANG Description: In an MSTP Bridge, an MSTID, i.e., a value used to identify
a spanning tree (or MST) instance.
    """
    return self.__mst_id
      
  def _set_mst_id(self, v, load=False):
    """
    Setter method for mst_id, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/mst_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mst_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mst_id() directly.

    YANG Description: In an MSTP Bridge, an MSTID, i.e., a value used to identify
a spanning tree (or MST) instance.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="mst-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mst_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="mst-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)""",
        })

    self.__mst_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mst_id(self):
    self.__mst_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="mst-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/vlan (union)

    YANG Description: list of vlans mapped to the MST instance
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/vlan (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.

    YANG Description: list of vlans mapped to the MST instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])$'}),]), is_leaf=False, yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with union""",
          'defined-type': "openconfig-spanning-tree:union",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])$'}),]), is_leaf=False, yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='union', is_config=False)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])$'}),]), is_leaf=False, yang_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='union', is_config=False)


  def _get_bridge_priority(self):
    """
    Getter method for bridge_priority, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/bridge_priority (oc-stp-types:stp-bridge-priority-type)

    YANG Description: The manageable component of the Bridge Identifier
    """
    return self.__bridge_priority
      
  def _set_bridge_priority(self, v, load=False):
    """
    Setter method for bridge_priority, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/bridge_priority (oc-stp-types:stp-bridge-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_priority() directly.

    YANG Description: The manageable component of the Bridge Identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_priority must be of a type compatible with oc-stp-types:stp-bridge-priority-type""",
          'defined-type': "oc-stp-types:stp-bridge-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)""",
        })

    self.__bridge_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_priority(self):
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)


  def _get_bridge_address(self):
    """
    Getter method for bridge_address, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/bridge_address (oc-yang:mac-address)

    YANG Description: A unique 48-bit Universally Administered MAC Address
assigned to the bridge
    """
    return self.__bridge_address
      
  def _set_bridge_address(self, v, load=False):
    """
    Setter method for bridge_address, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/bridge_address (oc-yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_address() directly.

    YANG Description: A unique 48-bit Universally Administered MAC Address
assigned to the bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bridge-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_address must be of a type compatible with oc-yang:mac-address""",
          'defined-type': "oc-yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bridge-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)""",
        })

    self.__bridge_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_address(self):
    self.__bridge_address = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="bridge-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)


  def _get_designated_root_priority(self):
    """
    Getter method for designated_root_priority, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/designated_root_priority (oc-stp-types:stp-bridge-priority-type)

    YANG Description: The bridge priority of the root of the spanning
tree, as determined by the Spanning Tree Protocol,
as executed by this node
    """
    return self.__designated_root_priority
      
  def _set_designated_root_priority(self, v, load=False):
    """
    Setter method for designated_root_priority, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/designated_root_priority (oc-stp-types:stp-bridge-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_designated_root_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_designated_root_priority() directly.

    YANG Description: The bridge priority of the root of the spanning
tree, as determined by the Spanning Tree Protocol,
as executed by this node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="designated-root-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """designated_root_priority must be of a type compatible with oc-stp-types:stp-bridge-priority-type""",
          'defined-type': "oc-stp-types:stp-bridge-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="designated-root-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)""",
        })

    self.__designated_root_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_designated_root_priority(self):
    self.__designated_root_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="designated-root-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=False)


  def _get_designated_root_address(self):
    """
    Getter method for designated_root_address, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/designated_root_address (oc-yang:mac-address)

    YANG Description: The bridge address of the root of the spanning
tree, as determined by the Spanning Tree Protocol,
as executed by this node
    """
    return self.__designated_root_address
      
  def _set_designated_root_address(self, v, load=False):
    """
    Setter method for designated_root_address, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/designated_root_address (oc-yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_designated_root_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_designated_root_address() directly.

    YANG Description: The bridge address of the root of the spanning
tree, as determined by the Spanning Tree Protocol,
as executed by this node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="designated-root-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """designated_root_address must be of a type compatible with oc-yang:mac-address""",
          'defined-type': "oc-yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="designated-root-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)""",
        })

    self.__designated_root_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_designated_root_address(self):
    self.__designated_root_address = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="designated-root-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:mac-address', is_config=False)


  def _get_root_port(self):
    """
    Getter method for root_port, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/root_port (uint16)

    YANG Description: The port number of the port which offers the lowest
cost path from this bridge to the root bridge
    """
    return self.__root_port
      
  def _set_root_port(self, v, load=False):
    """
    Setter method for root_port, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/root_port (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_root_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_root_port() directly.

    YANG Description: The port number of the port which offers the lowest
cost path from this bridge to the root bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="root-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """root_port must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="root-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)""",
        })

    self.__root_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_root_port(self):
    self.__root_port = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="root-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint16', is_config=False)


  def _get_root_cost(self):
    """
    Getter method for root_cost, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/root_cost (uint32)

    YANG Description: The cost of the path to the root as seen from this bridge
    """
    return self.__root_cost
      
  def _set_root_cost(self, v, load=False):
    """
    Setter method for root_cost, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/root_cost (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_root_cost is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_root_cost() directly.

    YANG Description: The cost of the path to the root as seen from this bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="root-cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """root_cost must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="root-cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=False)""",
        })

    self.__root_cost = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_root_cost(self):
    self.__root_cost = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="root-cost", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint32', is_config=False)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/hold_time (uint8)

    YANG Description: This time value determines the interval length
during which no more than two Configuration bridge
PDUs shall be transmitted by this node
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/hold_time (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.

    YANG Description: This time value determines the interval length
during which no more than two Configuration bridge
PDUs shall be transmitted by this node
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)


  def _get_topology_changes(self):
    """
    Getter method for topology_changes, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/topology_changes (oc-yang:counter64)

    YANG Description: The total number of topology changes detected by
this bridge since the management entity was last
reset or initialized
    """
    return self.__topology_changes
      
  def _set_topology_changes(self, v, load=False):
    """
    Setter method for topology_changes, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/topology_changes (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_topology_changes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_topology_changes() directly.

    YANG Description: The total number of topology changes detected by
this bridge since the management entity was last
reset or initialized
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="topology-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """topology_changes must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="topology-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__topology_changes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_topology_changes(self):
    self.__topology_changes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="topology-changes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)


  def _get_last_topology_change(self):
    """
    Getter method for last_topology_change, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/last_topology_change (oc-types:timeticks64)

    YANG Description: The time at which the last topology change was
detected by the bridge entity. The value is
expressed relative to the Unix Epoch (Jan 1, 1970
00:00:00 UTC).
    """
    return self.__last_topology_change
      
  def _set_last_topology_change(self, v, load=False):
    """
    Setter method for last_topology_change, mapped from YANG variable /stp/mstp/mst_instances/mst_instance/state/last_topology_change (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_topology_change is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_topology_change() directly.

    YANG Description: The time at which the last topology change was
detected by the bridge entity. The value is
expressed relative to the Unix Epoch (Jan 1, 1970
00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-topology-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_topology_change must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-topology-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__last_topology_change = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_topology_change(self):
    self.__last_topology_change = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="last-topology-change", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-types:timeticks64', is_config=False)

  mst_id = __builtin__.property(_get_mst_id)
  vlan = __builtin__.property(_get_vlan)
  bridge_priority = __builtin__.property(_get_bridge_priority)
  bridge_address = __builtin__.property(_get_bridge_address)
  designated_root_priority = __builtin__.property(_get_designated_root_priority)
  designated_root_address = __builtin__.property(_get_designated_root_address)
  root_port = __builtin__.property(_get_root_port)
  root_cost = __builtin__.property(_get_root_cost)
  hold_time = __builtin__.property(_get_hold_time)
  topology_changes = __builtin__.property(_get_topology_changes)
  last_topology_change = __builtin__.property(_get_last_topology_change)


  _pyangbind_elements = OrderedDict([('mst_id', mst_id), ('vlan', vlan), ('bridge_priority', bridge_priority), ('bridge_address', bridge_address), ('designated_root_priority', designated_root_priority), ('designated_root_address', designated_root_address), ('root_port', root_port), ('root_cost', root_cost), ('hold_time', hold_time), ('topology_changes', topology_changes), ('last_topology_change', last_topology_change), ])



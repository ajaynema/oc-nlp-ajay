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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv/administrative-groups/admin-group/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the administrative
groups being described for the link
  """
  __slots__ = ('_path_helper', '_extmethods', '__bit_index','__set_',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bit_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__set_ = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'link', 'sub-tlvs', 'sub-tlv', 'administrative-groups', 'admin-group', 'state']

  def _get_bit_index(self):
    """
    Getter method for bit_index, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/bit_index (uint8)

    YANG Description: The index of the bit within the 32-bit administrative group field
of the Administrative Group sub-TLV of the Traffic Engineering LSA
    """
    return self.__bit_index
      
  def _set_bit_index(self, v, load=False):
    """
    Setter method for bit_index, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/bit_index (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bit_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bit_index() directly.

    YANG Description: The index of the bit within the 32-bit administrative group field
of the Administrative Group sub-TLV of the Traffic Engineering LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bit_index must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__bit_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bit_index(self):
    self.__bit_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_set_(self):
    """
    Getter method for set_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/set (boolean)

    YANG Description: Whether the bit is set within the administrative group field
    """
    return self.__set_
      
  def _set_set_(self, v, load=False):
    """
    Setter method for set_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/set (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_() directly.

    YANG Description: Whether the bit is set within the administrative group field
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__set_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_(self):
    self.__set_ = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  bit_index = __builtin__.property(_get_bit_index)
  set_ = __builtin__.property(_get_set_)


  _pyangbind_elements = OrderedDict([('bit_index', bit_index), ('set_', set_), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv/administrative-groups/admin-group/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters relating to the administrative
groups being described for the link
  """
  __slots__ = ('_path_helper', '_extmethods', '__bit_index','__set_',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bit_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__set_ = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'traffic-engineering', 'tlvs', 'tlv', 'link', 'sub-tlvs', 'sub-tlv', 'administrative-groups', 'admin-group', 'state']

  def _get_bit_index(self):
    """
    Getter method for bit_index, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/bit_index (uint8)

    YANG Description: The index of the bit within the 32-bit administrative group field
of the Administrative Group sub-TLV of the Traffic Engineering LSA
    """
    return self.__bit_index
      
  def _set_bit_index(self, v, load=False):
    """
    Setter method for bit_index, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/bit_index (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bit_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bit_index() directly.

    YANG Description: The index of the bit within the 32-bit administrative group field
of the Administrative Group sub-TLV of the Traffic Engineering LSA
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bit_index must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__bit_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bit_index(self):
    self.__bit_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..31']}), is_leaf=True, yang_name="bit-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_set_(self):
    """
    Getter method for set_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/set (boolean)

    YANG Description: Whether the bit is set within the administrative group field
    """
    return self.__set_
      
  def _set_set_(self, v, load=False):
    """
    Setter method for set_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups/admin_group/state/set (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_() directly.

    YANG Description: Whether the bit is set within the administrative group field
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_ must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__set_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_(self):
    self.__set_ = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  bit_index = __builtin__.property(_get_bit_index)
  set_ = __builtin__.property(_get_set_)


  _pyangbind_elements = OrderedDict([('bit_index', bit_index), ('set_', set_), ])



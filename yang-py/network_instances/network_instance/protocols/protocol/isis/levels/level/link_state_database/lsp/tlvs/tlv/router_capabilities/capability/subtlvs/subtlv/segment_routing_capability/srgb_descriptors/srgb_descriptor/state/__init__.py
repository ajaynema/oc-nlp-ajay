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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors/srgb-descriptor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the SR range
  """
  __slots__ = ('_path_helper', '_extmethods', '__range','__label',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__range = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors', 'srgb-descriptor', 'state']

  def _get_range(self):
    """
    Getter method for range, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/range (uint32)

    YANG Description: Number of SRGB elements. The range
value MUST be greater than 0.
    """
    return self.__range
      
  def _set_range(self, v, load=False):
    """
    Setter method for range, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/range (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range() directly.

    YANG Description: Number of SRGB elements. The range
value MUST be greater than 0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range(self):
    self.__range = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_label(self):
    """
    Getter method for label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/label (oc-mplst:mpls-label)

    YANG Description: The first value of the SRGB when
expressed as an MPLS label.
    """
    return self.__label
      
  def _set_label(self, v, load=False):
    """
    Setter method for label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label() directly.

    YANG Description: The first value of the SRGB when
expressed as an MPLS label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label(self):
    self.__label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

  range = __builtin__.property(_get_range)
  label = __builtin__.property(_get_label)


  _pyangbind_elements = OrderedDict([('range', range), ('label', label), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors/srgb-descriptor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the SR range
  """
  __slots__ = ('_path_helper', '_extmethods', '__range','__label',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__range = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors', 'srgb-descriptor', 'state']

  def _get_range(self):
    """
    Getter method for range, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/range (uint32)

    YANG Description: Number of SRGB elements. The range
value MUST be greater than 0.
    """
    return self.__range
      
  def _set_range(self, v, load=False):
    """
    Setter method for range, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/range (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_range() directly.

    YANG Description: Number of SRGB elements. The range
value MUST be greater than 0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """range must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_range(self):
    self.__range = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_label(self):
    """
    Getter method for label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/label (oc-mplst:mpls-label)

    YANG Description: The first value of the SRGB when
expressed as an MPLS label.
    """
    return self.__label
      
  def _set_label(self, v, load=False):
    """
    Setter method for label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor/state/label (oc-mplst:mpls-label)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label() directly.

    YANG Description: The first value of the SRGB when
expressed as an MPLS label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label must be of a type compatible with oc-mplst:mpls-label""",
          'defined-type': "oc-mplst:mpls-label",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)""",
        })

    self.__label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label(self):
    self.__label = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['16..1048575']}),RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'IPV4_EXPLICIT_NULL': {'value': 0}, 'ROUTER_ALERT': {'value': 1}, 'IPV6_EXPLICIT_NULL': {'value': 2}, 'IMPLICIT_NULL': {'value': 3}, 'ENTROPY_LABEL_INDICATOR': {'value': 7}, 'NO_LABEL': {}},),], is_leaf=True, yang_name="label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:mpls-label', is_config=False)

  range = __builtin__.property(_get_range)
  label = __builtin__.property(_get_label)


  _pyangbind_elements = OrderedDict([('range', range), ('label', label), ])



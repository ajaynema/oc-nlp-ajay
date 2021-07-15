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

class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/segment-routing/te-policies/te-policy/candidate-paths/candidate-path/segment-lists/segment-list/next-hops/next-hop/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The counters of traffic steered to the segment-list on
per next-hop basis.
  """
  __slots__ = ('_path_helper', '_extmethods', '__out_pkts','__out_octets','__out_labeled_pkts','__out_labeled_octets',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_labeled_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_labeled_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)

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
      return ['network-instances', 'network-instance', 'segment-routing', 'te-policies', 'te-policy', 'candidate-paths', 'candidate-path', 'segment-lists', 'segment-list', 'next-hops', 'next-hop', 'state', 'counters']

  def _get_out_pkts(self):
    """
    Getter method for out_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_pkts (oc-yang:counter64)

    YANG Description: A cumulative counter of the outgoing packets steered to the
segment list. The counter includes both labeled and unlabeled
steered traffic.
    """
    return self.__out_pkts
      
  def _set_out_pkts(self, v, load=False):
    """
    Setter method for out_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_pkts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts() directly.

    YANG Description: A cumulative counter of the outgoing packets steered to the
segment list. The counter includes both labeled and unlabeled
steered traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts(self):
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_octets(self):
    """
    Getter method for out_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_octets (oc-yang:counter64)

    YANG Description: The cumulative counter of the total outgoing bytes steered
to the segment list. The counter includes both labeled and
unlabeled steerted traffic.
    """
    return self.__out_octets
      
  def _set_out_octets(self, v, load=False):
    """
    Setter method for out_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_octets() directly.

    YANG Description: The cumulative counter of the total outgoing bytes steered
to the segment list. The counter includes both labeled and
unlabeled steerted traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_octets(self):
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_labeled_pkts(self):
    """
    Getter method for out_labeled_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_pkts (oc-yang:counter64)

    YANG Description: A cumulative counter of the incoming labeled packets steered
to the segment list.
    """
    return self.__out_labeled_pkts
      
  def _set_out_labeled_pkts(self, v, load=False):
    """
    Setter method for out_labeled_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_pkts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_labeled_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_labeled_pkts() directly.

    YANG Description: A cumulative counter of the incoming labeled packets steered
to the segment list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_labeled_pkts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_labeled_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_labeled_pkts(self):
    self.__out_labeled_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_labeled_octets(self):
    """
    Getter method for out_labeled_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_octets (oc-yang:counter64)

    YANG Description: A cumulative counter of the total bytes of incoming labeled
traffic steered to the segment list.
    """
    return self.__out_labeled_octets
      
  def _set_out_labeled_octets(self, v, load=False):
    """
    Setter method for out_labeled_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_labeled_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_labeled_octets() directly.

    YANG Description: A cumulative counter of the total bytes of incoming labeled
traffic steered to the segment list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_labeled_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_labeled_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_labeled_octets(self):
    self.__out_labeled_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)

  out_pkts = __builtin__.property(_get_out_pkts)
  out_octets = __builtin__.property(_get_out_octets)
  out_labeled_pkts = __builtin__.property(_get_out_labeled_pkts)
  out_labeled_octets = __builtin__.property(_get_out_labeled_octets)


  _pyangbind_elements = OrderedDict([('out_pkts', out_pkts), ('out_octets', out_octets), ('out_labeled_pkts', out_labeled_pkts), ('out_labeled_octets', out_labeled_octets), ])


class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/segment-routing/te-policies/te-policy/candidate-paths/candidate-path/segment-lists/segment-list/next-hops/next-hop/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The counters of traffic steered to the segment-list on
per next-hop basis.
  """
  __slots__ = ('_path_helper', '_extmethods', '__out_pkts','__out_octets','__out_labeled_pkts','__out_labeled_octets',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_labeled_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    self.__out_labeled_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)

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
      return ['network-instances', 'network-instance', 'segment-routing', 'te-policies', 'te-policy', 'candidate-paths', 'candidate-path', 'segment-lists', 'segment-list', 'next-hops', 'next-hop', 'state', 'counters']

  def _get_out_pkts(self):
    """
    Getter method for out_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_pkts (oc-yang:counter64)

    YANG Description: A cumulative counter of the outgoing packets steered to the
segment list. The counter includes both labeled and unlabeled
steered traffic.
    """
    return self.__out_pkts
      
  def _set_out_pkts(self, v, load=False):
    """
    Setter method for out_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_pkts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts() directly.

    YANG Description: A cumulative counter of the outgoing packets steered to the
segment list. The counter includes both labeled and unlabeled
steered traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts(self):
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_octets(self):
    """
    Getter method for out_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_octets (oc-yang:counter64)

    YANG Description: The cumulative counter of the total outgoing bytes steered
to the segment list. The counter includes both labeled and
unlabeled steerted traffic.
    """
    return self.__out_octets
      
  def _set_out_octets(self, v, load=False):
    """
    Setter method for out_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_octets() directly.

    YANG Description: The cumulative counter of the total outgoing bytes steered
to the segment list. The counter includes both labeled and
unlabeled steerted traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_octets(self):
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_labeled_pkts(self):
    """
    Getter method for out_labeled_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_pkts (oc-yang:counter64)

    YANG Description: A cumulative counter of the incoming labeled packets steered
to the segment list.
    """
    return self.__out_labeled_pkts
      
  def _set_out_labeled_pkts(self, v, load=False):
    """
    Setter method for out_labeled_pkts, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_pkts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_labeled_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_labeled_pkts() directly.

    YANG Description: A cumulative counter of the incoming labeled packets steered
to the segment list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_labeled_pkts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_labeled_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_labeled_pkts(self):
    self.__out_labeled_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)


  def _get_out_labeled_octets(self):
    """
    Getter method for out_labeled_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_octets (oc-yang:counter64)

    YANG Description: A cumulative counter of the total bytes of incoming labeled
traffic steered to the segment list.
    """
    return self.__out_labeled_octets
      
  def _set_out_labeled_octets(self, v, load=False):
    """
    Setter method for out_labeled_octets, mapped from YANG variable /network_instances/network_instance/segment_routing/te_policies/te_policy/candidate_paths/candidate_path/segment_lists/segment_list/next_hops/next_hop/state/counters/out_labeled_octets (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_labeled_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_labeled_octets() directly.

    YANG Description: A cumulative counter of the total bytes of incoming labeled
traffic steered to the segment list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_labeled_octets must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__out_labeled_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_labeled_octets(self):
    self.__out_labeled_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-labeled-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-yang:counter64', is_config=False)

  out_pkts = __builtin__.property(_get_out_pkts)
  out_octets = __builtin__.property(_get_out_octets)
  out_labeled_pkts = __builtin__.property(_get_out_labeled_pkts)
  out_labeled_octets = __builtin__.property(_get_out_labeled_octets)


  _pyangbind_elements = OrderedDict([('out_pkts', out_pkts), ('out_octets', out_octets), ('out_labeled_pkts', out_labeled_pkts), ('out_labeled_octets', out_labeled_octets), ])



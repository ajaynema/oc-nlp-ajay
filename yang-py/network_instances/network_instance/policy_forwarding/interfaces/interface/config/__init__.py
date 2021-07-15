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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to an interface to
policy forwarding rule binding.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__apply_forwarding_policy','__apply_vrf_selection_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    self.__apply_forwarding_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__apply_vrf_selection_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'interfaces', 'interface', 'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: A unique identifier for the interface.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: A unique identifier for the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_apply_forwarding_policy(self):
    """
    Getter method for apply_forwarding_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_forwarding_policy (leafref)

    YANG Description: The policy to be applied on the interface. Packets ingress on
the referenced interface should be compared to the match
criteria within the specified policy, and in the case that
these criteria are met, the forwarding actions specified
applied. These policies should be applied following quality of
service classification, and ACL actions if such entities are
referenced by the corresponding interface.
    """
    return self.__apply_forwarding_policy
      
  def _set_apply_forwarding_policy(self, v, load=False):
    """
    Setter method for apply_forwarding_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_forwarding_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_forwarding_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_forwarding_policy() directly.

    YANG Description: The policy to be applied on the interface. Packets ingress on
the referenced interface should be compared to the match
criteria within the specified policy, and in the case that
these criteria are met, the forwarding actions specified
applied. These policies should be applied following quality of
service classification, and ACL actions if such entities are
referenced by the corresponding interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_forwarding_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__apply_forwarding_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_forwarding_policy(self):
    self.__apply_forwarding_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_apply_vrf_selection_policy(self):
    """
    Getter method for apply_vrf_selection_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_vrf_selection_policy (leafref)

    YANG Description: Apply the specific VRF selection policy on the interface. The referenced policy
MUST be of type VRF_SELECTION_POLICY. The VRF selection policy may coexist with
a policy-forwarding policy.

The policy specified in this leaf is used to specifically choose the L3VRF network
instance that is used for specific input criteria of packets.
    """
    return self.__apply_vrf_selection_policy
      
  def _set_apply_vrf_selection_policy(self, v, load=False):
    """
    Setter method for apply_vrf_selection_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_vrf_selection_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_vrf_selection_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_vrf_selection_policy() directly.

    YANG Description: Apply the specific VRF selection policy on the interface. The referenced policy
MUST be of type VRF_SELECTION_POLICY. The VRF selection policy may coexist with
a policy-forwarding policy.

The policy specified in this leaf is used to specifically choose the L3VRF network
instance that is used for specific input criteria of packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_vrf_selection_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__apply_vrf_selection_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_vrf_selection_policy(self):
    self.__apply_vrf_selection_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  apply_forwarding_policy = __builtin__.property(_get_apply_forwarding_policy, _set_apply_forwarding_policy)
  apply_vrf_selection_policy = __builtin__.property(_get_apply_vrf_selection_policy, _set_apply_vrf_selection_policy)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('apply_forwarding_policy', apply_forwarding_policy), ('apply_vrf_selection_policy', apply_vrf_selection_policy), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to an interface to
policy forwarding rule binding.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__apply_forwarding_policy','__apply_vrf_selection_policy',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    self.__apply_forwarding_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__apply_vrf_selection_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

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
      return ['network-instances', 'network-instance', 'policy-forwarding', 'interfaces', 'interface', 'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: A unique identifier for the interface.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: A unique identifier for the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_apply_forwarding_policy(self):
    """
    Getter method for apply_forwarding_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_forwarding_policy (leafref)

    YANG Description: The policy to be applied on the interface. Packets ingress on
the referenced interface should be compared to the match
criteria within the specified policy, and in the case that
these criteria are met, the forwarding actions specified
applied. These policies should be applied following quality of
service classification, and ACL actions if such entities are
referenced by the corresponding interface.
    """
    return self.__apply_forwarding_policy
      
  def _set_apply_forwarding_policy(self, v, load=False):
    """
    Setter method for apply_forwarding_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_forwarding_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_forwarding_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_forwarding_policy() directly.

    YANG Description: The policy to be applied on the interface. Packets ingress on
the referenced interface should be compared to the match
criteria within the specified policy, and in the case that
these criteria are met, the forwarding actions specified
applied. These policies should be applied following quality of
service classification, and ACL actions if such entities are
referenced by the corresponding interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_forwarding_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__apply_forwarding_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_forwarding_policy(self):
    self.__apply_forwarding_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-forwarding-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_apply_vrf_selection_policy(self):
    """
    Getter method for apply_vrf_selection_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_vrf_selection_policy (leafref)

    YANG Description: Apply the specific VRF selection policy on the interface. The referenced policy
MUST be of type VRF_SELECTION_POLICY. The VRF selection policy may coexist with
a policy-forwarding policy.

The policy specified in this leaf is used to specifically choose the L3VRF network
instance that is used for specific input criteria of packets.
    """
    return self.__apply_vrf_selection_policy
      
  def _set_apply_vrf_selection_policy(self, v, load=False):
    """
    Setter method for apply_vrf_selection_policy, mapped from YANG variable /network_instances/network_instance/policy_forwarding/interfaces/interface/config/apply_vrf_selection_policy (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_apply_vrf_selection_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_apply_vrf_selection_policy() directly.

    YANG Description: Apply the specific VRF selection policy on the interface. The referenced policy
MUST be of type VRF_SELECTION_POLICY. The VRF selection policy may coexist with
a policy-forwarding policy.

The policy specified in this leaf is used to specifically choose the L3VRF network
instance that is used for specific input criteria of packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """apply_vrf_selection_policy must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__apply_vrf_selection_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_apply_vrf_selection_policy(self):
    self.__apply_vrf_selection_policy = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="apply-vrf-selection-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  apply_forwarding_policy = __builtin__.property(_get_apply_forwarding_policy, _set_apply_forwarding_policy)
  apply_vrf_selection_policy = __builtin__.property(_get_apply_vrf_selection_policy, _set_apply_vrf_selection_policy)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('apply_forwarding_policy', apply_forwarding_policy), ('apply_vrf_selection_policy', apply_vrf_selection_policy), ])



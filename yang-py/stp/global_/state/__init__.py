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
  from YANG module openconfig-spanning-tree - based on the path /stp/global/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global spanning tree state
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled_protocol','__bridge_assurance','__etherchannel_misconfig_guard','__bpduguard_timeout_recovery','__loop_guard','__bpdu_guard','__bpdu_filter',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled_protocol = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}},)), is_leaf=False, yang_name="enabled-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='identityref', is_config=False)
    self.__bridge_assurance = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bridge-assurance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    self.__etherchannel_misconfig_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etherchannel-misconfig-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    self.__bpduguard_timeout_recovery = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="bpduguard-timeout-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)
    self.__loop_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="loop-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    self.__bpdu_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    self.__bpdu_filter = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)

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
      return ['stp', 'global', 'state']

  def _get_enabled_protocol(self):
    """
    Getter method for enabled_protocol, mapped from YANG variable /stp/global/state/enabled_protocol (identityref)

    YANG Description: List of the spanning tree protocols enabled on the
device
    """
    return self.__enabled_protocol
      
  def _set_enabled_protocol(self, v, load=False):
    """
    Setter method for enabled_protocol, mapped from YANG variable /stp/global/state/enabled_protocol (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled_protocol() directly.

    YANG Description: List of the spanning tree protocols enabled on the
device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}},)), is_leaf=False, yang_name="enabled-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled_protocol must be of a type compatible with identityref""",
          'defined-type': "openconfig-spanning-tree:identityref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}},)), is_leaf=False, yang_name="enabled-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='identityref', is_config=False)""",
        })

    self.__enabled_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled_protocol(self):
    self.__enabled_protocol = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:MSTP': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}, 'oc-stp-types:RAPID_PVST': {'@module': 'openconfig-spanning-tree-types', '@namespace': 'http://openconfig.net/yang/spanning-tree/types'}},)), is_leaf=False, yang_name="enabled-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='identityref', is_config=False)


  def _get_bridge_assurance(self):
    """
    Getter method for bridge_assurance, mapped from YANG variable /stp/global/state/bridge_assurance (boolean)

    YANG Description: Enable bridge assurance to protect against unidirectional
link failure
    """
    return self.__bridge_assurance
      
  def _set_bridge_assurance(self, v, load=False):
    """
    Setter method for bridge_assurance, mapped from YANG variable /stp/global/state/bridge_assurance (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_assurance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_assurance() directly.

    YANG Description: Enable bridge assurance to protect against unidirectional
link failure
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bridge-assurance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_assurance must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bridge-assurance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)""",
        })

    self.__bridge_assurance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_assurance(self):
    self.__bridge_assurance = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bridge-assurance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)


  def _get_etherchannel_misconfig_guard(self):
    """
    Getter method for etherchannel_misconfig_guard, mapped from YANG variable /stp/global/state/etherchannel_misconfig_guard (boolean)

    YANG Description: EtherChannel guard detects a misconfigured EtherChannel
when interfaces on the switch are configured as an
EtherChannel while interfaces on the other device are not
or when not all the interfaces on the other device are in
the same EtherChannel.
    """
    return self.__etherchannel_misconfig_guard
      
  def _set_etherchannel_misconfig_guard(self, v, load=False):
    """
    Setter method for etherchannel_misconfig_guard, mapped from YANG variable /stp/global/state/etherchannel_misconfig_guard (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_etherchannel_misconfig_guard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_etherchannel_misconfig_guard() directly.

    YANG Description: EtherChannel guard detects a misconfigured EtherChannel
when interfaces on the switch are configured as an
EtherChannel while interfaces on the other device are not
or when not all the interfaces on the other device are in
the same EtherChannel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="etherchannel-misconfig-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """etherchannel_misconfig_guard must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etherchannel-misconfig-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)""",
        })

    self.__etherchannel_misconfig_guard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_etherchannel_misconfig_guard(self):
    self.__etherchannel_misconfig_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etherchannel-misconfig-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)


  def _get_bpduguard_timeout_recovery(self):
    """
    Getter method for bpduguard_timeout_recovery, mapped from YANG variable /stp/global/state/bpduguard_timeout_recovery (uint8)

    YANG Description: Amount of time, in seconds, the interface receiving BPDUs
is disabled. Once the timeout expires, the interface is
brought back into service.
    """
    return self.__bpduguard_timeout_recovery
      
  def _set_bpduguard_timeout_recovery(self, v, load=False):
    """
    Setter method for bpduguard_timeout_recovery, mapped from YANG variable /stp/global/state/bpduguard_timeout_recovery (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpduguard_timeout_recovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpduguard_timeout_recovery() directly.

    YANG Description: Amount of time, in seconds, the interface receiving BPDUs
is disabled. Once the timeout expires, the interface is
brought back into service.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="bpduguard-timeout-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpduguard_timeout_recovery must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="bpduguard-timeout-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)""",
        })

    self.__bpduguard_timeout_recovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpduguard_timeout_recovery(self):
    self.__bpduguard_timeout_recovery = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="bpduguard-timeout-recovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=False)


  def _get_loop_guard(self):
    """
    Getter method for loop_guard, mapped from YANG variable /stp/global/state/loop_guard (boolean)

    YANG Description: The loop guard default setting for the bridge
    """
    return self.__loop_guard
      
  def _set_loop_guard(self, v, load=False):
    """
    Setter method for loop_guard, mapped from YANG variable /stp/global/state/loop_guard (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_loop_guard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_loop_guard() directly.

    YANG Description: The loop guard default setting for the bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="loop-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """loop_guard must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="loop-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)""",
        })

    self.__loop_guard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_loop_guard(self):
    self.__loop_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="loop-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)


  def _get_bpdu_guard(self):
    """
    Getter method for bpdu_guard, mapped from YANG variable /stp/global/state/bpdu_guard (boolean)

    YANG Description: Enable edge port BPDU guard
    """
    return self.__bpdu_guard
      
  def _set_bpdu_guard(self, v, load=False):
    """
    Setter method for bpdu_guard, mapped from YANG variable /stp/global/state/bpdu_guard (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_guard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_guard() directly.

    YANG Description: Enable edge port BPDU guard
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_guard must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)""",
        })

    self.__bpdu_guard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_guard(self):
    self.__bpdu_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)


  def _get_bpdu_filter(self):
    """
    Getter method for bpdu_filter, mapped from YANG variable /stp/global/state/bpdu_filter (boolean)

    YANG Description: Enable edge port BPDU filter
    """
    return self.__bpdu_filter
      
  def _set_bpdu_filter(self, v, load=False):
    """
    Setter method for bpdu_filter, mapped from YANG variable /stp/global/state/bpdu_filter (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_filter() directly.

    YANG Description: Enable edge port BPDU filter
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_filter must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)""",
        })

    self.__bpdu_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_filter(self):
    self.__bpdu_filter = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='boolean', is_config=False)

  enabled_protocol = __builtin__.property(_get_enabled_protocol)
  bridge_assurance = __builtin__.property(_get_bridge_assurance)
  etherchannel_misconfig_guard = __builtin__.property(_get_etherchannel_misconfig_guard)
  bpduguard_timeout_recovery = __builtin__.property(_get_bpduguard_timeout_recovery)
  loop_guard = __builtin__.property(_get_loop_guard)
  bpdu_guard = __builtin__.property(_get_bpdu_guard)
  bpdu_filter = __builtin__.property(_get_bpdu_filter)


  _pyangbind_elements = OrderedDict([('enabled_protocol', enabled_protocol), ('bridge_assurance', bridge_assurance), ('etherchannel_misconfig_guard', etherchannel_misconfig_guard), ('bpduguard_timeout_recovery', bpduguard_timeout_recovery), ('loop_guard', loop_guard), ('bpdu_guard', bpdu_guard), ('bpdu_filter', bpdu_filter), ])



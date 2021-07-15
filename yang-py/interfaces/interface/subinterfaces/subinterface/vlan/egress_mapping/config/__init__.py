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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/egress-mapping/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for egress VLAN stack behaviors for
packets that are destined for output via this subinterface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_stack_action','__vlan_id','__tpid',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_stack_action = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'egress-mapping', 'config']

  def _get_vlan_stack_action(self):
    """
    Getter method for vlan_stack_action, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_stack_action (oc-vlan-types:vlan-stack-action)

    YANG Description: The action to take on the VLAN stack of a packet. This is
optionally used in conjunction with adjacent leaves to override
the values of the action.
    """
    return self.__vlan_stack_action
      
  def _set_vlan_stack_action(self, v, load=False):
    """
    Setter method for vlan_stack_action, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_stack_action (oc-vlan-types:vlan-stack-action)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_stack_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_stack_action() directly.

    YANG Description: The action to take on the VLAN stack of a packet. This is
optionally used in conjunction with adjacent leaves to override
the values of the action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_stack_action must be of a type compatible with oc-vlan-types:vlan-stack-action""",
          'defined-type': "oc-vlan-types:vlan-stack-action",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)""",
        })

    self.__vlan_stack_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_stack_action(self):
    self.__vlan_stack_action = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_id (oc-vlan-types:vlan-id)

    YANG Description: Optionally specifies a fixed VLAN identifier that is used by the
action configured in 'vlan-stack-action'. For example, if the action
is 'POP' then a VLAN identifier is removed from the stack but the
value of this leaf is used instead. This value must be non-zero if
the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Optionally specifies a fixed VLAN identifier that is used by the
action configured in 'vlan-stack-action'. For example, if the action
is 'POP' then a VLAN identifier is removed from the stack but the
value of this leaf is used instead. This value must be non-zero if
the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_tpid(self):
    """
    Getter method for tpid, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/tpid (identityref)

    YANG Description: Optionally override the tag protocol identifier field (TPID) that
is used by the action configured by 'vlan-stack-action' when
modifying the VLAN stack.
    """
    return self.__tpid
      
  def _set_tpid(self, v, load=False):
    """
    Setter method for tpid, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/tpid (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tpid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tpid() directly.

    YANG Description: Optionally override the tag protocol identifier field (TPID) that
is used by the action configured by 'vlan-stack-action' when
modifying the VLAN stack.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tpid must be of a type compatible with identityref""",
          'defined-type': "openconfig-vlan:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)""",
        })

    self.__tpid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tpid(self):
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

  vlan_stack_action = __builtin__.property(_get_vlan_stack_action, _set_vlan_stack_action)
  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  tpid = __builtin__.property(_get_tpid, _set_tpid)


  _pyangbind_elements = OrderedDict([('vlan_stack_action', vlan_stack_action), ('vlan_id', vlan_id), ('tpid', tpid), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan/egress-mapping/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for egress VLAN stack behaviors for
packets that are destined for output via this subinterface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__vlan_stack_action','__vlan_id','__tpid',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__vlan_stack_action = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan', 'egress-mapping', 'config']

  def _get_vlan_stack_action(self):
    """
    Getter method for vlan_stack_action, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_stack_action (oc-vlan-types:vlan-stack-action)

    YANG Description: The action to take on the VLAN stack of a packet. This is
optionally used in conjunction with adjacent leaves to override
the values of the action.
    """
    return self.__vlan_stack_action
      
  def _set_vlan_stack_action(self, v, load=False):
    """
    Setter method for vlan_stack_action, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_stack_action (oc-vlan-types:vlan-stack-action)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_stack_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_stack_action() directly.

    YANG Description: The action to take on the VLAN stack of a packet. This is
optionally used in conjunction with adjacent leaves to override
the values of the action.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_stack_action must be of a type compatible with oc-vlan-types:vlan-stack-action""",
          'defined-type': "oc-vlan-types:vlan-stack-action",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)""",
        })

    self.__vlan_stack_action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_stack_action(self):
    self.__vlan_stack_action = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'PUSH': {}, 'POP': {}, 'SWAP': {}},), is_leaf=True, yang_name="vlan-stack-action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-stack-action', is_config=True)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_id (oc-vlan-types:vlan-id)

    YANG Description: Optionally specifies a fixed VLAN identifier that is used by the
action configured in 'vlan-stack-action'. For example, if the action
is 'POP' then a VLAN identifier is removed from the stack but the
value of this leaf is used instead. This value must be non-zero if
the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/vlan_id (oc-vlan-types:vlan-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Optionally specifies a fixed VLAN identifier that is used by the
action configured in 'vlan-stack-action'. For example, if the action
is 'POP' then a VLAN identifier is removed from the stack but the
value of this leaf is used instead. This value must be non-zero if
the 'vlan-stack-action' is one of 'PUSH' or 'SWAP'.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with oc-vlan-types:vlan-id""",
          'defined-type': "oc-vlan-types:vlan-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}), is_leaf=True, yang_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-id', is_config=True)


  def _get_tpid(self):
    """
    Getter method for tpid, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/tpid (identityref)

    YANG Description: Optionally override the tag protocol identifier field (TPID) that
is used by the action configured by 'vlan-stack-action' when
modifying the VLAN stack.
    """
    return self.__tpid
      
  def _set_tpid(self, v, load=False):
    """
    Setter method for tpid, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping/config/tpid (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tpid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tpid() directly.

    YANG Description: Optionally override the tag protocol identifier field (TPID) that
is used by the action configured by 'vlan-stack-action' when
modifying the VLAN stack.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tpid must be of a type compatible with identityref""",
          'defined-type': "openconfig-vlan:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)""",
        })

    self.__tpid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tpid(self):
    self.__tpid = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X8100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X88A8': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9100': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_0X9200': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}, 'oc-vlan-types:TPID_ANY': {'@module': 'openconfig-vlan-types', '@namespace': 'http://openconfig.net/yang/vlan-types'}},), is_leaf=True, yang_name="tpid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='identityref', is_config=True)

  vlan_stack_action = __builtin__.property(_get_vlan_stack_action, _set_vlan_stack_action)
  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  tpid = __builtin__.property(_get_tpid, _set_tpid)


  _pyangbind_elements = OrderedDict([('vlan_stack_action', vlan_stack_action), ('vlan_id', vlan_id), ('tpid', tpid), ])



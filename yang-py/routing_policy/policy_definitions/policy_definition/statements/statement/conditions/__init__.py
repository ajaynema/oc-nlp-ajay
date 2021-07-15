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

from . import config
from . import state
from . import match_interface
from . import match_prefix_set
from . import match_neighbor_set
from . import match_tag_set
class conditions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/conditions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Condition statements for the current policy statement
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__match_interface','__match_prefix_set','__match_neighbor_set','__match_tag_set',)

  _yang_name = 'conditions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__match_interface = YANGDynClass(base=match_interface.match_interface, is_container='container', yang_name="match-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__match_prefix_set = YANGDynClass(base=match_prefix_set.match_prefix_set, is_container='container', yang_name="match-prefix-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__match_neighbor_set = YANGDynClass(base=match_neighbor_set.match_neighbor_set, is_container='container', yang_name="match-neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__match_tag_set = YANGDynClass(base=match_tag_set.match_tag_set, is_container='container', yang_name="match-tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'conditions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/config (container)

    YANG Description: Configuration data for policy conditions
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for policy conditions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/state (container)

    YANG Description: Operational state data for policy conditions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for policy conditions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_match_interface(self):
    """
    Getter method for match_interface, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_interface (container)

    YANG Description: Top-level container for interface match conditions
    """
    return self.__match_interface
      
  def _set_match_interface(self, v, load=False):
    """
    Setter method for match_interface, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_interface() directly.

    YANG Description: Top-level container for interface match conditions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match_interface.match_interface, is_container='container', yang_name="match-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match_interface.match_interface, is_container='container', yang_name="match-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__match_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_interface(self):
    self.__match_interface = YANGDynClass(base=match_interface.match_interface, is_container='container', yang_name="match-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_match_prefix_set(self):
    """
    Getter method for match_prefix_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_prefix_set (container)

    YANG Description: Match a referenced prefix-set according to the logic
defined in the match-set-options leaf
    """
    return self.__match_prefix_set
      
  def _set_match_prefix_set(self, v, load=False):
    """
    Setter method for match_prefix_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_prefix_set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_prefix_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_prefix_set() directly.

    YANG Description: Match a referenced prefix-set according to the logic
defined in the match-set-options leaf
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match_prefix_set.match_prefix_set, is_container='container', yang_name="match-prefix-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_prefix_set must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match_prefix_set.match_prefix_set, is_container='container', yang_name="match-prefix-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__match_prefix_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_prefix_set(self):
    self.__match_prefix_set = YANGDynClass(base=match_prefix_set.match_prefix_set, is_container='container', yang_name="match-prefix-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_match_neighbor_set(self):
    """
    Getter method for match_neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set (container)

    YANG Description: Match a referenced neighbor set according to the logic
defined in the match-set-options-leaf
    """
    return self.__match_neighbor_set
      
  def _set_match_neighbor_set(self, v, load=False):
    """
    Setter method for match_neighbor_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_neighbor_set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_neighbor_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_neighbor_set() directly.

    YANG Description: Match a referenced neighbor set according to the logic
defined in the match-set-options-leaf
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match_neighbor_set.match_neighbor_set, is_container='container', yang_name="match-neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_neighbor_set must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match_neighbor_set.match_neighbor_set, is_container='container', yang_name="match-neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__match_neighbor_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_neighbor_set(self):
    self.__match_neighbor_set = YANGDynClass(base=match_neighbor_set.match_neighbor_set, is_container='container', yang_name="match-neighbor-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_match_tag_set(self):
    """
    Getter method for match_tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set (container)

    YANG Description: Match a referenced tag set according to the logic defined
in the match-options-set leaf
    """
    return self.__match_tag_set
      
  def _set_match_tag_set(self, v, load=False):
    """
    Setter method for match_tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/conditions/match_tag_set (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match_tag_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match_tag_set() directly.

    YANG Description: Match a referenced tag set according to the logic defined
in the match-options-set leaf
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match_tag_set.match_tag_set, is_container='container', yang_name="match-tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match_tag_set must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match_tag_set.match_tag_set, is_container='container', yang_name="match-tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__match_tag_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match_tag_set(self):
    self.__match_tag_set = YANGDynClass(base=match_tag_set.match_tag_set, is_container='container', yang_name="match-tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  match_interface = __builtin__.property(_get_match_interface, _set_match_interface)
  match_prefix_set = __builtin__.property(_get_match_prefix_set, _set_match_prefix_set)
  match_neighbor_set = __builtin__.property(_get_match_neighbor_set, _set_match_neighbor_set)
  match_tag_set = __builtin__.property(_get_match_tag_set, _set_match_tag_set)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('match_interface', match_interface), ('match_prefix_set', match_prefix_set), ('match_neighbor_set', match_neighbor_set), ('match_tag_set', match_tag_set), ])



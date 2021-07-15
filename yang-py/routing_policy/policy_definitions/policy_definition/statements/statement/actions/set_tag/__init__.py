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
from . import inline
from . import reference
class set_tag(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/set-tag. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Policy actions associated with setting tags for a particular
route. A tag is an abstract entity which can be mapped to underlying
protocol attributes where applicable.
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__inline','__reference',)

  _yang_name = 'set-tag'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__inline = YANGDynClass(base=inline.inline, is_container='container', yang_name="inline", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__reference = YANGDynClass(base=reference.reference, is_container='container', yang_name="reference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'set-tag']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/config (container)

    YANG Description: Configuration of tag application
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration of tag application
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
    Getter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/state (container)

    YANG Description: Operational state related to tag application.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state related to tag application.
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


  def _get_inline(self):
    """
    Getter method for inline, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/inline (container)

    YANG Description: The tags specified in this container are set on a route using
the values directly. It is applicable when the mode of application
is explicitly specified as INLINE.
    """
    return self.__inline
      
  def _set_inline(self, v, load=False):
    """
    Setter method for inline, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/inline (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inline is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inline() directly.

    YANG Description: The tags specified in this container are set on a route using
the values directly. It is applicable when the mode of application
is explicitly specified as INLINE.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=inline.inline, is_container='container', yang_name="inline", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inline must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=inline.inline, is_container='container', yang_name="inline", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__inline = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inline(self):
    self.__inline = YANGDynClass(base=inline.inline, is_container='container', yang_name="inline", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_reference(self):
    """
    Getter method for reference, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/reference (container)

    YANG Description: This container is applicable when the mode of application is explicitly
specified to as REFERENCE. The tags set on a route are those that are
specified within the tag-set
    """
    return self.__reference
      
  def _set_reference(self, v, load=False):
    """
    Setter method for reference, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/reference (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reference() directly.

    YANG Description: This container is applicable when the mode of application is explicitly
specified to as REFERENCE. The tags set on a route are those that are
specified within the tag-set
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=reference.reference, is_container='container', yang_name="reference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reference must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=reference.reference, is_container='container', yang_name="reference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__reference = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reference(self):
    self.__reference = YANGDynClass(base=reference.reference, is_container='container', yang_name="reference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  inline = __builtin__.property(_get_inline, _set_inline)
  reference = __builtin__.property(_get_reference, _set_reference)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('inline', inline), ('reference', reference), ])


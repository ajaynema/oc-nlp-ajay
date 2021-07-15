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
from . import control_link
from . import data_link
from . import interface_groups
class ha_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-fw-high-availability - based on the path /ha-groups/ha-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: HA group id used to create a logical HA group
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__config','__state','__control_link','__data_link','__interface_groups',)

  _yang_name = 'ha-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__control_link = YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__data_link = YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__interface_groups = YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)

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
      return ['ha-groups', 'ha-group']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /ha_groups/ha_group/id (leafref)

    YANG Description: References the group id key.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /ha_groups/ha_group/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: References the group id key.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /ha_groups/ha_group/config (container)

    YANG Description: Config container for HA parameters
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /ha_groups/ha_group/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Config container for HA parameters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /ha_groups/ha_group/state (container)

    YANG Description: State container for HA parameters
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /ha_groups/ha_group/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State container for HA parameters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_control_link(self):
    """
    Getter method for control_link, mapped from YANG variable /ha_groups/ha_group/control_link (container)

    YANG Description: Top-level container for HA control link
    """
    return self.__control_link
      
  def _set_control_link(self, v, load=False):
    """
    Setter method for control_link, mapped from YANG variable /ha_groups/ha_group/control_link (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_link() directly.

    YANG Description: Top-level container for HA control link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_link must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__control_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_link(self):
    self.__control_link = YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_data_link(self):
    """
    Getter method for data_link, mapped from YANG variable /ha_groups/ha_group/data_link (container)

    YANG Description: Top-level container for HA data link
    """
    return self.__data_link
      
  def _set_data_link(self, v, load=False):
    """
    Setter method for data_link, mapped from YANG variable /ha_groups/ha_group/data_link (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link() directly.

    YANG Description: Top-level container for HA data link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__data_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link(self):
    self.__data_link = YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_interface_groups(self):
    """
    Getter method for interface_groups, mapped from YANG variable /ha_groups/ha_group/interface_groups (container)

    YANG Description: Top level container for monitored interface groups
    """
    return self.__interface_groups
      
  def _set_interface_groups(self, v, load=False):
    """
    Setter method for interface_groups, mapped from YANG variable /ha_groups/ha_group/interface_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_groups() directly.

    YANG Description: Top level container for monitored interface groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__interface_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_groups(self):
    self.__interface_groups = YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  control_link = __builtin__.property(_get_control_link, _set_control_link)
  data_link = __builtin__.property(_get_data_link, _set_data_link)
  interface_groups = __builtin__.property(_get_interface_groups, _set_interface_groups)


  _pyangbind_elements = OrderedDict([('id', id), ('config', config), ('state', state), ('control_link', control_link), ('data_link', data_link), ('interface_groups', interface_groups), ])


from . import config
from . import state
from . import control_link
from . import data_link
from . import interface_groups
class ha_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-fw-high-availability - based on the path /ha-groups/ha-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: HA group id used to create a logical HA group
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__config','__state','__control_link','__data_link','__interface_groups',)

  _yang_name = 'ha-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__control_link = YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__data_link = YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    self.__interface_groups = YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)

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
      return ['ha-groups', 'ha-group']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /ha_groups/ha_group/id (leafref)

    YANG Description: References the group id key.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /ha_groups/ha_group/id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: References the group id key.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /ha_groups/ha_group/config (container)

    YANG Description: Config container for HA parameters
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /ha_groups/ha_group/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Config container for HA parameters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /ha_groups/ha_group/state (container)

    YANG Description: State container for HA parameters
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /ha_groups/ha_group/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State container for HA parameters
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_control_link(self):
    """
    Getter method for control_link, mapped from YANG variable /ha_groups/ha_group/control_link (container)

    YANG Description: Top-level container for HA control link
    """
    return self.__control_link
      
  def _set_control_link(self, v, load=False):
    """
    Setter method for control_link, mapped from YANG variable /ha_groups/ha_group/control_link (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_link() directly.

    YANG Description: Top-level container for HA control link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_link must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__control_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_link(self):
    self.__control_link = YANGDynClass(base=control_link.control_link, is_container='container', yang_name="control-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_data_link(self):
    """
    Getter method for data_link, mapped from YANG variable /ha_groups/ha_group/data_link (container)

    YANG Description: Top-level container for HA data link
    """
    return self.__data_link
      
  def _set_data_link(self, v, load=False):
    """
    Setter method for data_link, mapped from YANG variable /ha_groups/ha_group/data_link (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_data_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_data_link() directly.

    YANG Description: Top-level container for HA data link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """data_link must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__data_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_data_link(self):
    self.__data_link = YANGDynClass(base=data_link.data_link, is_container='container', yang_name="data-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)


  def _get_interface_groups(self):
    """
    Getter method for interface_groups, mapped from YANG variable /ha_groups/ha_group/interface_groups (container)

    YANG Description: Top level container for monitored interface groups
    """
    return self.__interface_groups
      
  def _set_interface_groups(self, v, load=False):
    """
    Setter method for interface_groups, mapped from YANG variable /ha_groups/ha_group/interface_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_groups() directly.

    YANG Description: Top level container for monitored interface groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)""",
        })

    self.__interface_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_groups(self):
    self.__interface_groups = YANGDynClass(base=interface_groups.interface_groups, is_container='container', yang_name="interface-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/oc-fw-ha', defining_module='openconfig-fw-high-availability', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  control_link = __builtin__.property(_get_control_link, _set_control_link)
  data_link = __builtin__.property(_get_data_link, _set_data_link)
  interface_groups = __builtin__.property(_get_interface_groups, _set_interface_groups)


  _pyangbind_elements = OrderedDict([('id', id), ('config', config), ('state', state), ('control_link', control_link), ('data_link', data_link), ('interface_groups', interface_groups), ])



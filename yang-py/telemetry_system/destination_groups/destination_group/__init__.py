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
from . import destinations
class destination_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/destination-groups/destination-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of destination-groups. Destination groups allow the
reuse of common telemetry destinations across the
telemetry configuration. An operator references a
set of destinations via the configurable
destination-group-identifier.

A destination group may contain one or more telemetry
destinations
  """
  __slots__ = ('_path_helper', '_extmethods', '__group_id','__config','__state','__destinations',)

  _yang_name = 'destination-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destinations = YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system', 'destination-groups', 'destination-group']

  def _get_group_id(self):
    """
    Getter method for group_id, mapped from YANG variable /telemetry_system/destination_groups/destination_group/group_id (leafref)

    YANG Description: Unique identifier for the destination group
    """
    return self.__group_id
      
  def _set_group_id(self, v, load=False):
    """
    Setter method for group_id, mapped from YANG variable /telemetry_system/destination_groups/destination_group/group_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_id() directly.

    YANG Description: Unique identifier for the destination group
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_id(self):
    self.__group_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/config (container)

    YANG Description: Top level config container for destination groups
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Top level config container for destination groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/state (container)

    YANG Description: Top level state container for destination groups
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Top level state container for destination groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destinations(self):
    """
    Getter method for destinations, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations (container)

    YANG Description: The destination container lists the destination
information such as IP address and port of the
telemetry messages from the network element.
    """
    return self.__destinations
      
  def _set_destinations(self, v, load=False):
    """
    Setter method for destinations, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destinations is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destinations() directly.

    YANG Description: The destination container lists the destination
information such as IP address and port of the
telemetry messages from the network element.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destinations must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destinations = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destinations(self):
    self.__destinations = YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  group_id = __builtin__.property(_get_group_id, _set_group_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  destinations = __builtin__.property(_get_destinations, _set_destinations)


  _pyangbind_elements = OrderedDict([('group_id', group_id), ('config', config), ('state', state), ('destinations', destinations), ])


from . import config
from . import state
from . import destinations
class destination_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/destination-groups/destination-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of destination-groups. Destination groups allow the
reuse of common telemetry destinations across the
telemetry configuration. An operator references a
set of destinations via the configurable
destination-group-identifier.

A destination group may contain one or more telemetry
destinations
  """
  __slots__ = ('_path_helper', '_extmethods', '__group_id','__config','__state','__destinations',)

  _yang_name = 'destination-group'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__group_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__destinations = YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system', 'destination-groups', 'destination-group']

  def _get_group_id(self):
    """
    Getter method for group_id, mapped from YANG variable /telemetry_system/destination_groups/destination_group/group_id (leafref)

    YANG Description: Unique identifier for the destination group
    """
    return self.__group_id
      
  def _set_group_id(self, v, load=False):
    """
    Setter method for group_id, mapped from YANG variable /telemetry_system/destination_groups/destination_group/group_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_id() directly.

    YANG Description: Unique identifier for the destination group
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)""",
        })

    self.__group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_id(self):
    self.__group_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/config (container)

    YANG Description: Top level config container for destination groups
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /telemetry_system/destination_groups/destination_group/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Top level config container for destination groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/state (container)

    YANG Description: Top level state container for destination groups
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /telemetry_system/destination_groups/destination_group/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Top level state container for destination groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_destinations(self):
    """
    Getter method for destinations, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations (container)

    YANG Description: The destination container lists the destination
information such as IP address and port of the
telemetry messages from the network element.
    """
    return self.__destinations
      
  def _set_destinations(self, v, load=False):
    """
    Setter method for destinations, mapped from YANG variable /telemetry_system/destination_groups/destination_group/destinations (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destinations is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destinations() directly.

    YANG Description: The destination container lists the destination
information such as IP address and port of the
telemetry messages from the network element.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destinations must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__destinations = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destinations(self):
    self.__destinations = YANGDynClass(base=destinations.destinations, is_container='container', yang_name="destinations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  group_id = __builtin__.property(_get_group_id, _set_group_id)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  destinations = __builtin__.property(_get_destinations, _set_destinations)


  _pyangbind_elements = OrderedDict([('group_id', group_id), ('config', config), ('state', state), ('destinations', destinations), ])



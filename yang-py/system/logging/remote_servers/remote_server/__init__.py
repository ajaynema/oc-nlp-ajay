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
from . import selectors
class remote_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/logging/remote-servers/remote-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of remote log servers
  """
  __slots__ = ('_path_helper', '_extmethods', '__host','__config','__state','__selectors',)

  _yang_name = 'remote-server'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__host = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return ['system', 'logging', 'remote-servers', 'remote-server']

  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /system/logging/remote_servers/remote_server/host (leafref)

    YANG Description: Reference to the host list key
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /system/logging/remote_servers/remote_server/host (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.

    YANG Description: Reference to the host list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/logging/remote_servers/remote_server/config (container)

    YANG Description: Configuration data for remote log servers
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/logging/remote_servers/remote_server/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for remote log servers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/logging/remote_servers/remote_server/state (container)

    YANG Description: Operational state data for remote log servers
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/logging/remote_servers/remote_server/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for remote log servers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_selectors(self):
    """
    Getter method for selectors, mapped from YANG variable /system/logging/remote_servers/remote_server/selectors (container)

    YANG Description: Enclosing container 
    """
    return self.__selectors
      
  def _set_selectors(self, v, load=False):
    """
    Setter method for selectors, mapped from YANG variable /system/logging/remote_servers/remote_server/selectors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selectors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selectors() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selectors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__selectors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selectors(self):
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  host = __builtin__.property(_get_host, _set_host)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  selectors = __builtin__.property(_get_selectors, _set_selectors)


  _pyangbind_elements = OrderedDict([('host', host), ('config', config), ('state', state), ('selectors', selectors), ])


from . import config
from . import state
from . import selectors
class remote_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/logging/remote-servers/remote-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of remote log servers
  """
  __slots__ = ('_path_helper', '_extmethods', '__host','__config','__state','__selectors',)

  _yang_name = 'remote-server'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__host = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return ['system', 'logging', 'remote-servers', 'remote-server']

  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /system/logging/remote_servers/remote_server/host (leafref)

    YANG Description: Reference to the host list key
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /system/logging/remote_servers/remote_server/host (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.

    YANG Description: Reference to the host list key
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/logging/remote_servers/remote_server/config (container)

    YANG Description: Configuration data for remote log servers
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/logging/remote_servers/remote_server/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for remote log servers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/logging/remote_servers/remote_server/state (container)

    YANG Description: Operational state data for remote log servers
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/logging/remote_servers/remote_server/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for remote log servers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_selectors(self):
    """
    Getter method for selectors, mapped from YANG variable /system/logging/remote_servers/remote_server/selectors (container)

    YANG Description: Enclosing container 
    """
    return self.__selectors
      
  def _set_selectors(self, v, load=False):
    """
    Setter method for selectors, mapped from YANG variable /system/logging/remote_servers/remote_server/selectors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selectors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selectors() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selectors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__selectors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selectors(self):
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  host = __builtin__.property(_get_host, _set_host)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  selectors = __builtin__.property(_get_selectors, _set_selectors)


  _pyangbind_elements = OrderedDict([('host', host), ('config', config), ('state', state), ('selectors', selectors), ])



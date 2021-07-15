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
from . import i_components
class b_component(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/evpn/evpn-instances/evpn-instance/pbb/b-component. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of B-components. The b-component learns and forwards
traffic on the backbone in order to reduce the number of
BGP MAC Advertisement routes by aggregating Customer/Client
MAC (C-MAC) addresses via Provider Backbone MAC (B-MAC) address.
  """
  __slots__ = ('_path_helper', '_extmethods', '__b_component_name','__config','__state','__i_components',)

  _yang_name = 'b-component'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__b_component_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__i_components = YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'evpn', 'evpn-instances', 'evpn-instance', 'pbb', 'b-component']

  def _get_b_component_name(self):
    """
    Getter method for b_component_name, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/b_component_name (leafref)

    YANG Description: Provider Backbone Bridging component name.
    """
    return self.__b_component_name
      
  def _set_b_component_name(self, v, load=False):
    """
    Setter method for b_component_name, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/b_component_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_b_component_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_b_component_name() directly.

    YANG Description: Provider Backbone Bridging component name.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """b_component_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__b_component_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_b_component_name(self):
    self.__b_component_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/config (container)

    YANG Description: Configuration variables for the b-components.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration variables for the b-components.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/state (container)

    YANG Description: State variables for the b-components.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for the b-components.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_i_components(self):
    """
    Getter method for i_components, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components (container)

    YANG Description: i-components container definition.
    """
    return self.__i_components
      
  def _set_i_components(self, v, load=False):
    """
    Setter method for i_components, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_components is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_components() directly.

    YANG Description: i-components container definition.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_components must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__i_components = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_components(self):
    self.__i_components = YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  b_component_name = __builtin__.property(_get_b_component_name, _set_b_component_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  i_components = __builtin__.property(_get_i_components, _set_i_components)


  _pyangbind_elements = OrderedDict([('b_component_name', b_component_name), ('config', config), ('state', state), ('i_components', i_components), ])


from . import config
from . import state
from . import i_components
class b_component(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/evpn/evpn-instances/evpn-instance/pbb/b-component. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of B-components. The b-component learns and forwards
traffic on the backbone in order to reduce the number of
BGP MAC Advertisement routes by aggregating Customer/Client
MAC (C-MAC) addresses via Provider Backbone MAC (B-MAC) address.
  """
  __slots__ = ('_path_helper', '_extmethods', '__b_component_name','__config','__state','__i_components',)

  _yang_name = 'b-component'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__b_component_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__i_components = YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'evpn', 'evpn-instances', 'evpn-instance', 'pbb', 'b-component']

  def _get_b_component_name(self):
    """
    Getter method for b_component_name, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/b_component_name (leafref)

    YANG Description: Provider Backbone Bridging component name.
    """
    return self.__b_component_name
      
  def _set_b_component_name(self, v, load=False):
    """
    Setter method for b_component_name, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/b_component_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_b_component_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_b_component_name() directly.

    YANG Description: Provider Backbone Bridging component name.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """b_component_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__b_component_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_b_component_name(self):
    self.__b_component_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="b-component-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/config (container)

    YANG Description: Configuration variables for the b-components.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration variables for the b-components.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/state (container)

    YANG Description: State variables for the b-components.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for the b-components.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_i_components(self):
    """
    Getter method for i_components, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components (container)

    YANG Description: i-components container definition.
    """
    return self.__i_components
      
  def _set_i_components(self, v, load=False):
    """
    Setter method for i_components, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_components is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_components() directly.

    YANG Description: i-components container definition.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_components must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__i_components = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_components(self):
    self.__i_components = YANGDynClass(base=i_components.i_components, is_container='container', yang_name="i-components", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  b_component_name = __builtin__.property(_get_b_component_name, _set_b_component_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  i_components = __builtin__.property(_get_i_components, _set_i_components)


  _pyangbind_elements = OrderedDict([('b_component_name', b_component_name), ('config', config), ('state', state), ('i_components', i_components), ])



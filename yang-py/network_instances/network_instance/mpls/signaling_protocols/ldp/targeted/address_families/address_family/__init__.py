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
from . import targets
class address_family(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of address families for targeted LDP
configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi_name','__config','__state','__targets',)

  _yang_name = 'address-family'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__targets = YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'ldp', 'targeted', 'address-families', 'address-family']

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/afi_name (leafref)

    YANG Description: Adress-family name atttibute (IPv4, IPv6).
    """
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/afi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Adress-family name atttibute (IPv4, IPv6).
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__afi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_name(self):
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/config (container)

    YANG Description: Address-family configuration for targeted LDP
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Address-family configuration for targeted LDP
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/state (container)

    YANG Description: Address-family state for targeted LDP
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Address-family state for targeted LDP
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


  def _get_targets(self):
    """
    Getter method for targets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/targets (container)

    YANG Description: Container aggregating all targeted sessions and
their LDP-specific attributes.
    """
    return self.__targets
      
  def _set_targets(self, v, load=False):
    """
    Setter method for targets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/targets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_targets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_targets() directly.

    YANG Description: Container aggregating all targeted sessions and
their LDP-specific attributes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """targets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__targets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_targets(self):
    self.__targets = YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  targets = __builtin__.property(_get_targets, _set_targets)


  _pyangbind_elements = OrderedDict([('afi_name', afi_name), ('config', config), ('state', state), ('targets', targets), ])


from . import config
from . import state
from . import targets
class address_family(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families/address-family. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of address families for targeted LDP
configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi_name','__config','__state','__targets',)

  _yang_name = 'address-family'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__targets = YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'ldp', 'targeted', 'address-families', 'address-family']

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/afi_name (leafref)

    YANG Description: Adress-family name atttibute (IPv4, IPv6).
    """
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/afi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Adress-family name atttibute (IPv4, IPv6).
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__afi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi_name(self):
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/config (container)

    YANG Description: Address-family configuration for targeted LDP
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Address-family configuration for targeted LDP
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/state (container)

    YANG Description: Address-family state for targeted LDP
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Address-family state for targeted LDP
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


  def _get_targets(self):
    """
    Getter method for targets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/targets (container)

    YANG Description: Container aggregating all targeted sessions and
their LDP-specific attributes.
    """
    return self.__targets
      
  def _set_targets(self, v, load=False):
    """
    Setter method for targets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family/targets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_targets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_targets() directly.

    YANG Description: Container aggregating all targeted sessions and
their LDP-specific attributes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """targets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__targets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_targets(self):
    self.__targets = YANGDynClass(base=targets.targets, is_container='container', yang_name="targets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  targets = __builtin__.property(_get_targets, _set_targets)


  _pyangbind_elements = OrderedDict([('afi_name', afi_name), ('config', config), ('state', state), ('targets', targets), ])



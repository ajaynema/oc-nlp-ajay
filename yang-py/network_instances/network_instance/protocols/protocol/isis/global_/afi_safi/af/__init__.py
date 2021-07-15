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
from . import multi_topology
class af(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/afi-safi/af. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Address-family/Subsequent Address-family list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi_name','__safi_name','__config','__state','__multi_topology',)

  _yang_name = 'af'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__safi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__multi_topology = YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'afi-safi', 'af']

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/afi_name (leafref)

    YANG Description: Reference to address-family type
    """
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/afi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Reference to address-family type
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


  def _get_safi_name(self):
    """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/safi_name (leafref)

    YANG Description: Reference to subsequent address-family type
    """
    return self.__safi_name
      
  def _set_safi_name(self, v, load=False):
    """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/safi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Reference to subsequent address-family type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """safi_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__safi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_safi_name(self):
    self.__safi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/config (container)

    YANG Description: This container defines AFI-SAFI configuration parameters
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: This container defines AFI-SAFI configuration parameters
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/state (container)

    YANG Description: This container defines AFI-SAFI State information
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: This container defines AFI-SAFI State information
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


  def _get_multi_topology(self):
    """
    Getter method for multi_topology, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology (container)

    YANG Description: This container defines multi-topology address-family configuration
and state information. ISIS TLV 235, 237.
    """
    return self.__multi_topology
      
  def _set_multi_topology(self, v, load=False):
    """
    Setter method for multi_topology, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multi_topology is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multi_topology() directly.

    YANG Description: This container defines multi-topology address-family configuration
and state information. ISIS TLV 235, 237.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multi_topology must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__multi_topology = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multi_topology(self):
    self.__multi_topology = YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  safi_name = __builtin__.property(_get_safi_name, _set_safi_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  multi_topology = __builtin__.property(_get_multi_topology, _set_multi_topology)


  _pyangbind_elements = OrderedDict([('afi_name', afi_name), ('safi_name', safi_name), ('config', config), ('state', state), ('multi_topology', multi_topology), ])


from . import config
from . import state
from . import multi_topology
class af(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/afi-safi/af. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Address-family/Subsequent Address-family list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi_name','__safi_name','__config','__state','__multi_topology',)

  _yang_name = 'af'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__safi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__multi_topology = YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'global', 'afi-safi', 'af']

  def _get_afi_name(self):
    """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/afi_name (leafref)

    YANG Description: Reference to address-family type
    """
    return self.__afi_name
      
  def _set_afi_name(self, v, load=False):
    """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/afi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Reference to address-family type
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


  def _get_safi_name(self):
    """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/safi_name (leafref)

    YANG Description: Reference to subsequent address-family type
    """
    return self.__safi_name
      
  def _set_safi_name(self, v, load=False):
    """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/safi_name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Reference to subsequent address-family type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """safi_name must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
        })

    self.__safi_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_safi_name(self):
    self.__safi_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/config (container)

    YANG Description: This container defines AFI-SAFI configuration parameters
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: This container defines AFI-SAFI configuration parameters
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/state (container)

    YANG Description: This container defines AFI-SAFI State information
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: This container defines AFI-SAFI State information
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


  def _get_multi_topology(self):
    """
    Getter method for multi_topology, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology (container)

    YANG Description: This container defines multi-topology address-family configuration
and state information. ISIS TLV 235, 237.
    """
    return self.__multi_topology
      
  def _set_multi_topology(self, v, load=False):
    """
    Setter method for multi_topology, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/afi_safi/af/multi_topology (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multi_topology is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multi_topology() directly.

    YANG Description: This container defines multi-topology address-family configuration
and state information. ISIS TLV 235, 237.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multi_topology must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__multi_topology = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multi_topology(self):
    self.__multi_topology = YANGDynClass(base=multi_topology.multi_topology, is_container='container', yang_name="multi-topology", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
  safi_name = __builtin__.property(_get_safi_name, _set_safi_name)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  multi_topology = __builtin__.property(_get_multi_topology, _set_multi_topology)


  _pyangbind_elements = OrderedDict([('afi_name', afi_name), ('safi_name', safi_name), ('config', config), ('state', state), ('multi_topology', multi_topology), ])



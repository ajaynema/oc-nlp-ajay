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
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/neighbors/neighbor/capabilities/capability/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for LLDP capabilities
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__enabled',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}},), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='identityref', is_config=False)
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)

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
      return ['lldp', 'interfaces', 'interface', 'neighbors', 'neighbor', 'capabilities', 'capability', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/capabilities/capability/state/name (identityref)

    YANG Description: Name of the system capability advertised by the neighbor.
Capabilities are represented in a bitmap that defines the
primary functions of the system. The capabilities are
defined in IEEE 802.1AB.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/capabilities/capability/state/name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the system capability advertised by the neighbor.
Capabilities are represented in a bitmap that defines the
primary functions of the system. The capabilities are
defined in IEEE 802.1AB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}},), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with identityref""",
          'defined-type': "openconfig-lldp:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}},), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='identityref', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:OTHER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:REPEATER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:MAC_BRIDGE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:WLAN_ACCESS_POINT': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:ROUTER': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TELEPHONE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:DOCSIS_CABLE_DEVICE': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:STATION_ONLY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:C_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:S_VLAN': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}, 'oc-lldp-types:TWO_PORT_MAC_RELAY': {'@module': 'openconfig-lldp-types', '@namespace': 'http://openconfig.net/yang/lldp/types'}},), is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='identityref', is_config=False)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/capabilities/capability/state/enabled (boolean)

    YANG Description: Indicates whether the corresponding system capability is
enabled on the neighbor.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /lldp/interfaces/interface/neighbors/neighbor/capabilities/capability/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Indicates whether the corresponding system capability is
enabled on the neighbor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)

  name = __builtin__.property(_get_name)
  enabled = __builtin__.property(_get_enabled)


  _pyangbind_elements = OrderedDict([('name', name), ('enabled', enabled), ])



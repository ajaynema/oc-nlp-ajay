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
from . import radios
from . import ssids
from . import system
from . import assigned_ap_managers
from . import interfaces
class access_point(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and state data for the access point referenced in the
list entry.
  """
  __slots__ = ('_path_helper', '_extmethods', '__hostname','__config','__radios','__ssids','__system','__assigned_ap_managers','__interfaces',)

  _yang_name = 'access-point'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hostname = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    self.__radios = YANGDynClass(base=radios.radios, is_container='container', yang_name="radios", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    self.__ssids = YANGDynClass(base=ssids.ssids, is_container='container', yang_name="ssids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    self.__system = YANGDynClass(base=system.system, is_container='container', yang_name="system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    self.__assigned_ap_managers = YANGDynClass(base=assigned_ap_managers.assigned_ap_managers, is_container='container', yang_name="assigned-ap-managers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

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
      return ['access-points', 'access-point']

  def _get_hostname(self):
    """
    Getter method for hostname, mapped from YANG variable /access_points/access_point/hostname (leafref)

    YANG Description: Access Point FQDN.
    """
    return self.__hostname
      
  def _set_hostname(self, v, load=False):
    """
    Setter method for hostname, mapped from YANG variable /access_points/access_point/hostname (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname() directly.

    YANG Description: Access Point FQDN.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='leafref', is_config=True)""",
        })

    self.__hostname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname(self):
    self.__hostname = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="hostname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /access_points/access_point/config (container)

    YANG Description: Config items at the global, Access Point level.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /access_points/access_point/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Config items at the global, Access Point level.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)


  def _get_radios(self):
    """
    Getter method for radios, mapped from YANG variable /access_points/access_point/radios (container)

    YANG Description: Top level container for radios, including configuration
and state data.
    """
    return self.__radios
      
  def _set_radios(self, v, load=False):
    """
    Setter method for radios, mapped from YANG variable /access_points/access_point/radios (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_radios is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_radios() directly.

    YANG Description: Top level container for radios, including configuration
and state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=radios.radios, is_container='container', yang_name="radios", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """radios must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=radios.radios, is_container='container', yang_name="radios", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)""",
        })

    self.__radios = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_radios(self):
    self.__radios = YANGDynClass(base=radios.radios, is_container='container', yang_name="radios", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)


  def _get_ssids(self):
    """
    Getter method for ssids, mapped from YANG variable /access_points/access_point/ssids (container)

    YANG Description: Top level container for ssids, including configuration
and state data.
    """
    return self.__ssids
      
  def _set_ssids(self, v, load=False):
    """
    Setter method for ssids, mapped from YANG variable /access_points/access_point/ssids (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssids is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssids() directly.

    YANG Description: Top level container for ssids, including configuration
and state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ssids.ssids, is_container='container', yang_name="ssids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssids must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssids.ssids, is_container='container', yang_name="ssids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)""",
        })

    self.__ssids = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssids(self):
    self.__ssids = YANGDynClass(base=ssids.ssids, is_container='container', yang_name="ssids", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)


  def _get_system(self):
    """
    Getter method for system, mapped from YANG variable /access_points/access_point/system (container)

    YANG Description: Enclosing container for system-related configuration and
operational state data
    """
    return self.__system
      
  def _set_system(self, v, load=False):
    """
    Setter method for system, mapped from YANG variable /access_points/access_point/system (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system() directly.

    YANG Description: Enclosing container for system-related configuration and
operational state data
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=system.system, is_container='container', yang_name="system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=system.system, is_container='container', yang_name="system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)""",
        })

    self.__system = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system(self):
    self.__system = YANGDynClass(base=system.system, is_container='container', yang_name="system", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)


  def _get_assigned_ap_managers(self):
    """
    Getter method for assigned_ap_managers, mapped from YANG variable /access_points/access_point/assigned_ap_managers (container)

    YANG Description: Wireless manager(s) this AP is assigned to. eg. Primary
Secondary, Tertiary etc.
    """
    return self.__assigned_ap_managers
      
  def _set_assigned_ap_managers(self, v, load=False):
    """
    Setter method for assigned_ap_managers, mapped from YANG variable /access_points/access_point/assigned_ap_managers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_assigned_ap_managers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_assigned_ap_managers() directly.

    YANG Description: Wireless manager(s) this AP is assigned to. eg. Primary
Secondary, Tertiary etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=assigned_ap_managers.assigned_ap_managers, is_container='container', yang_name="assigned-ap-managers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """assigned_ap_managers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=assigned_ap_managers.assigned_ap_managers, is_container='container', yang_name="assigned-ap-managers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)""",
        })

    self.__assigned_ap_managers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_assigned_ap_managers(self):
    self.__assigned_ap_managers = YANGDynClass(base=assigned_ap_managers.assigned_ap_managers, is_container='container', yang_name="assigned-ap-managers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=True)


  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /access_points/access_point/interfaces (container)

    YANG Description: Top level container for non-radio AP interfaces, including
configuration and state data.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /access_points/access_point/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Top level container for non-radio AP interfaces, including
configuration and state data.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='container', is_config=True)

  hostname = __builtin__.property(_get_hostname, _set_hostname)
  config = __builtin__.property(_get_config, _set_config)
  radios = __builtin__.property(_get_radios, _set_radios)
  ssids = __builtin__.property(_get_ssids, _set_ssids)
  system = __builtin__.property(_get_system, _set_system)
  assigned_ap_managers = __builtin__.property(_get_assigned_ap_managers, _set_assigned_ap_managers)
  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('hostname', hostname), ('config', config), ('radios', radios), ('ssids', ssids), ('system', system), ('assigned_ap_managers', assigned_ap_managers), ('interfaces', interfaces), ])



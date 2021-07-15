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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IGMP interface configuration.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__enabled','__version','__query_interval','__filter_prefixes',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)
    self.__filter_prefixes = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Reference to an interface on which IGMP is enabled.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Reference to an interface on which IGMP is enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this
leaf is defined is enabled, when set to false it is
explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this
leaf is defined is enabled, when set to false it is
explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/version (oc-igmp-types:igmp-version)

    YANG Description: IGMP Version.
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/version (oc-igmp-types:igmp-version)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: IGMP Version.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with oc-igmp-types:igmp-version""",
          'defined-type': "oc-igmp-types:igmp-version",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)


  def _get_query_interval(self):
    """
    Getter method for query_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/query_interval (oc-igmp-types:igmp-interval-type)

    YANG Description: Interval at which the router sends the IGMP membership
queries.
    """
    return self.__query_interval
      
  def _set_query_interval(self, v, load=False):
    """
    Setter method for query_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/query_interval (oc-igmp-types:igmp-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_interval() directly.

    YANG Description: Interval at which the router sends the IGMP membership
queries.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_interval must be of a type compatible with oc-igmp-types:igmp-interval-type""",
          'defined-type': "oc-igmp-types:igmp-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)""",
        })

    self.__query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_interval(self):
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)


  def _get_filter_prefixes(self):
    """
    Getter method for filter_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/filter_prefixes (string)

    YANG Description: List used to filter joins.
    """
    return self.__filter_prefixes
      
  def _set_filter_prefixes(self, v, load=False):
    """
    Setter method for filter_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/filter_prefixes (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_prefixes() directly.

    YANG Description: List used to filter joins.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_prefixes must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__filter_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_prefixes(self):
    self.__filter_prefixes = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  enabled = __builtin__.property(_get_enabled, _set_enabled)
  version = __builtin__.property(_get_version, _set_version)
  query_interval = __builtin__.property(_get_query_interval, _set_query_interval)
  filter_prefixes = __builtin__.property(_get_filter_prefixes, _set_filter_prefixes)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('enabled', enabled), ('version', version), ('query_interval', query_interval), ('filter_prefixes', filter_prefixes), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/igmp/interfaces/interface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IGMP interface configuration.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__enabled','__version','__query_interval','__filter_prefixes',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)
    self.__filter_prefixes = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'interfaces', 'interface', 'config']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/interface_id (oc-if:interface-id)

    YANG Description: Reference to an interface on which IGMP is enabled.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Reference to an interface on which IGMP is enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with oc-if:interface-id""",
          'defined-type': "oc-if:interface-id",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=True)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this
leaf is defined is enabled, when set to false it is
explicitly disabled.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this
leaf is defined is enabled, when set to false it is
explicitly disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/version (oc-igmp-types:igmp-version)

    YANG Description: IGMP Version.
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/version (oc-igmp-types:igmp-version)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: IGMP Version.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with oc-igmp-types:igmp-version""",
          'defined-type': "oc-igmp-types:igmp-version",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..3']}), is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-version', is_config=True)


  def _get_query_interval(self):
    """
    Getter method for query_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/query_interval (oc-igmp-types:igmp-interval-type)

    YANG Description: Interval at which the router sends the IGMP membership
queries.
    """
    return self.__query_interval
      
  def _set_query_interval(self, v, load=False):
    """
    Setter method for query_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/query_interval (oc-igmp-types:igmp-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_query_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_query_interval() directly.

    YANG Description: Interval at which the router sends the IGMP membership
queries.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """query_interval must be of a type compatible with oc-igmp-types:igmp-interval-type""",
          'defined-type': "oc-igmp-types:igmp-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)""",
        })

    self.__query_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_query_interval(self):
    self.__query_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..1024']}), is_leaf=True, yang_name="query-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-igmp-types:igmp-interval-type', is_config=True)


  def _get_filter_prefixes(self):
    """
    Getter method for filter_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/filter_prefixes (string)

    YANG Description: List used to filter joins.
    """
    return self.__filter_prefixes
      
  def _set_filter_prefixes(self, v, load=False):
    """
    Setter method for filter_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/interfaces/interface/config/filter_prefixes (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_prefixes() directly.

    YANG Description: List used to filter joins.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_prefixes must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)""",
        })

    self.__filter_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_prefixes(self):
    self.__filter_prefixes = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="filter-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=True)

  interface_id = __builtin__.property(_get_interface_id, _set_interface_id)
  enabled = __builtin__.property(_get_enabled, _set_enabled)
  version = __builtin__.property(_get_version, _set_version)
  query_interval = __builtin__.property(_get_query_interval, _set_query_interval)
  filter_prefixes = __builtin__.property(_get_filter_prefixes, _set_filter_prefixes)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('enabled', enabled), ('version', version), ('query_interval', query_interval), ('filter_prefixes', filter_prefixes), ])


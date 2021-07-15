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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/prefix-limit/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the prefix
limit for the AFI-SAFI
  """
  __slots__ = ('_path_helper', '_extmethods', '__max_prefixes','__prevent_teardown','__warning_threshold_pct','__restart_timer',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__max_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__prevent_teardown = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__warning_threshold_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    self.__restart_timer = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-labeled-unicast', 'prefix-limit', 'config']

  def _get_max_prefixes(self):
    """
    Getter method for max_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/max_prefixes (uint32)

    YANG Description: Maximum number of prefixes that will be accepted
from the neighbour
    """
    return self.__max_prefixes
      
  def _set_max_prefixes(self, v, load=False):
    """
    Setter method for max_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/max_prefixes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_prefixes() directly.

    YANG Description: Maximum number of prefixes that will be accepted
from the neighbour
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_prefixes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__max_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_prefixes(self):
    self.__max_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_prevent_teardown(self):
    """
    Getter method for prevent_teardown, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/prevent_teardown (boolean)

    YANG Description: Do not tear down the BGP session when the maximum
prefix limit is exceeded, but rather only log a
warning. The default of this leaf is false, such
that when it is not specified, the session is torn
down.
    """
    return self.__prevent_teardown
      
  def _set_prevent_teardown(self, v, load=False):
    """
    Setter method for prevent_teardown, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/prevent_teardown (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prevent_teardown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prevent_teardown() directly.

    YANG Description: Do not tear down the BGP session when the maximum
prefix limit is exceeded, but rather only log a
warning. The default of this leaf is false, such
that when it is not specified, the session is torn
down.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prevent_teardown must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__prevent_teardown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prevent_teardown(self):
    self.__prevent_teardown = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_warning_threshold_pct(self):
    """
    Getter method for warning_threshold_pct, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/warning_threshold_pct (oc-types:percentage)

    YANG Description: Threshold on number of prefixes that can be received
from a neighbour before generation of warning messages
or log entries. Expressed as a percentage of
max-prefixes
    """
    return self.__warning_threshold_pct
      
  def _set_warning_threshold_pct(self, v, load=False):
    """
    Setter method for warning_threshold_pct, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/warning_threshold_pct (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_warning_threshold_pct is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_warning_threshold_pct() directly.

    YANG Description: Threshold on number of prefixes that can be received
from a neighbour before generation of warning messages
or log entries. Expressed as a percentage of
max-prefixes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """warning_threshold_pct must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)""",
        })

    self.__warning_threshold_pct = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_warning_threshold_pct(self):
    self.__warning_threshold_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)


  def _get_restart_timer(self):
    """
    Getter method for restart_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/restart_timer (decimal64)

    YANG Description: Time interval in seconds after which the BGP session
is re-established after being torn down due to exceeding
the max-prefix limit.
    """
    return self.__restart_timer
      
  def _set_restart_timer(self, v, load=False):
    """
    Setter method for restart_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/restart_timer (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_restart_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_restart_timer() directly.

    YANG Description: Time interval in seconds after which the BGP session
is re-established after being torn down due to exceeding
the max-prefix limit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """restart_timer must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)""",
        })

    self.__restart_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_restart_timer(self):
    self.__restart_timer = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)

  max_prefixes = __builtin__.property(_get_max_prefixes, _set_max_prefixes)
  prevent_teardown = __builtin__.property(_get_prevent_teardown, _set_prevent_teardown)
  warning_threshold_pct = __builtin__.property(_get_warning_threshold_pct, _set_warning_threshold_pct)
  restart_timer = __builtin__.property(_get_restart_timer, _set_restart_timer)


  _pyangbind_elements = OrderedDict([('max_prefixes', max_prefixes), ('prevent_teardown', prevent_teardown), ('warning_threshold_pct', warning_threshold_pct), ('restart_timer', restart_timer), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/afi-safis/afi-safi/ipv4-labeled-unicast/prefix-limit/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the prefix
limit for the AFI-SAFI
  """
  __slots__ = ('_path_helper', '_extmethods', '__max_prefixes','__prevent_teardown','__warning_threshold_pct','__restart_timer',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__max_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    self.__prevent_teardown = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    self.__warning_threshold_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    self.__restart_timer = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'global', 'afi-safis', 'afi-safi', 'ipv4-labeled-unicast', 'prefix-limit', 'config']

  def _get_max_prefixes(self):
    """
    Getter method for max_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/max_prefixes (uint32)

    YANG Description: Maximum number of prefixes that will be accepted
from the neighbour
    """
    return self.__max_prefixes
      
  def _set_max_prefixes(self, v, load=False):
    """
    Setter method for max_prefixes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/max_prefixes (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_prefixes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_prefixes() directly.

    YANG Description: Maximum number of prefixes that will be accepted
from the neighbour
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_prefixes must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
        })

    self.__max_prefixes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_prefixes(self):
    self.__max_prefixes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-prefixes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)


  def _get_prevent_teardown(self):
    """
    Getter method for prevent_teardown, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/prevent_teardown (boolean)

    YANG Description: Do not tear down the BGP session when the maximum
prefix limit is exceeded, but rather only log a
warning. The default of this leaf is false, such
that when it is not specified, the session is torn
down.
    """
    return self.__prevent_teardown
      
  def _set_prevent_teardown(self, v, load=False):
    """
    Setter method for prevent_teardown, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/prevent_teardown (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prevent_teardown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prevent_teardown() directly.

    YANG Description: Do not tear down the BGP session when the maximum
prefix limit is exceeded, but rather only log a
warning. The default of this leaf is false, such
that when it is not specified, the session is torn
down.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prevent_teardown must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__prevent_teardown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prevent_teardown(self):
    self.__prevent_teardown = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="prevent-teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)


  def _get_warning_threshold_pct(self):
    """
    Getter method for warning_threshold_pct, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/warning_threshold_pct (oc-types:percentage)

    YANG Description: Threshold on number of prefixes that can be received
from a neighbour before generation of warning messages
or log entries. Expressed as a percentage of
max-prefixes
    """
    return self.__warning_threshold_pct
      
  def _set_warning_threshold_pct(self, v, load=False):
    """
    Setter method for warning_threshold_pct, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/warning_threshold_pct (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_warning_threshold_pct is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_warning_threshold_pct() directly.

    YANG Description: Threshold on number of prefixes that can be received
from a neighbour before generation of warning messages
or log entries. Expressed as a percentage of
max-prefixes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """warning_threshold_pct must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)""",
        })

    self.__warning_threshold_pct = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_warning_threshold_pct(self):
    self.__warning_threshold_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="warning-threshold-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:percentage', is_config=True)


  def _get_restart_timer(self):
    """
    Getter method for restart_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/restart_timer (decimal64)

    YANG Description: Time interval in seconds after which the BGP session
is re-established after being torn down due to exceeding
the max-prefix limit.
    """
    return self.__restart_timer
      
  def _set_restart_timer(self, v, load=False):
    """
    Setter method for restart_timer, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/afi_safis/afi_safi/ipv4_labeled_unicast/prefix_limit/config/restart_timer (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_restart_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_restart_timer() directly.

    YANG Description: Time interval in seconds after which the BGP session
is re-established after being torn down due to exceeding
the max-prefix limit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """restart_timer must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)""",
        })

    self.__restart_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_restart_timer(self):
    self.__restart_timer = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="restart-timer", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='decimal64', is_config=True)

  max_prefixes = __builtin__.property(_get_max_prefixes, _set_max_prefixes)
  prevent_teardown = __builtin__.property(_get_prevent_teardown, _set_prevent_teardown)
  warning_threshold_pct = __builtin__.property(_get_warning_threshold_pct, _set_warning_threshold_pct)
  restart_timer = __builtin__.property(_get_restart_timer, _set_restart_timer)


  _pyangbind_elements = OrderedDict([('max_prefixes', max_prefixes), ('prevent_teardown', prevent_teardown), ('warning_threshold_pct', warning_threshold_pct), ('restart_timer', restart_timer), ])



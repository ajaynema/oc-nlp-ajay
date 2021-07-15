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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for SSM maps.
  """
  __slots__ = ('_path_helper', '_extmethods', '__source','__ssm_ranges',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)
    self.__ssm_ranges = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'global', 'ssm', 'mappings', 'mapping', 'state']

  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/source (inet:ipv4-address)

    YANG Description: Multicast source address.
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/source (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.

    YANG Description: Multicast source address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)


  def _get_ssm_ranges(self):
    """
    Getter method for ssm_ranges, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/ssm_ranges (leafref)

    YANG Description: List of accepted source specific multicast (SSM) address
ranges.
    """
    return self.__ssm_ranges
      
  def _set_ssm_ranges(self, v, load=False):
    """
    Setter method for ssm_ranges, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/ssm_ranges (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssm_ranges is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssm_ranges() directly.

    YANG Description: List of accepted source specific multicast (SSM) address
ranges.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssm_ranges must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__ssm_ranges = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssm_ranges(self):
    self.__ssm_ranges = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

  source = __builtin__.property(_get_source)
  ssm_ranges = __builtin__.property(_get_ssm_ranges)


  _pyangbind_elements = OrderedDict([('source', source), ('ssm_ranges', ssm_ranges), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for SSM maps.
  """
  __slots__ = ('_path_helper', '_extmethods', '__source','__ssm_ranges',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)
    self.__ssm_ranges = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'global', 'ssm', 'mappings', 'mapping', 'state']

  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/source (inet:ipv4-address)

    YANG Description: Multicast source address.
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/source (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.

    YANG Description: Multicast source address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address', is_config=False)


  def _get_ssm_ranges(self):
    """
    Getter method for ssm_ranges, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/ssm_ranges (leafref)

    YANG Description: List of accepted source specific multicast (SSM) address
ranges.
    """
    return self.__ssm_ranges
      
  def _set_ssm_ranges(self, v, load=False):
    """
    Setter method for ssm_ranges, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping/state/ssm_ranges (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssm_ranges is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssm_ranges() directly.

    YANG Description: List of accepted source specific multicast (SSM) address
ranges.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssm_ranges must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__ssm_ranges = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssm_ranges(self):
    self.__ssm_ranges = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ssm-ranges", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)

  source = __builtin__.property(_get_source)
  ssm_ranges = __builtin__.property(_get_ssm_ranges)


  _pyangbind_elements = OrderedDict([('source', source), ('ssm_ranges', ssm_ranges), ])



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

from . import mapping
class mappings(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/igmp/global/ssm/mappings. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of source specific multicast (SSM) mappings.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mapping',)

  _yang_name = 'mappings'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mapping = YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'global', 'ssm', 'mappings']

  def _get_mapping(self):
    """
    Getter method for mapping, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping (list)

    YANG Description: A Source Specific Multicast (SSM) mapping. This allows
IGMP v2 hosts to be able to join in SSM environments
by translating IGMP v2 reports into IGMP v3 reports.
The request in an IGMP v2 join is sent toward the source
address found by matching the multicast address.
    """
    return self.__mapping
      
  def _set_mapping(self, v, load=False):
    """
    Setter method for mapping, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mapping() directly.

    YANG Description: A Source Specific Multicast (SSM) mapping. This allows
IGMP v2 hosts to be able to join in SSM environments
by translating IGMP v2 reports into IGMP v3 reports.
The request in an IGMP v2 join is sent toward the source
address found by matching the multicast address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mapping(self):
    self.__mapping = YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  mapping = __builtin__.property(_get_mapping, _set_mapping)


  _pyangbind_elements = OrderedDict([('mapping', mapping), ])


from . import mapping
class mappings(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/igmp/global/ssm/mappings. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of source specific multicast (SSM) mappings.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mapping',)

  _yang_name = 'mappings'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mapping = YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'igmp', 'global', 'ssm', 'mappings']

  def _get_mapping(self):
    """
    Getter method for mapping, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping (list)

    YANG Description: A Source Specific Multicast (SSM) mapping. This allows
IGMP v2 hosts to be able to join in SSM environments
by translating IGMP v2 reports into IGMP v3 reports.
The request in an IGMP v2 join is sent toward the source
address found by matching the multicast address.
    """
    return self.__mapping
      
  def _set_mapping(self, v, load=False):
    """
    Setter method for mapping, mapped from YANG variable /network_instances/network_instance/protocols/protocol/igmp/global/ssm/mappings/mapping (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mapping() directly.

    YANG Description: A Source Specific Multicast (SSM) mapping. This allows
IGMP v2 hosts to be able to join in SSM environments
by translating IGMP v2 reports into IGMP v3 reports.
The request in an IGMP v2 join is sent toward the source
address found by matching the multicast address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mapping must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mapping(self):
    self.__mapping = YANGDynClass(base=YANGListType("source",mapping.mapping, yang_name="mapping", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='source', extensions=None), is_container='list', yang_name="mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  mapping = __builtin__.property(_get_mapping, _set_mapping)


  _pyangbind_elements = OrderedDict([('mapping', mapping), ])



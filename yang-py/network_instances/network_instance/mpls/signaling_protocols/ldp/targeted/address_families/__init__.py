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

from . import address_family
class address_families(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global container for IPv4 and IPv6 attributes for LDP.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address_family',)

  _yang_name = 'address-families'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__address_family = YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'ldp', 'targeted', 'address-families']

  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family (list)

    YANG Description: List of address families for targeted LDP
configuration
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: List of address families for targeted LDP
configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  address_family = __builtin__.property(_get_address_family, _set_address_family)


  _pyangbind_elements = OrderedDict([('address_family', address_family), ])


from . import address_family
class address_families(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/ldp/targeted/address-families. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global container for IPv4 and IPv6 attributes for LDP.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address_family',)

  _yang_name = 'address-families'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__address_family = YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'ldp', 'targeted', 'address-families']

  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family (list)

    YANG Description: List of address families for targeted LDP
configuration
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/ldp/targeted/address_families/address_family (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: List of address families for targeted LDP
configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=YANGListType("afi_name",address_family.address_family, yang_name="address-family", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  address_family = __builtin__.property(_get_address_family, _set_address_family)


  _pyangbind_elements = OrderedDict([('address_family', address_family), ])



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

from . import unknown_attribute
class unknown_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/loc-rib/routes/route/unknown-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Unknown path attributes that were received in the UPDATE
message which contained the prefix.
  """
  __slots__ = ('_path_helper', '_extmethods', '__unknown_attribute',)

  _yang_name = 'unknown-attributes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__unknown_attribute = YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'loc-rib', 'routes', 'route', 'unknown-attributes']

  def _get_unknown_attribute(self):
    """
    Getter method for unknown_attribute, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/loc_rib/routes/route/unknown_attributes/unknown_attribute (list)

    YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
    """
    return self.__unknown_attribute
      
  def _set_unknown_attribute(self, v, load=False):
    """
    Setter method for unknown_attribute, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/loc_rib/routes/route/unknown_attributes/unknown_attribute (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_attribute is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_attribute() directly.

    YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_attribute must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__unknown_attribute = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_attribute(self):
    self.__unknown_attribute = YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  unknown_attribute = __builtin__.property(_get_unknown_attribute)


  _pyangbind_elements = OrderedDict([('unknown_attribute', unknown_attribute), ])


from . import unknown_attribute
class unknown_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/rib/afi-safis/afi-safi/ipv4-srte-policy/loc-rib/routes/route/unknown-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Unknown path attributes that were received in the UPDATE
message which contained the prefix.
  """
  __slots__ = ('_path_helper', '_extmethods', '__unknown_attribute',)

  _yang_name = 'unknown-attributes'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__unknown_attribute = YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'bgp', 'rib', 'afi-safis', 'afi-safi', 'ipv4-srte-policy', 'loc-rib', 'routes', 'route', 'unknown-attributes']

  def _get_unknown_attribute(self):
    """
    Getter method for unknown_attribute, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/loc_rib/routes/route/unknown_attributes/unknown_attribute (list)

    YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
    """
    return self.__unknown_attribute
      
  def _set_unknown_attribute(self, v, load=False):
    """
    Setter method for unknown_attribute, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/rib/afi_safis/afi_safi/ipv4_srte_policy/loc_rib/routes/route/unknown_attributes/unknown_attribute (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_attribute is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_attribute() directly.

    YANG Description: This list contains received attributes that are unrecognized
or unsupported by the local router.  The list may be empty.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_attribute must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__unknown_attribute = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_attribute(self):
    self.__unknown_attribute = YANGDynClass(base=YANGListType("attr_type",unknown_attribute.unknown_attribute, yang_name="unknown-attribute", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='attr-type', extensions=None), is_container='list', yang_name="unknown-attribute", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  unknown_attribute = __builtin__.property(_get_unknown_attribute)


  _pyangbind_elements = OrderedDict([('unknown_attribute', unknown_attribute), ])



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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/tunnel/ipv6/router-advertisement/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to router advertisements
for IPv6.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interval','__lifetime','__suppress',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    self.__suppress = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'tunnel', 'ipv6', 'router-advertisement', 'config']

  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/interval (uint32)

    YANG Description: The interval between periodic router advertisement neighbor
discovery messages sent on this interface expressed in
seconds.
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: The interval between periodic router advertisement neighbor
discovery messages sent on this interface expressed in
seconds.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_lifetime(self):
    """
    Getter method for lifetime, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/lifetime (uint32)

    YANG Description: The lifetime advertised in the router advertisement neighbor
discovery message on this interface.
    """
    return self.__lifetime
      
  def _set_lifetime(self, v, load=False):
    """
    Setter method for lifetime, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/lifetime (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lifetime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lifetime() directly.

    YANG Description: The lifetime advertised in the router advertisement neighbor
discovery message on this interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lifetime must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__lifetime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lifetime(self):
    self.__lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint32', is_config=True)


  def _get_suppress(self):
    """
    Getter method for suppress, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/suppress (boolean)

    YANG Description: When set to true, router advertisement neighbor discovery
messages are not transmitted on this interface.
    """
    return self.__suppress
      
  def _set_suppress(self, v, load=False):
    """
    Setter method for suppress, mapped from YANG variable /access_points/access_point/interfaces/interface/tunnel/ipv6/router_advertisement/config/suppress (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress() directly.

    YANG Description: When set to true, router advertisement neighbor discovery
messages are not transmitted on this interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__suppress = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress(self):
    self.__suppress = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=True)

  interval = __builtin__.property(_get_interval, _set_interval)
  lifetime = __builtin__.property(_get_lifetime, _set_lifetime)
  suppress = __builtin__.property(_get_suppress, _set_suppress)


  _pyangbind_elements = OrderedDict([('interval', interval), ('lifetime', lifetime), ('suppress', suppress), ])



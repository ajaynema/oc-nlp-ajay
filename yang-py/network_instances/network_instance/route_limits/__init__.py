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

from . import route_limit
class route_limits(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/route-limits. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to the
maximum number of routes for the address family that
should be allowed within the Layer 3 network instance.

When the specified value is reached, no further prefixes
should be installed into the system's RIB from this network
instance unless the warning only leaf is set. In this case,
new routes should still be installed. If a alarm threshold
is specified, then this should be used to generate
alarms via telemetry for the network instance.
  """
  __slots__ = ('_path_helper', '_extmethods', '__route_limit',)

  _yang_name = 'route-limits'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__route_limit = YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'route-limits']

  def _get_route_limit(self):
    """
    Getter method for route_limit, mapped from YANG variable /network_instances/network_instance/route_limits/route_limit (list)

    YANG Description: A route limit applying to a particular address family.
    """
    return self.__route_limit
      
  def _set_route_limit(self, v, load=False):
    """
    Setter method for route_limit, mapped from YANG variable /network_instances/network_instance/route_limits/route_limit (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_limit() directly.

    YANG Description: A route limit applying to a particular address family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_limit must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__route_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_limit(self):
    self.__route_limit = YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  route_limit = __builtin__.property(_get_route_limit, _set_route_limit)


  _pyangbind_elements = OrderedDict([('route_limit', route_limit), ])


from . import route_limit
class route_limits(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/route-limits. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state relating to the
maximum number of routes for the address family that
should be allowed within the Layer 3 network instance.

When the specified value is reached, no further prefixes
should be installed into the system's RIB from this network
instance unless the warning only leaf is set. In this case,
new routes should still be installed. If a alarm threshold
is specified, then this should be used to generate
alarms via telemetry for the network instance.
  """
  __slots__ = ('_path_helper', '_extmethods', '__route_limit',)

  _yang_name = 'route-limits'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__route_limit = YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return ['network-instances', 'network-instance', 'route-limits']

  def _get_route_limit(self):
    """
    Getter method for route_limit, mapped from YANG variable /network_instances/network_instance/route_limits/route_limit (list)

    YANG Description: A route limit applying to a particular address family.
    """
    return self.__route_limit
      
  def _set_route_limit(self, v, load=False):
    """
    Setter method for route_limit, mapped from YANG variable /network_instances/network_instance/route_limits/route_limit (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_limit() directly.

    YANG Description: A route limit applying to a particular address family.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_limit must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__route_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_limit(self):
    self.__route_limit = YANGDynClass(base=YANGListType("afi",route_limit.route_limit, yang_name="route-limit", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi', extensions=None), is_container='list', yang_name="route-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  route_limit = __builtin__.property(_get_route_limit, _set_route_limit)


  _pyangbind_elements = OrderedDict([('route_limit', route_limit), ])



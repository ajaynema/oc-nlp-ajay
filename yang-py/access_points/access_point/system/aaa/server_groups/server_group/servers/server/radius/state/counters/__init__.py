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

class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/server-groups/server-group/servers/server/radius/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A collection of RADIUS related state objects.
  """
  __slots__ = ('_path_helper', '_extmethods', '__retried_access_requests','__access_accepts','__access_rejects','__timeout_access_requests',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__retried_access_requests = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="retried-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__access_accepts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-accepts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__access_rejects = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-rejects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__timeout_access_requests = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="timeout-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'server-groups', 'server-group', 'servers', 'server', 'radius', 'state', 'counters']

  def _get_retried_access_requests(self):
    """
    Getter method for retried_access_requests, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/retried_access_requests (oc-yang:counter64)

    YANG Description: Retransmitted Access-Request messages.
    """
    return self.__retried_access_requests
      
  def _set_retried_access_requests(self, v, load=False):
    """
    Setter method for retried_access_requests, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/retried_access_requests (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retried_access_requests is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retried_access_requests() directly.

    YANG Description: Retransmitted Access-Request messages.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="retried-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retried_access_requests must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="retried-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__retried_access_requests = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retried_access_requests(self):
    self.__retried_access_requests = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="retried-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_access_accepts(self):
    """
    Getter method for access_accepts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/access_accepts (oc-yang:counter64)

    YANG Description: Received Access-Accept messages.
    """
    return self.__access_accepts
      
  def _set_access_accepts(self, v, load=False):
    """
    Setter method for access_accepts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/access_accepts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_accepts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_accepts() directly.

    YANG Description: Received Access-Accept messages.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-accepts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_accepts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-accepts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__access_accepts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_accepts(self):
    self.__access_accepts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-accepts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_access_rejects(self):
    """
    Getter method for access_rejects, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/access_rejects (oc-yang:counter64)

    YANG Description: Received Access-Reject messages.
    """
    return self.__access_rejects
      
  def _set_access_rejects(self, v, load=False):
    """
    Setter method for access_rejects, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/access_rejects (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_rejects is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_rejects() directly.

    YANG Description: Received Access-Reject messages.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-rejects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_rejects must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-rejects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__access_rejects = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_rejects(self):
    self.__access_rejects = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="access-rejects", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_timeout_access_requests(self):
    """
    Getter method for timeout_access_requests, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/timeout_access_requests (oc-yang:counter64)

    YANG Description: Access-Request messages that have timed-out,
requiring retransmission.
    """
    return self.__timeout_access_requests
      
  def _set_timeout_access_requests(self, v, load=False):
    """
    Setter method for timeout_access_requests, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/radius/state/counters/timeout_access_requests (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout_access_requests is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout_access_requests() directly.

    YANG Description: Access-Request messages that have timed-out,
requiring retransmission.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="timeout-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout_access_requests must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="timeout-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__timeout_access_requests = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout_access_requests(self):
    self.__timeout_access_requests = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="timeout-access-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

  retried_access_requests = __builtin__.property(_get_retried_access_requests)
  access_accepts = __builtin__.property(_get_access_accepts)
  access_rejects = __builtin__.property(_get_access_rejects)
  timeout_access_requests = __builtin__.property(_get_timeout_access_requests)


  _pyangbind_elements = OrderedDict([('retried_access_requests', retried_access_requests), ('access_accepts', access_accepts), ('access_rejects', access_rejects), ('timeout_access_requests', timeout_access_requests), ])



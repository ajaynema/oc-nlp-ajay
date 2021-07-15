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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/authentication/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for global authentication
services
  """
  __slots__ = ('_path_helper', '_extmethods', '__authentication_method',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__authentication_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),six.text_type,]), is_leaf=False, yang_name="authentication-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'authentication', 'state']

  def _get_authentication_method(self):
    """
    Getter method for authentication_method, mapped from YANG variable /access_points/access_point/system/aaa/authentication/state/authentication_method (union)

    YANG Description: Ordered list of authentication methods for users.  This
can be either a reference to a server group, or a well-
defined designation in the AAA_METHOD_TYPE identity.  If
authentication fails with one method, the next defined
method is tried -- failure of all methods results in the
user being denied access.
    """
    return self.__authentication_method
      
  def _set_authentication_method(self, v, load=False):
    """
    Setter method for authentication_method, mapped from YANG variable /access_points/access_point/system/aaa/authentication/state/authentication_method (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication_method() directly.

    YANG Description: Ordered list of authentication methods for users.  This
can be either a reference to a server group, or a well-
defined designation in the AAA_METHOD_TYPE identity.  If
authentication fails with one method, the next defined
method is tried -- failure of all methods results in the
user being denied access.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),six.text_type,]), is_leaf=False, yang_name="authentication-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication_method must be of a type compatible with union""",
          'defined-type': "openconfig-access-points:union",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),six.text_type,]), is_leaf=False, yang_name="authentication-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=False)""",
        })

    self.__authentication_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication_method(self):
    self.__authentication_method = YANGDynClass(unique=True, base=TypedListType(allowed_type=[RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:TACACS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:RADIUS_ALL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:LOCAL': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},),six.text_type,]), is_leaf=False, yang_name="authentication-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='union', is_config=False)

  authentication_method = __builtin__.property(_get_authentication_method)


  _pyangbind_elements = OrderedDict([('authentication_method', authentication_method), ])



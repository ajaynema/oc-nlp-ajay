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
  from YANG module openconfig-system - based on the path /system/aaa/server-groups/server-group/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each server group
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)

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
      return ['system', 'aaa', 'server-groups', 'server-group', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/aaa/server_groups/server_group/config/name (string)

    YANG Description: Name for the server group
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/aaa/server_groups/server_group/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name for the server group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /system/aaa/server_groups/server_group/config/type (identityref)

    YANG Description: AAA server type -- all servers in the group must be of this
type
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /system/aaa/server_groups/server_group/config/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: AAA server type -- all servers in the group must be of this
type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-system:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  type = __builtin__.property(_get_type, _set_type)


  _pyangbind_elements = OrderedDict([('name', name), ('type', type), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/aaa/server-groups/server-group/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each server group
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__type',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)

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
      return ['system', 'aaa', 'server-groups', 'server-group', 'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /system/aaa/server_groups/server_group/config/name (string)

    YANG Description: Name for the server group
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /system/aaa/server_groups/server_group/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name for the server group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /system/aaa/server_groups/server_group/config/type (identityref)

    YANG Description: AAA server type -- all servers in the group must be of this
type
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /system/aaa/server_groups/server_group/config/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: AAA server type -- all servers in the group must be of this
type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-system:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:TACACS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}, 'oc-aaa:RADIUS': {'@module': 'openconfig-aaa', '@namespace': 'http://openconfig.net/yang/aaa'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='identityref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  type = __builtin__.property(_get_type, _set_type)


  _pyangbind_elements = OrderedDict([('name', name), ('type', type), ])



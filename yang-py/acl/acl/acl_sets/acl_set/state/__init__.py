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
  from YANG module openconfig-acl - based on the path /acl/acl-sets/acl-set/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Access list state information
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__type','__description',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='identityref', is_config=False)
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)

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
      return ['acl', 'acl-sets', 'acl-set', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /acl/acl_sets/acl_set/state/name (string)

    YANG Description: The name of the access-list set
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /acl/acl_sets/acl_set/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: The name of the access-list set
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /acl/acl_sets/acl_set/state/type (identityref)

    YANG Description: The type determines the fields allowed in the ACL entries
belonging to the ACL set (e.g., IPv4, IPv6, etc.)
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /acl/acl_sets/acl_set/state/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type determines the fields allowed in the ACL entries
belonging to the ACL set (e.g., IPv4, IPv6, etc.)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-acl:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='identityref', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV4': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_IPV6': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_L2': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MIXED': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}, 'oc-acl:ACL_MPLS': {'@module': 'openconfig-acl', '@namespace': 'http://openconfig.net/yang/acl'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='identityref', is_config=False)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /acl/acl_sets/acl_set/state/description (string)

    YANG Description: Description, or comment, for the ACL set
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /acl/acl_sets/acl_set/state/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Description, or comment, for the ACL set
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=False)

  name = __builtin__.property(_get_name)
  type = __builtin__.property(_get_type)
  description = __builtin__.property(_get_description)


  _pyangbind_elements = OrderedDict([('name', name), ('type', type), ('description', description), ])



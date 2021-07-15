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
  from YANG module openconfig-acl - based on the path /acl/acl-sets/acl-set/acl-entries/acl-entry/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Access list entries config
  """
  __slots__ = ('_path_helper', '_extmethods', '__sequence_id','__description',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint32', is_config=True)
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=True)

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
      return ['acl', 'acl-sets', 'acl-set', 'acl-entries', 'acl-entry', 'config']

  def _get_sequence_id(self):
    """
    Getter method for sequence_id, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/config/sequence_id (uint32)

    YANG Description: The sequence id determines the order in which ACL entries
are applied.  The sequence id must be unique for each entry
in an ACL set.  Target devices should apply the ACL entry
rules in ascending order determined by sequence id (low to
high), rather than the relying only on order in the list.
    """
    return self.__sequence_id
      
  def _set_sequence_id(self, v, load=False):
    """
    Setter method for sequence_id, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/config/sequence_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sequence_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sequence_id() directly.

    YANG Description: The sequence id determines the order in which ACL entries
are applied.  The sequence id must be unique for each entry
in an ACL set.  Target devices should apply the ACL entry
rules in ascending order determined by sequence id (low to
high), rather than the relying only on order in the list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sequence_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint32', is_config=True)""",
        })

    self.__sequence_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sequence_id(self):
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='uint32', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/config/description (string)

    YANG Description: A user-defined description, or comment, for this Access List
Entry.
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /acl/acl_sets/acl_set/acl_entries/acl_entry/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: A user-defined description, or comment, for this Access List
Entry.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='string', is_config=True)

  sequence_id = __builtin__.property(_get_sequence_id, _set_sequence_id)
  description = __builtin__.property(_get_description, _set_description)


  _pyangbind_elements = OrderedDict([('sequence_id', sequence_id), ('description', description), ])



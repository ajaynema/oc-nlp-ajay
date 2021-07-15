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

from . import access
class submodule(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization/modules/module/submodules/submodule. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of submodules included by a module.  All submodules
specified by 'include' statements in the module should be
included in this list.
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__access',)

  _yang_name = 'submodule'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    self.__access = YANGDynClass(base=access.access, is_container='container', yang_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)

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
      return ['organizations', 'organization', 'modules', 'module', 'submodules', 'submodule']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /organizations/organization/modules/module/submodules/submodule/name (string)

    YANG Description: Name of the submodule as indicated by its top-level
'submodule' statement
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /organizations/organization/modules/module/submodules/submodule/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the submodule as indicated by its top-level
'submodule' statement
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)


  def _get_access(self):
    """
    Getter method for access, mapped from YANG variable /organizations/organization/modules/module/submodules/submodule/access (container)

    YANG Description: Container for data pertaining to retrieval and usage of the
module
    """
    return self.__access
      
  def _set_access(self, v, load=False):
    """
    Setter method for access, mapped from YANG variable /organizations/organization/modules/module/submodules/submodule/access (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access() directly.

    YANG Description: Container for data pertaining to retrieval and usage of the
module
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access.access, is_container='container', yang_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access.access, is_container='container', yang_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)""",
        })

    self.__access = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access(self):
    self.__access = YANGDynClass(base=access.access, is_container='container', yang_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  access = __builtin__.property(_get_access, _set_access)


  _pyangbind_elements = OrderedDict([('name', name), ('access', access), ])


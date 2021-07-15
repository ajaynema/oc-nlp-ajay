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

from . import implementation
class implementations(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization/implementations. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for module implementation information
  """
  __slots__ = ('_path_helper', '_extmethods', '__implementation',)

  _yang_name = 'implementations'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__implementation = YANGDynClass(base=YANGListType("id",implementation.implementation, yang_name="implementation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="implementation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='list', is_config=True)

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
      return ['organizations', 'organization', 'implementations']

  def _get_implementation(self):
    """
    Getter method for implementation, mapped from YANG variable /organizations/organization/implementations/implementation (list)

    YANG Description: List of available implementations, keyed by an identifier
provided by either the implementor or the module
maintainer.  Such a key avoids needing a complex composite
key to uniquely identify an implementation.
    """
    return self.__implementation
      
  def _set_implementation(self, v, load=False):
    """
    Setter method for implementation, mapped from YANG variable /organizations/organization/implementations/implementation (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_implementation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_implementation() directly.

    YANG Description: List of available implementations, keyed by an identifier
provided by either the implementor or the module
maintainer.  Such a key avoids needing a complex composite
key to uniquely identify an implementation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",implementation.implementation, yang_name="implementation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="implementation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """implementation must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",implementation.implementation, yang_name="implementation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="implementation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='list', is_config=True)""",
        })

    self.__implementation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_implementation(self):
    self.__implementation = YANGDynClass(base=YANGListType("id",implementation.implementation, yang_name="implementation", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="implementation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='list', is_config=True)

  implementation = __builtin__.property(_get_implementation, _set_implementation)


  _pyangbind_elements = OrderedDict([('implementation', implementation), ])



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

from . import subcomponent
class subcomponents(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/subcomponents. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for subcomponent references
  """
  __slots__ = ('_path_helper', '_extmethods', '__subcomponent',)

  _yang_name = 'subcomponents'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__subcomponent = YANGDynClass(base=YANGListType("name",subcomponent.subcomponent, yang_name="subcomponent", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="subcomponent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='list', is_config=True)

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
      return ['components', 'component', 'subcomponents']

  def _get_subcomponent(self):
    """
    Getter method for subcomponent, mapped from YANG variable /components/component/subcomponents/subcomponent (list)

    YANG Description: List of subcomponent references
    """
    return self.__subcomponent
      
  def _set_subcomponent(self, v, load=False):
    """
    Setter method for subcomponent, mapped from YANG variable /components/component/subcomponents/subcomponent (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subcomponent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subcomponent() directly.

    YANG Description: List of subcomponent references
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",subcomponent.subcomponent, yang_name="subcomponent", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="subcomponent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subcomponent must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",subcomponent.subcomponent, yang_name="subcomponent", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="subcomponent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='list', is_config=True)""",
        })

    self.__subcomponent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subcomponent(self):
    self.__subcomponent = YANGDynClass(base=YANGListType("name",subcomponent.subcomponent, yang_name="subcomponent", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="subcomponent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='list', is_config=True)

  subcomponent = __builtin__.property(_get_subcomponent, _set_subcomponent)


  _pyangbind_elements = OrderedDict([('subcomponent', subcomponent), ])



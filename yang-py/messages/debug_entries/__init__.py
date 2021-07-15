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

from . import debug_service
class debug_entries(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-messages - based on the path /messages/debug-entries. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of debugs to enable.
  """
  __slots__ = ('_path_helper', '_extmethods', '__debug_service',)

  _yang_name = 'debug-entries'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__debug_service = YANGDynClass(base=YANGListType("service",debug_service.debug_service, yang_name="debug-service", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='service', extensions=None), is_container='list', yang_name="debug-service", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/messages', defining_module='openconfig-messages', yang_type='list', is_config=True)

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
      return ['messages', 'debug-entries']

  def _get_debug_service(self):
    """
    Getter method for debug_service, mapped from YANG variable /messages/debug_entries/debug_service (list)

    YANG Description: List of debugging entries.
    """
    return self.__debug_service
      
  def _set_debug_service(self, v, load=False):
    """
    Setter method for debug_service, mapped from YANG variable /messages/debug_entries/debug_service (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_debug_service is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_debug_service() directly.

    YANG Description: List of debugging entries.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("service",debug_service.debug_service, yang_name="debug-service", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='service', extensions=None), is_container='list', yang_name="debug-service", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/messages', defining_module='openconfig-messages', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """debug_service must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("service",debug_service.debug_service, yang_name="debug-service", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='service', extensions=None), is_container='list', yang_name="debug-service", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/messages', defining_module='openconfig-messages', yang_type='list', is_config=True)""",
        })

    self.__debug_service = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_debug_service(self):
    self.__debug_service = YANGDynClass(base=YANGListType("service",debug_service.debug_service, yang_name="debug-service", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='service', extensions=None), is_container='list', yang_name="debug-service", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/messages', defining_module='openconfig-messages', yang_type='list', is_config=True)

  debug_service = __builtin__.property(_get_debug_service, _set_debug_service)


  _pyangbind_elements = OrderedDict([('debug_service', debug_service), ])



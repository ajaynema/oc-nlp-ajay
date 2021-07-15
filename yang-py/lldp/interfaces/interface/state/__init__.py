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

from . import counters
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-lldp - based on the path /lldp/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__enabled','__counters',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='oc-if:base-interface-ref', is_config=False)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='container', is_config=False)

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
      return ['lldp', 'interfaces', 'interface', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /lldp/interfaces/interface/state/name (oc-if:base-interface-ref)

    YANG Description: Reference to the LLDP Ethernet interface
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /lldp/interfaces/interface/state/name (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Reference to the LLDP Ethernet interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='oc-if:base-interface-ref', is_config=False)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /lldp/interfaces/interface/state/enabled (boolean)

    YANG Description: Enable or disable the LLDP protocol on the interface.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /lldp/interfaces/interface/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enable or disable the LLDP protocol on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='boolean', is_config=False)


  def _get_counters(self):
    """
    Getter method for counters, mapped from YANG variable /lldp/interfaces/interface/state/counters (container)

    YANG Description: LLDP counters on each interface
    """
    return self.__counters
      
  def _set_counters(self, v, load=False):
    """
    Setter method for counters, mapped from YANG variable /lldp/interfaces/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: LLDP counters on each interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='container', is_config=False)""",
        })

    self.__counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counters(self):
    self.__counters = YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/lldp', defining_module='openconfig-lldp', yang_type='container', is_config=False)

  name = __builtin__.property(_get_name)
  enabled = __builtin__.property(_get_enabled)
  counters = __builtin__.property(_get_counters)


  _pyangbind_elements = OrderedDict([('name', name), ('enabled', enabled), ('counters', counters), ])



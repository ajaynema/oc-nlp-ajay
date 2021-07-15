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
  from YANG module openconfig-platform - based on the path /components/component/integrated-circuit/backplane-facing-capacity/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to backplane capacity.
  """
  __slots__ = ('_path_helper', '_extmethods', '__total','__consumed_capacity','__available_pct',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__total = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    self.__consumed_capacity = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    self.__available_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'backplane-facing-capacity', 'state']

  def _get_total(self):
    """
    Getter method for total, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/total (uint64)

    YANG Description: Total backplane-facing capacity that is available in the presence
of no link failures or degradation.
    """
    return self.__total
      
  def _set_total(self, v, load=False):
    """
    Setter method for total, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/total (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total() directly.

    YANG Description: Total backplane-facing capacity that is available in the presence
of no link failures or degradation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)""",
        })

    self.__total = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total(self):
    self.__total = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)


  def _get_consumed_capacity(self):
    """
    Getter method for consumed_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/consumed_capacity (uint64)

    YANG Description: Backplane-facing capacity that is consumed by front-panel ports that are connected
to the integrated circuit.
    """
    return self.__consumed_capacity
      
  def _set_consumed_capacity(self, v, load=False):
    """
    Setter method for consumed_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/consumed_capacity (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_consumed_capacity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_consumed_capacity() directly.

    YANG Description: Backplane-facing capacity that is consumed by front-panel ports that are connected
to the integrated circuit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """consumed_capacity must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)""",
        })

    self.__consumed_capacity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_consumed_capacity(self):
    self.__consumed_capacity = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)


  def _get_available_pct(self):
    """
    Getter method for available_pct, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/available_pct (oc-types:percentage)

    YANG Description: Percentage of the total backplane-facing capacity that is currently available to the front
panel ports taking into account failures and/or degradation within the system.
    """
    return self.__available_pct
      
  def _set_available_pct(self, v, load=False):
    """
    Setter method for available_pct, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/available_pct (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_available_pct is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_available_pct() directly.

    YANG Description: Percentage of the total backplane-facing capacity that is currently available to the front
panel ports taking into account failures and/or degradation within the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """available_pct must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__available_pct = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_available_pct(self):
    self.__available_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)

  total = __builtin__.property(_get_total)
  consumed_capacity = __builtin__.property(_get_consumed_capacity)
  available_pct = __builtin__.property(_get_available_pct)


  _pyangbind_elements = OrderedDict([('total', total), ('consumed_capacity', consumed_capacity), ('available_pct', available_pct), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/integrated-circuit/backplane-facing-capacity/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to backplane capacity.
  """
  __slots__ = ('_path_helper', '_extmethods', '__total','__consumed_capacity','__available_pct',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__total = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    self.__consumed_capacity = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    self.__available_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)

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
      return ['components', 'component', 'integrated-circuit', 'backplane-facing-capacity', 'state']

  def _get_total(self):
    """
    Getter method for total, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/total (uint64)

    YANG Description: Total backplane-facing capacity that is available in the presence
of no link failures or degradation.
    """
    return self.__total
      
  def _set_total(self, v, load=False):
    """
    Setter method for total, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/total (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total() directly.

    YANG Description: Total backplane-facing capacity that is available in the presence
of no link failures or degradation.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)""",
        })

    self.__total = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total(self):
    self.__total = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)


  def _get_consumed_capacity(self):
    """
    Getter method for consumed_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/consumed_capacity (uint64)

    YANG Description: Backplane-facing capacity that is consumed by front-panel ports that are connected
to the integrated circuit.
    """
    return self.__consumed_capacity
      
  def _set_consumed_capacity(self, v, load=False):
    """
    Setter method for consumed_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/consumed_capacity (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_consumed_capacity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_consumed_capacity() directly.

    YANG Description: Backplane-facing capacity that is consumed by front-panel ports that are connected
to the integrated circuit.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """consumed_capacity must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)""",
        })

    self.__consumed_capacity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_consumed_capacity(self):
    self.__consumed_capacity = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="consumed-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='uint64', is_config=False)


  def _get_available_pct(self):
    """
    Getter method for available_pct, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/available_pct (oc-types:percentage)

    YANG Description: Percentage of the total backplane-facing capacity that is currently available to the front
panel ports taking into account failures and/or degradation within the system.
    """
    return self.__available_pct
      
  def _set_available_pct(self, v, load=False):
    """
    Setter method for available_pct, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity/state/available_pct (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_available_pct is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_available_pct() directly.

    YANG Description: Percentage of the total backplane-facing capacity that is currently available to the front
panel ports taking into account failures and/or degradation within the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """available_pct must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__available_pct = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_available_pct(self):
    self.__available_pct = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="available-pct", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='oc-types:percentage', is_config=False)

  total = __builtin__.property(_get_total)
  consumed_capacity = __builtin__.property(_get_consumed_capacity)
  available_pct = __builtin__.property(_get_available_pct)


  _pyangbind_elements = OrderedDict([('total', total), ('consumed_capacity', consumed_capacity), ('available_pct', available_pct), ])



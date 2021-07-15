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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet/poe/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for PoE
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__power_used','__power_class',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    self.__power_used = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)
    self.__power_class = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet', 'poe', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/enabled (boolean)

    YANG Description: Enable or disable PoE in the ethernet interface.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enable or disable PoE in the ethernet interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)


  def _get_power_used(self):
    """
    Getter method for power_used, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_used (decimal64)

    YANG Description: Power used by the ethernet interface in Watts.
    """
    return self.__power_used
      
  def _set_power_used(self, v, load=False):
    """
    Setter method for power_used, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_used (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_used is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_used() directly.

    YANG Description: Power used by the ethernet interface in Watts.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_used must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)""",
        })

    self.__power_used = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_used(self):
    self.__power_used = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)


  def _get_power_class(self):
    """
    Getter method for power_class, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_class (uint8)

    YANG Description: IEEE 802.3af Power class detected for this ethernet
interface.
    """
    return self.__power_class
      
  def _set_power_class(self, v, load=False):
    """
    Setter method for power_class, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_class (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_class() directly.

    YANG Description: IEEE 802.3af Power class detected for this ethernet
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_class must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)""",
        })

    self.__power_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_class(self):
    self.__power_class = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  power_used = __builtin__.property(_get_power_used)
  power_class = __builtin__.property(_get_power_class)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('power_used', power_used), ('power_class', power_class), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/interfaces/interface/ethernet/poe/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for PoE
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__power_used','__power_class',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    self.__power_used = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)
    self.__power_class = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)

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
      return ['access-points', 'access-point', 'interfaces', 'interface', 'ethernet', 'poe', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/enabled (boolean)

    YANG Description: Enable or disable PoE in the ethernet interface.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enable or disable PoE in the ethernet interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='boolean', is_config=False)


  def _get_power_used(self):
    """
    Getter method for power_used, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_used (decimal64)

    YANG Description: Power used by the ethernet interface in Watts.
    """
    return self.__power_used
      
  def _set_power_used(self, v, load=False):
    """
    Setter method for power_used, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_used (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_used is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_used() directly.

    YANG Description: Power used by the ethernet interface in Watts.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_used must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)""",
        })

    self.__power_used = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_used(self):
    self.__power_used = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="power-used", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='decimal64', is_config=False)


  def _get_power_class(self):
    """
    Getter method for power_class, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_class (uint8)

    YANG Description: IEEE 802.3af Power class detected for this ethernet
interface.
    """
    return self.__power_class
      
  def _set_power_class(self, v, load=False):
    """
    Setter method for power_class, mapped from YANG variable /access_points/access_point/interfaces/interface/ethernet/poe/state/power_class (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_class() directly.

    YANG Description: IEEE 802.3af Power class detected for this ethernet
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_class must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)""",
        })

    self.__power_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_class(self):
    self.__power_class = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="power-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/ap-interfaces', defining_module='openconfig-ap-interfaces', yang_type='uint8', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  power_used = __builtin__.property(_get_power_used)
  power_class = __builtin__.property(_get_power_class)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('power_used', power_used), ('power_class', power_class), ])



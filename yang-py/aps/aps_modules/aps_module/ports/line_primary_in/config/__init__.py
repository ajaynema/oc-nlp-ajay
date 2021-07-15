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
  from YANG module openconfig-transport-line-protection - based on the path /aps/aps-modules/aps-module/ports/line-primary-in/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for the line primary input port
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__target_attenuation',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='boolean', is_config=True)
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=True)

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
      return ['aps', 'aps-modules', 'aps-module', 'ports', 'line-primary-in', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_primary_in/config/enabled (boolean)

    YANG Description: This leaf contains the configured, desired state of the
port. Disabling the port turns off alarm reporting for
the port
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_primary_in/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: This leaf contains the configured, desired state of the
port. Disabling the port turns off alarm reporting for
the port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='boolean', is_config=True)


  def _get_target_attenuation(self):
    """
    Getter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_primary_in/config/target_attenuation (decimal64)

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB.
    """
    return self.__target_attenuation
      
  def _set_target_attenuation(self, v, load=False):
    """
    Setter method for target_attenuation, mapped from YANG variable /aps/aps_modules/aps_module/ports/line_primary_in/config/target_attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_attenuation() directly.

    YANG Description: Target attenuation of the variable optical attenuator
associated with the port in increments of 0.01 dB.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=True)""",
        })

    self.__target_attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_attenuation(self):
    self.__target_attenuation = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-transport-line-protection', defining_module='openconfig-transport-line-protection', yang_type='decimal64', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  target_attenuation = __builtin__.property(_get_target_attenuation, _set_target_attenuation)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('target_attenuation', target_attenuation), ])



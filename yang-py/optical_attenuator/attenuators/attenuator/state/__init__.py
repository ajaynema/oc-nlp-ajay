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

from . import actual_attenuation
from . import output_power_total
from . import optical_return_loss
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-optical-attenuator - based on the path /optical-attenuator/attenuators/attenuator/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the attenuator
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__attenuation_mode','__target_output_power','__attenuation','__enabled','__component','__ingress_port','__egress_port','__actual_attenuation','__output_power_total','__optical_return_loss',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='string', is_config=False)
    self.__attenuation_mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}},), is_leaf=True, yang_name="attenuation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='identityref', is_config=False)
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)
    self.__attenuation = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='boolean', is_config=False)
    self.__component = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    self.__ingress_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ingress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    self.__egress_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="egress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    self.__actual_attenuation = YANGDynClass(base=actual_attenuation.actual_attenuation, is_container='container', yang_name="actual-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)
    self.__output_power_total = YANGDynClass(base=output_power_total.output_power_total, is_container='container', yang_name="output-power-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)
    self.__optical_return_loss = YANGDynClass(base=optical_return_loss.optical_return_loss, is_container='container', yang_name="optical-return-loss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)

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
      return ['optical-attenuator', 'attenuators', 'attenuator', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/name (string)

    YANG Description: User-defined name assigned to identify a specific attenuator
in the device
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: User-defined name assigned to identify a specific attenuator
in the device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='string', is_config=False)


  def _get_attenuation_mode(self):
    """
    Getter method for attenuation_mode, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/attenuation_mode (identityref)

    YANG Description: The operating mode of the attenuator
    """
    return self.__attenuation_mode
      
  def _set_attenuation_mode(self, v, load=False):
    """
    Setter method for attenuation_mode, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/attenuation_mode (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuation_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuation_mode() directly.

    YANG Description: The operating mode of the attenuator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}},), is_leaf=True, yang_name="attenuation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuation_mode must be of a type compatible with identityref""",
          'defined-type': "openconfig-optical-attenuator:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}},), is_leaf=True, yang_name="attenuation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='identityref', is_config=False)""",
        })

    self.__attenuation_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuation_mode(self):
    self.__attenuation_mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_POWER': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}, 'oc-opt-att:CONSTANT_ATTENUATION': {'@module': 'openconfig-optical-attenuator', '@namespace': 'http://openconfig.net/yang/optical-attenuator'}},), is_leaf=True, yang_name="attenuation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='identityref', is_config=False)


  def _get_target_output_power(self):
    """
    Getter method for target_output_power, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/target_output_power (decimal64)

    YANG Description: Power level set on the output of attenuator.  This leaf is
only relevant when in CONSTANT_POWER mode.
    """
    return self.__target_output_power
      
  def _set_target_output_power(self, v, load=False):
    """
    Setter method for target_output_power, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/target_output_power (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_output_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_output_power() directly.

    YANG Description: Power level set on the output of attenuator.  This leaf is
only relevant when in CONSTANT_POWER mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_output_power must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)""",
        })

    self.__target_output_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_output_power(self):
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)


  def _get_attenuation(self):
    """
    Getter method for attenuation, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/attenuation (decimal64)

    YANG Description: Attenuation applied by the attenuator.  This leaf is only
relevant when in CONSTANT_ATTENUATION mode.
    """
    return self.__attenuation
      
  def _set_attenuation(self, v, load=False):
    """
    Setter method for attenuation, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/attenuation (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attenuation() directly.

    YANG Description: Attenuation applied by the attenuator.  This leaf is only
relevant when in CONSTANT_ATTENUATION mode.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attenuation must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)""",
        })

    self.__attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attenuation(self):
    self.__attenuation = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='decimal64', is_config=False)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/enabled (boolean)

    YANG Description: When true, attenuator is set to specified attenuation or varies to
maintain constant output power.  When false, the attenuator is set
max attenuation or blocked.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When true, attenuator is set to specified attenuation or varies to
maintain constant output power.  When false, the attenuator is set
max attenuation or blocked.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='boolean', is_config=False)


  def _get_component(self):
    """
    Getter method for component, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/component (leafref)

    YANG Description: Reference to the system-supplied physical component that
the attenuator block is contained within. Multiple
attenuator blocks may be contained within the same
physical component.
    """
    return self.__component
      
  def _set_component(self, v, load=False):
    """
    Setter method for component, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/component (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_component is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_component() directly.

    YANG Description: Reference to the system-supplied physical component that
the attenuator block is contained within. Multiple
attenuator blocks may be contained within the same
physical component.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """component must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)""",
        })

    self.__component = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_component(self):
    self.__component = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="component", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)


  def _get_ingress_port(self):
    """
    Getter method for ingress_port, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/ingress_port (leafref)

    YANG Description: Reference to system-supplied name of the attenuator ingress
port. This leaf is only valid for ports of type INGRESS.
    """
    return self.__ingress_port
      
  def _set_ingress_port(self, v, load=False):
    """
    Setter method for ingress_port, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/ingress_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_port() directly.

    YANG Description: Reference to system-supplied name of the attenuator ingress
port. This leaf is only valid for ports of type INGRESS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="ingress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ingress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)""",
        })

    self.__ingress_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_port(self):
    self.__ingress_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="ingress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)


  def _get_egress_port(self):
    """
    Getter method for egress_port, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/egress_port (leafref)

    YANG Description: Reference to system-supplied name of the attenuator egress
port. This leaf is only valid for ports of type EGRESS.
    """
    return self.__egress_port
      
  def _set_egress_port(self, v, load=False):
    """
    Setter method for egress_port, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/egress_port (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress_port() directly.

    YANG Description: Reference to system-supplied name of the attenuator egress
port. This leaf is only valid for ports of type EGRESS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="egress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress_port must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="egress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)""",
        })

    self.__egress_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress_port(self):
    self.__egress_port = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="egress-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='leafref', is_config=False)


  def _get_actual_attenuation(self):
    """
    Getter method for actual_attenuation, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/actual_attenuation (container)

    YANG Description: The actual attenuation applied by the attenuator in units of
0.01dB. If avg/min/max statistics are not supported,
just supply the instant value
    """
    return self.__actual_attenuation
      
  def _set_actual_attenuation(self, v, load=False):
    """
    Setter method for actual_attenuation, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/actual_attenuation (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actual_attenuation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actual_attenuation() directly.

    YANG Description: The actual attenuation applied by the attenuator in units of
0.01dB. If avg/min/max statistics are not supported,
just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=actual_attenuation.actual_attenuation, is_container='container', yang_name="actual-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actual_attenuation must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=actual_attenuation.actual_attenuation, is_container='container', yang_name="actual-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)""",
        })

    self.__actual_attenuation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actual_attenuation(self):
    self.__actual_attenuation = YANGDynClass(base=actual_attenuation.actual_attenuation, is_container='container', yang_name="actual-attenuation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)


  def _get_output_power_total(self):
    """
    Getter method for output_power_total, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/output_power_total (container)

    YANG Description: The total output optical power of this port in units
of 0.01dBm. If avg/min/max statistics are not supported,
just supply the instant value
    """
    return self.__output_power_total
      
  def _set_output_power_total(self, v, load=False):
    """
    Setter method for output_power_total, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/output_power_total (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_power_total is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_power_total() directly.

    YANG Description: The total output optical power of this port in units
of 0.01dBm. If avg/min/max statistics are not supported,
just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=output_power_total.output_power_total, is_container='container', yang_name="output-power-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_power_total must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=output_power_total.output_power_total, is_container='container', yang_name="output-power-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)""",
        })

    self.__output_power_total = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_power_total(self):
    self.__output_power_total = YANGDynClass(base=output_power_total.output_power_total, is_container='container', yang_name="output-power-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)


  def _get_optical_return_loss(self):
    """
    Getter method for optical_return_loss, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/optical_return_loss (container)

    YANG Description: The optical return loss (ORL) is the ratio of the light
reflected back into the port to the light launched out of
the port. ORL is in units of 0.01dBm. If avg/min/max
statistics are not supported, just supply the instant value.
    """
    return self.__optical_return_loss
      
  def _set_optical_return_loss(self, v, load=False):
    """
    Setter method for optical_return_loss, mapped from YANG variable /optical_attenuator/attenuators/attenuator/state/optical_return_loss (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optical_return_loss is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optical_return_loss() directly.

    YANG Description: The optical return loss (ORL) is the ratio of the light
reflected back into the port to the light launched out of
the port. ORL is in units of 0.01dBm. If avg/min/max
statistics are not supported, just supply the instant value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=optical_return_loss.optical_return_loss, is_container='container', yang_name="optical-return-loss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optical_return_loss must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optical_return_loss.optical_return_loss, is_container='container', yang_name="optical-return-loss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)""",
        })

    self.__optical_return_loss = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optical_return_loss(self):
    self.__optical_return_loss = YANGDynClass(base=optical_return_loss.optical_return_loss, is_container='container', yang_name="optical-return-loss", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-attenuator', defining_module='openconfig-optical-attenuator', yang_type='container', is_config=False)

  name = __builtin__.property(_get_name)
  attenuation_mode = __builtin__.property(_get_attenuation_mode)
  target_output_power = __builtin__.property(_get_target_output_power)
  attenuation = __builtin__.property(_get_attenuation)
  enabled = __builtin__.property(_get_enabled)
  component = __builtin__.property(_get_component)
  ingress_port = __builtin__.property(_get_ingress_port)
  egress_port = __builtin__.property(_get_egress_port)
  actual_attenuation = __builtin__.property(_get_actual_attenuation)
  output_power_total = __builtin__.property(_get_output_power_total)
  optical_return_loss = __builtin__.property(_get_optical_return_loss)


  _pyangbind_elements = OrderedDict([('name', name), ('attenuation_mode', attenuation_mode), ('target_output_power', target_output_power), ('attenuation', attenuation), ('enabled', enabled), ('component', component), ('ingress_port', ingress_port), ('egress_port', egress_port), ('actual_attenuation', actual_attenuation), ('output_power_total', output_power_total), ('optical_return_loss', optical_return_loss), ])


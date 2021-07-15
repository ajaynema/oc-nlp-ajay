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

from . import output_power
from . import input_power
from . import laser_bias_current
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/transceiver/physical-channels/channel/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for channels
  """
  __slots__ = ('_path_helper', '_extmethods', '__index','__associated_optical_channel','__description','__tx_laser','__target_output_power','__output_frequency','__output_power','__input_power','__laser_bias_current',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=False)
    self.__associated_optical_channel = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="associated-optical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='leafref', is_config=False)
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=False)
    self.__tx_laser = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=False)
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=False)
    self.__output_frequency = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="output-frequency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='oc-opt-types:frequency-type', is_config=False)
    self.__output_power = YANGDynClass(base=output_power.output_power, is_container='container', yang_name="output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)
    self.__input_power = YANGDynClass(base=input_power.input_power, is_container='container', yang_name="input-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)
    self.__laser_bias_current = YANGDynClass(base=laser_bias_current.laser_bias_current, is_container='container', yang_name="laser-bias-current", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)

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
      return ['components', 'component', 'transceiver', 'physical-channels', 'channel', 'state']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/index (uint16)

    YANG Description: Index of the physical channnel or lane within a physical
client port
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/index (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: Index of the physical channnel or lane within a physical
client port
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=False)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..max']}), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='uint16', is_config=False)


  def _get_associated_optical_channel(self):
    """
    Getter method for associated_optical_channel, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/associated_optical_channel (leafref)

    YANG Description: A physical channel may reference an optical channel
component. If the physical channel does make this optional
reference, then a limited set of leaves will apply within
the physical channel to avoid duplication within the optical
channel.
    """
    return self.__associated_optical_channel
      
  def _set_associated_optical_channel(self, v, load=False):
    """
    Setter method for associated_optical_channel, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/associated_optical_channel (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_associated_optical_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_associated_optical_channel() directly.

    YANG Description: A physical channel may reference an optical channel
component. If the physical channel does make this optional
reference, then a limited set of leaves will apply within
the physical channel to avoid duplication within the optical
channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="associated-optical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """associated_optical_channel must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="associated-optical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='leafref', is_config=False)""",
        })

    self.__associated_optical_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_associated_optical_channel(self):
    self.__associated_optical_channel = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="associated-optical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='leafref', is_config=False)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/description (string)

    YANG Description: Text description for the client physical channel
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Text description for the client physical channel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=False)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='string', is_config=False)


  def _get_tx_laser(self):
    """
    Getter method for tx_laser, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/tx_laser (boolean)

    YANG Description: Enable (true) or disable (false) the transmit label for the
channel
    """
    return self.__tx_laser
      
  def _set_tx_laser(self, v, load=False):
    """
    Setter method for tx_laser, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/tx_laser (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_laser is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_laser() directly.

    YANG Description: Enable (true) or disable (false) the transmit label for the
channel
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_laser must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=False)""",
        })

    self.__tx_laser = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_laser(self):
    self.__tx_laser = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="tx-laser", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='boolean', is_config=False)


  def _get_target_output_power(self):
    """
    Getter method for target_output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/target_output_power (decimal64)

    YANG Description: Target output optical power level of the optical channel,
expressed in increments of 0.01 dBm (decibel-milliwats)
    """
    return self.__target_output_power
      
  def _set_target_output_power(self, v, load=False):
    """
    Setter method for target_output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/target_output_power (decimal64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_output_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_output_power() directly.

    YANG Description: Target output optical power level of the optical channel,
expressed in increments of 0.01 dBm (decibel-milliwats)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_output_power must be of a type compatible with decimal64""",
          'defined-type': "decimal64",
          'generated-type': """YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=False)""",
        })

    self.__target_output_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_output_power(self):
    self.__target_output_power = YANGDynClass(base=RestrictedPrecisionDecimalType(precision=2), is_leaf=True, yang_name="target-output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='decimal64', is_config=False)


  def _get_output_frequency(self):
    """
    Getter method for output_frequency, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/output_frequency (oc-opt-types:frequency-type)

    YANG Description: The frequency in MHz of the individual physical channel
(e.g. ITU C50 - 195.0THz and would be reported as
195,000,000 MHz in this model). This attribute is not
configurable on most client ports.
    """
    return self.__output_frequency
      
  def _set_output_frequency(self, v, load=False):
    """
    Setter method for output_frequency, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/output_frequency (oc-opt-types:frequency-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_frequency is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_frequency() directly.

    YANG Description: The frequency in MHz of the individual physical channel
(e.g. ITU C50 - 195.0THz and would be reported as
195,000,000 MHz in this model). This attribute is not
configurable on most client ports.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="output-frequency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='oc-opt-types:frequency-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_frequency must be of a type compatible with oc-opt-types:frequency-type""",
          'defined-type': "oc-opt-types:frequency-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="output-frequency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='oc-opt-types:frequency-type', is_config=False)""",
        })

    self.__output_frequency = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_frequency(self):
    self.__output_frequency = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="output-frequency", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='oc-opt-types:frequency-type', is_config=False)


  def _get_output_power(self):
    """
    Getter method for output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/output_power (container)

    YANG Description: The output optical power of a physical channel in units
of 0.01dBm, which may be associated with individual
physical channels, or an aggregate of multiple physical
channels (i.e., for the overall transceiver). For an
aggregate, this may be a measurement from a photodetector
or a a calculation performed on the device by summing up
all of the related individual physical channels.
Values include the instantaneous, average, minimum, and
maximum statistics. If avg/min/max statistics are not
supported, the target is expected to just supply the
instant value
    """
    return self.__output_power
      
  def _set_output_power(self, v, load=False):
    """
    Setter method for output_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/output_power (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_power() directly.

    YANG Description: The output optical power of a physical channel in units
of 0.01dBm, which may be associated with individual
physical channels, or an aggregate of multiple physical
channels (i.e., for the overall transceiver). For an
aggregate, this may be a measurement from a photodetector
or a a calculation performed on the device by summing up
all of the related individual physical channels.
Values include the instantaneous, average, minimum, and
maximum statistics. If avg/min/max statistics are not
supported, the target is expected to just supply the
instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=output_power.output_power, is_container='container', yang_name="output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_power must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=output_power.output_power, is_container='container', yang_name="output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)""",
        })

    self.__output_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_power(self):
    self.__output_power = YANGDynClass(base=output_power.output_power, is_container='container', yang_name="output-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)


  def _get_input_power(self):
    """
    Getter method for input_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/input_power (container)

    YANG Description: The input optical power of a physical channel in units
of 0.01dBm, which may be associated with individual
physical channels, or an aggregate of multiple physical
channels (i.e., for the overall transceiver). For an
aggregate, this may be a measurement from a photodetector
or a a calculation performed on the device by summing up
all of the related individual physical channels.
Values include the instantaneous, average, minimum, and
maximum statistics. If avg/min/max statistics are not
supported, the target is expected to just supply the
instant value
    """
    return self.__input_power
      
  def _set_input_power(self, v, load=False):
    """
    Setter method for input_power, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/input_power (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_input_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_input_power() directly.

    YANG Description: The input optical power of a physical channel in units
of 0.01dBm, which may be associated with individual
physical channels, or an aggregate of multiple physical
channels (i.e., for the overall transceiver). For an
aggregate, this may be a measurement from a photodetector
or a a calculation performed on the device by summing up
all of the related individual physical channels.
Values include the instantaneous, average, minimum, and
maximum statistics. If avg/min/max statistics are not
supported, the target is expected to just supply the
instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=input_power.input_power, is_container='container', yang_name="input-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """input_power must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=input_power.input_power, is_container='container', yang_name="input-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)""",
        })

    self.__input_power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_input_power(self):
    self.__input_power = YANGDynClass(base=input_power.input_power, is_container='container', yang_name="input-power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)


  def _get_laser_bias_current(self):
    """
    Getter method for laser_bias_current, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current (container)

    YANG Description: The current applied by the system to the transmit laser to
achieve the output power. The current is expressed in mA
with up to two decimal precision. Values include the
instantaneous, average, minimum, and maximum statistics.
If avg/min/max statistics are not supported, the target is
expected to just supply the instant value
    """
    return self.__laser_bias_current
      
  def _set_laser_bias_current(self, v, load=False):
    """
    Setter method for laser_bias_current, mapped from YANG variable /components/component/transceiver/physical_channels/channel/state/laser_bias_current (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_laser_bias_current is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_laser_bias_current() directly.

    YANG Description: The current applied by the system to the transmit laser to
achieve the output power. The current is expressed in mA
with up to two decimal precision. Values include the
instantaneous, average, minimum, and maximum statistics.
If avg/min/max statistics are not supported, the target is
expected to just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=laser_bias_current.laser_bias_current, is_container='container', yang_name="laser-bias-current", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """laser_bias_current must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=laser_bias_current.laser_bias_current, is_container='container', yang_name="laser-bias-current", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)""",
        })

    self.__laser_bias_current = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_laser_bias_current(self):
    self.__laser_bias_current = YANGDynClass(base=laser_bias_current.laser_bias_current, is_container='container', yang_name="laser-bias-current", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/transceiver', defining_module='openconfig-platform-transceiver', yang_type='container', is_config=False)

  index = __builtin__.property(_get_index)
  associated_optical_channel = __builtin__.property(_get_associated_optical_channel)
  description = __builtin__.property(_get_description)
  tx_laser = __builtin__.property(_get_tx_laser)
  target_output_power = __builtin__.property(_get_target_output_power)
  output_frequency = __builtin__.property(_get_output_frequency)
  output_power = __builtin__.property(_get_output_power)
  input_power = __builtin__.property(_get_input_power)
  laser_bias_current = __builtin__.property(_get_laser_bias_current)


  _pyangbind_elements = OrderedDict([('index', index), ('associated_optical_channel', associated_optical_channel), ('description', description), ('tx_laser', tx_laser), ('target_output_power', target_output_power), ('output_frequency', output_frequency), ('output_power', output_power), ('input_power', input_power), ('laser_bias_current', laser_bias_current), ])



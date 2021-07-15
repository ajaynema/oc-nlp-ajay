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
  from YANG module openconfig-sampling-sflow - based on the path /sampling/sflow/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for global sFlow.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__source_address','__sampling_rate','__sample_size',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    self.__sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)
    self.__sample_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)

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
      return ['sampling', 'sflow', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /sampling/sflow/state/enabled (boolean)

    YANG Description: Enables or disables sFlow sampling for the device.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /sampling/sflow/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enables or disables sFlow sampling for the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)


  def _get_source_address(self):
    """
    Getter method for source_address, mapped from YANG variable /sampling/sflow/state/source_address (oc-inet:ip-address)

    YANG Description: Sets the source IP address for sFlow datagrams sent to
sFlow collectors.
    """
    return self.__source_address
      
  def _set_source_address(self, v, load=False):
    """
    Setter method for source_address, mapped from YANG variable /sampling/sflow/state/source_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_address() directly.

    YANG Description: Sets the source IP address for sFlow datagrams sent to
sFlow collectors.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)""",
        })

    self.__source_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_address(self):
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)


  def _get_sampling_rate(self):
    """
    Getter method for sampling_rate, mapped from YANG variable /sampling/sflow/state/sampling_rate (uint32)

    YANG Description: Sets the global packet sampling rate.  The rate is
is expressed as an integer N, where the intended sampling
rate is 1/N packets.  An implementation may implement the
sampling rate as a statistical average, rather than a strict
periodic sampling.

The allowable sampling rate range is generally a
property of the system, e.g., determined by the
capability of the hardware.
    """
    return self.__sampling_rate
      
  def _set_sampling_rate(self, v, load=False):
    """
    Setter method for sampling_rate, mapped from YANG variable /sampling/sflow/state/sampling_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sampling_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sampling_rate() directly.

    YANG Description: Sets the global packet sampling rate.  The rate is
is expressed as an integer N, where the intended sampling
rate is 1/N packets.  An implementation may implement the
sampling rate as a statistical average, rather than a strict
periodic sampling.

The allowable sampling rate range is generally a
property of the system, e.g., determined by the
capability of the hardware.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sampling_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)""",
        })

    self.__sampling_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sampling_rate(self):
    self.__sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)


  def _get_sample_size(self):
    """
    Getter method for sample_size, mapped from YANG variable /sampling/sflow/state/sample_size (uint16)

    YANG Description: Sets the maximum number of bytes to be copied from a
sampled packet.
    """
    return self.__sample_size
      
  def _set_sample_size(self, v, load=False):
    """
    Setter method for sample_size, mapped from YANG variable /sampling/sflow/state/sample_size (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_size() directly.

    YANG Description: Sets the maximum number of bytes to be copied from a
sampled packet.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_size must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)""",
        })

    self.__sample_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_size(self):
    self.__sample_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  source_address = __builtin__.property(_get_source_address)
  sampling_rate = __builtin__.property(_get_sampling_rate)
  sample_size = __builtin__.property(_get_sample_size)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('source_address', source_address), ('sampling_rate', sampling_rate), ('sample_size', sample_size), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-sampling-sflow - based on the path /sampling/sflow/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for global sFlow.
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__source_address','__sampling_rate','__sample_size',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    self.__sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)
    self.__sample_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)

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
      return ['sampling', 'sflow', 'state']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /sampling/sflow/state/enabled (boolean)

    YANG Description: Enables or disables sFlow sampling for the device.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /sampling/sflow/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enables or disables sFlow sampling for the device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='boolean', is_config=False)


  def _get_source_address(self):
    """
    Getter method for source_address, mapped from YANG variable /sampling/sflow/state/source_address (oc-inet:ip-address)

    YANG Description: Sets the source IP address for sFlow datagrams sent to
sFlow collectors.
    """
    return self.__source_address
      
  def _set_source_address(self, v, load=False):
    """
    Setter method for source_address, mapped from YANG variable /sampling/sflow/state/source_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source_address() directly.

    YANG Description: Sets the source IP address for sFlow datagrams sent to
sFlow collectors.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)""",
        })

    self.__source_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source_address(self):
    self.__source_address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="source-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='oc-inet:ip-address', is_config=False)


  def _get_sampling_rate(self):
    """
    Getter method for sampling_rate, mapped from YANG variable /sampling/sflow/state/sampling_rate (uint32)

    YANG Description: Sets the global packet sampling rate.  The rate is
is expressed as an integer N, where the intended sampling
rate is 1/N packets.  An implementation may implement the
sampling rate as a statistical average, rather than a strict
periodic sampling.

The allowable sampling rate range is generally a
property of the system, e.g., determined by the
capability of the hardware.
    """
    return self.__sampling_rate
      
  def _set_sampling_rate(self, v, load=False):
    """
    Setter method for sampling_rate, mapped from YANG variable /sampling/sflow/state/sampling_rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sampling_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sampling_rate() directly.

    YANG Description: Sets the global packet sampling rate.  The rate is
is expressed as an integer N, where the intended sampling
rate is 1/N packets.  An implementation may implement the
sampling rate as a statistical average, rather than a strict
periodic sampling.

The allowable sampling rate range is generally a
property of the system, e.g., determined by the
capability of the hardware.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sampling_rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)""",
        })

    self.__sampling_rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sampling_rate(self):
    self.__sampling_rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sampling-rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint32', is_config=False)


  def _get_sample_size(self):
    """
    Getter method for sample_size, mapped from YANG variable /sampling/sflow/state/sample_size (uint16)

    YANG Description: Sets the maximum number of bytes to be copied from a
sampled packet.
    """
    return self.__sample_size
      
  def _set_sample_size(self, v, load=False):
    """
    Setter method for sample_size, mapped from YANG variable /sampling/sflow/state/sample_size (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_size() directly.

    YANG Description: Sets the maximum number of bytes to be copied from a
sampled packet.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_size must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)""",
        })

    self.__sample_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_size(self):
    self.__sample_size = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(128), is_leaf=True, yang_name="sample-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/sampling/sflow', defining_module='openconfig-sampling-sflow', yang_type='uint16', is_config=False)

  enabled = __builtin__.property(_get_enabled)
  source_address = __builtin__.property(_get_source_address)
  sampling_rate = __builtin__.property(_get_sampling_rate)
  sample_size = __builtin__.property(_get_sample_size)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('source_address', source_address), ('sampling_rate', sampling_rate), ('sample_size', sample_size), ])



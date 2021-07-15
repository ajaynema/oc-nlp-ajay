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
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ethernet/lldp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LLDP configuration data for logical channels
  """
  __slots__ = ('_path_helper', '_extmethods', '__enabled','__snooping',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)
    self.__snooping = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="snooping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ethernet', 'lldp', 'config']

  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/config/enabled (boolean)

    YANG Description: Enable or disable the LLDP protocol on the logical channel.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: Enable or disable the LLDP protocol on the logical channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)


  def _get_snooping(self):
    """
    Getter method for snooping, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/config/snooping (boolean)

    YANG Description: If true, LLDP PDUs are only received and processed on
the logical-channel, but are not originated by the local
agent. The PDUs are not dropped by the logical channel after
processing, but relayed to the downstream link layer
neighbors. The snooping mode is valid only when LLDP is
enabled on the logical channel. The snooping mode is useful
when a logical channel does not want its link layer neighbors
to discover itself since, for example, it is a lower-layer
logical channel.
    """
    return self.__snooping
      
  def _set_snooping(self, v, load=False):
    """
    Setter method for snooping, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/config/snooping (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_snooping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_snooping() directly.

    YANG Description: If true, LLDP PDUs are only received and processed on
the logical-channel, but are not originated by the local
agent. The PDUs are not dropped by the logical channel after
processing, but relayed to the downstream link layer
neighbors. The snooping mode is valid only when LLDP is
enabled on the logical channel. The snooping mode is useful
when a logical channel does not want its link layer neighbors
to discover itself since, for example, it is a lower-layer
logical channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="snooping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """snooping must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="snooping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)""",
        })

    self.__snooping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_snooping(self):
    self.__snooping = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="snooping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='boolean', is_config=True)

  enabled = __builtin__.property(_get_enabled, _set_enabled)
  snooping = __builtin__.property(_get_snooping, _set_snooping)


  _pyangbind_elements = OrderedDict([('enabled', enabled), ('snooping', snooping), ])


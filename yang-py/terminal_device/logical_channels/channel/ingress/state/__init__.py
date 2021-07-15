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
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ingress/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the signal source for the
logical channel
  """
  __slots__ = ('_path_helper', '_extmethods', '__transceiver','__physical_channel','__interface',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__transceiver = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__physical_channel = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ingress', 'state']

  def _get_transceiver(self):
    """
    Getter method for transceiver, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/transceiver (leafref)

    YANG Description: Reference to the transceiver carrying the input signal
for the logical channel.  If specific physical channels
are mapped to the logical channel (as opposed to all
physical channels carried by the transceiver), they can be
specified in the list of physical channel references.
    """
    return self.__transceiver
      
  def _set_transceiver(self, v, load=False):
    """
    Setter method for transceiver, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/transceiver (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transceiver is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transceiver() directly.

    YANG Description: Reference to the transceiver carrying the input signal
for the logical channel.  If specific physical channels
are mapped to the logical channel (as opposed to all
physical channels carried by the transceiver), they can be
specified in the list of physical channel references.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transceiver must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__transceiver = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transceiver(self):
    self.__transceiver = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_physical_channel(self):
    """
    Getter method for physical_channel, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/physical_channel (leafref)

    YANG Description: This list should be populated with references
to the client physical channels that feed this logical
channel from the transceiver specified in the 'transceiver'
leaf, which must be specified.  If this leaf-list is empty,
all physical channels in the transceiver are assumed to be
mapped to the logical channel.
    """
    return self.__physical_channel
      
  def _set_physical_channel(self, v, load=False):
    """
    Setter method for physical_channel, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/physical_channel (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_physical_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_physical_channel() directly.

    YANG Description: This list should be populated with references
to the client physical channels that feed this logical
channel from the transceiver specified in the 'transceiver'
leaf, which must be specified.  If this leaf-list is empty,
all physical channels in the transceiver are assumed to be
mapped to the logical channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """physical_channel must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__physical_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_physical_channel(self):
    self.__physical_channel = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/interface (oc-if:base-interface-ref)

    YANG Description: Reference to the interface carrying the input signal
for the logical channel. The ingress will specify an interface
in the case of a transceiver being utilized directly in a
router and bypassing a dedicated terminal device. When
specified, the other leaves in the ingress config must be
empty.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/interface (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to the interface carrying the input signal
for the logical channel. The ingress will specify an interface
in the case of a transceiver being utilized directly in a
router and bypassing a dedicated terminal device. When
specified, the other leaves in the ingress config must be
empty.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)

  transceiver = __builtin__.property(_get_transceiver)
  physical_channel = __builtin__.property(_get_physical_channel)
  interface = __builtin__.property(_get_interface)


  _pyangbind_elements = OrderedDict([('transceiver', transceiver), ('physical_channel', physical_channel), ('interface', interface), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ingress/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the signal source for the
logical channel
  """
  __slots__ = ('_path_helper', '_extmethods', '__transceiver','__physical_channel','__interface',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__transceiver = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__physical_channel = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    self.__interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ingress', 'state']

  def _get_transceiver(self):
    """
    Getter method for transceiver, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/transceiver (leafref)

    YANG Description: Reference to the transceiver carrying the input signal
for the logical channel.  If specific physical channels
are mapped to the logical channel (as opposed to all
physical channels carried by the transceiver), they can be
specified in the list of physical channel references.
    """
    return self.__transceiver
      
  def _set_transceiver(self, v, load=False):
    """
    Setter method for transceiver, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/transceiver (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transceiver is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transceiver() directly.

    YANG Description: Reference to the transceiver carrying the input signal
for the logical channel.  If specific physical channels
are mapped to the logical channel (as opposed to all
physical channels carried by the transceiver), they can be
specified in the list of physical channel references.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transceiver must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__transceiver = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transceiver(self):
    self.__transceiver = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_physical_channel(self):
    """
    Getter method for physical_channel, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/physical_channel (leafref)

    YANG Description: This list should be populated with references
to the client physical channels that feed this logical
channel from the transceiver specified in the 'transceiver'
leaf, which must be specified.  If this leaf-list is empty,
all physical channels in the transceiver are assumed to be
mapped to the logical channel.
    """
    return self.__physical_channel
      
  def _set_physical_channel(self, v, load=False):
    """
    Setter method for physical_channel, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/physical_channel (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_physical_channel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_physical_channel() directly.

    YANG Description: This list should be populated with references
to the client physical channels that feed this logical
channel from the transceiver specified in the 'transceiver'
leaf, which must be specified.  If this leaf-list is empty,
all physical channels in the transceiver are assumed to be
mapped to the logical channel.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """physical_channel must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)""",
        })

    self.__physical_channel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_physical_channel(self):
    self.__physical_channel = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="physical-channel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='leafref', is_config=False)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/interface (oc-if:base-interface-ref)

    YANG Description: Reference to the interface carrying the input signal
for the logical channel. The ingress will specify an interface
in the case of a transceiver being utilized directly in a
router and bypassing a dedicated terminal device. When
specified, the other leaves in the ingress config must be
empty.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /terminal_device/logical_channels/channel/ingress/state/interface (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Reference to the interface carrying the input signal
for the logical channel. The ingress will specify an interface
in the case of a transceiver being utilized directly in a
router and bypassing a dedicated terminal device. When
specified, the other leaves in the ingress config must be
empty.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='oc-if:base-interface-ref', is_config=False)

  transceiver = __builtin__.property(_get_transceiver)
  physical_channel = __builtin__.property(_get_physical_channel)
  interface = __builtin__.property(_get_interface)


  _pyangbind_elements = OrderedDict([('transceiver', transceiver), ('physical_channel', physical_channel), ('interface', interface), ])



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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses/address/vrrp/vrrp-group/interface-tracking/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for VRRP interface tracking
  """
  __slots__ = ('_path_helper', '_extmethods', '__track_interface','__priority_decrement',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__track_interface = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="track-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)
    self.__priority_decrement = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="priority-decrement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=True)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses', 'address', 'vrrp', 'vrrp-group', 'interface-tracking', 'config']

  def _get_track_interface(self):
    """
    Getter method for track_interface, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/vrrp/vrrp_group/interface_tracking/config/track_interface (leafref)

    YANG Description: Sets a list of one or more interfaces that should
be tracked for up/down events to dynamically change the
priority state of the VRRP group, and potentially
change the mastership if the tracked interface going
down lowers the priority sufficiently.  Any of the tracked
interfaces going down will cause the priority to be lowered.
Some implementations may only support a single
tracked interface.
    """
    return self.__track_interface
      
  def _set_track_interface(self, v, load=False):
    """
    Setter method for track_interface, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/vrrp/vrrp_group/interface_tracking/config/track_interface (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_track_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_track_interface() directly.

    YANG Description: Sets a list of one or more interfaces that should
be tracked for up/down events to dynamically change the
priority state of the VRRP group, and potentially
change the mastership if the tracked interface going
down lowers the priority sufficiently.  Any of the tracked
interfaces going down will cause the priority to be lowered.
Some implementations may only support a single
tracked interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="track-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """track_interface must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="track-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)""",
        })

    self.__track_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_track_interface(self):
    self.__track_interface = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="track-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='leafref', is_config=True)


  def _get_priority_decrement(self):
    """
    Getter method for priority_decrement, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/vrrp/vrrp_group/interface_tracking/config/priority_decrement (uint8)

    YANG Description: Set the value to subtract from priority when
the tracked interface goes down
    """
    return self.__priority_decrement
      
  def _set_priority_decrement(self, v, load=False):
    """
    Setter method for priority_decrement, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/vrrp/vrrp_group/interface_tracking/config/priority_decrement (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority_decrement is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority_decrement() directly.

    YANG Description: Set the value to subtract from priority when
the tracked interface goes down
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="priority-decrement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority_decrement must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="priority-decrement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=True)""",
        })

    self.__priority_decrement = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority_decrement(self):
    self.__priority_decrement = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(0), is_leaf=True, yang_name="priority-decrement", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=True)

  track_interface = __builtin__.property(_get_track_interface, _set_track_interface)
  priority_decrement = __builtin__.property(_get_priority_decrement, _set_priority_decrement)


  _pyangbind_elements = OrderedDict([('track_interface', track_interface), ('priority_decrement', priority_decrement), ])



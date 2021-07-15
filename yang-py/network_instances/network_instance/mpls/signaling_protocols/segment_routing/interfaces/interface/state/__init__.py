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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS-specific Segment Routing operational state parameters
related to an interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__in_pkts','__in_octets','__out_pkts','__out_octets',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    self.__in_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__in_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'state']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/interface_id (string)

    YANG Description: A unique identifier for the interface.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: A unique identifier for the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)


  def _get_in_pkts(self):
    """
    Getter method for in_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_pkts (yang:counter64)

    YANG Description: A cumulative counter of the packets received within the context
which have matched a label corresponding to an SR Segment Identifier.
    """
    return self.__in_pkts
      
  def _set_in_pkts(self, v, load=False):
    """
    Setter method for in_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_pkts() directly.

    YANG Description: A cumulative counter of the packets received within the context
which have matched a label corresponding to an SR Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__in_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_pkts(self):
    self.__in_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_in_octets(self):
    """
    Getter method for in_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_octets (yang:counter64)

    YANG Description: The cumulative counter of the total bytes received within the context
which have matched a label corresponding to an SR Segment Identifier
    """
    return self.__in_octets
      
  def _set_in_octets(self, v, load=False):
    """
    Setter method for in_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_octets() directly.

    YANG Description: The cumulative counter of the total bytes received within the context
which have matched a label corresponding to an SR Segment Identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__in_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_octets(self):
    self.__in_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_out_pkts(self):
    """
    Getter method for out_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_pkts (yang:counter64)

    YANG Description: A cumulative counter of the total number of packets transmitted by
the local system within the context which have a label imposed that
corresponds to an Segment Identifier.
    """
    return self.__out_pkts
      
  def _set_out_pkts(self, v, load=False):
    """
    Setter method for out_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts() directly.

    YANG Description: A cumulative counter of the total number of packets transmitted by
the local system within the context which have a label imposed that
corresponds to an Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__out_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts(self):
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_out_octets(self):
    """
    Getter method for out_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_octets (yang:counter64)

    YANG Description: A cumulative counter of the total bytes transmitted by the local
system within the context which have a label imported that
corresponds to an SR Segment Identifier.
    """
    return self.__out_octets
      
  def _set_out_octets(self, v, load=False):
    """
    Setter method for out_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_octets() directly.

    YANG Description: A cumulative counter of the total bytes transmitted by the local
system within the context which have a label imported that
corresponds to an SR Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__out_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_octets(self):
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

  interface_id = __builtin__.property(_get_interface_id)
  in_pkts = __builtin__.property(_get_in_pkts)
  in_octets = __builtin__.property(_get_in_octets)
  out_pkts = __builtin__.property(_get_out_pkts)
  out_octets = __builtin__.property(_get_out_octets)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('in_pkts', in_pkts), ('in_octets', in_octets), ('out_pkts', out_pkts), ('out_octets', out_octets), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/interfaces/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MPLS-specific Segment Routing operational state parameters
related to an interface.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interface_id','__in_pkts','__in_octets','__out_pkts','__out_octets',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    self.__in_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__in_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

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
      return ['network-instances', 'network-instance', 'mpls', 'signaling-protocols', 'segment-routing', 'interfaces', 'interface', 'state']

  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/interface_id (string)

    YANG Description: A unique identifier for the interface.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: A unique identifier for the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='string', is_config=False)


  def _get_in_pkts(self):
    """
    Getter method for in_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_pkts (yang:counter64)

    YANG Description: A cumulative counter of the packets received within the context
which have matched a label corresponding to an SR Segment Identifier.
    """
    return self.__in_pkts
      
  def _set_in_pkts(self, v, load=False):
    """
    Setter method for in_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_pkts() directly.

    YANG Description: A cumulative counter of the packets received within the context
which have matched a label corresponding to an SR Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__in_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_pkts(self):
    self.__in_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_in_octets(self):
    """
    Getter method for in_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_octets (yang:counter64)

    YANG Description: The cumulative counter of the total bytes received within the context
which have matched a label corresponding to an SR Segment Identifier
    """
    return self.__in_octets
      
  def _set_in_octets(self, v, load=False):
    """
    Setter method for in_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/in_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_octets() directly.

    YANG Description: The cumulative counter of the total bytes received within the context
which have matched a label corresponding to an SR Segment Identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__in_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_octets(self):
    self.__in_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="in-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_out_pkts(self):
    """
    Getter method for out_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_pkts (yang:counter64)

    YANG Description: A cumulative counter of the total number of packets transmitted by
the local system within the context which have a label imposed that
corresponds to an Segment Identifier.
    """
    return self.__out_pkts
      
  def _set_out_pkts(self, v, load=False):
    """
    Setter method for out_pkts, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_pkts() directly.

    YANG Description: A cumulative counter of the total number of packets transmitted by
the local system within the context which have a label imposed that
corresponds to an Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__out_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_pkts(self):
    self.__out_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_out_octets(self):
    """
    Getter method for out_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_octets (yang:counter64)

    YANG Description: A cumulative counter of the total bytes transmitted by the local
system within the context which have a label imported that
corresponds to an SR Segment Identifier.
    """
    return self.__out_octets
      
  def _set_out_octets(self, v, load=False):
    """
    Setter method for out_octets, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/interfaces/interface/state/out_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_octets() directly.

    YANG Description: A cumulative counter of the total bytes transmitted by the local
system within the context which have a label imported that
corresponds to an SR Segment Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__out_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_octets(self):
    self.__out_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="out-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

  interface_id = __builtin__.property(_get_interface_id)
  in_pkts = __builtin__.property(_get_in_pkts)
  in_octets = __builtin__.property(_get_in_octets)
  out_pkts = __builtin__.property(_get_out_pkts)
  out_octets = __builtin__.property(_get_out_octets)


  _pyangbind_elements = OrderedDict([('interface_id', interface_id), ('in_pkts', in_pkts), ('in_octets', in_octets), ('out_pkts', out_pkts), ('out_octets', out_octets), ])



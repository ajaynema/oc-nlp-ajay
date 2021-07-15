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

from . import srgb_descriptor
class srgb_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SRGB Descriptors included within the SR
capability sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__srgb_descriptor',)

  _yang_name = 'srgb-descriptors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors']

  def _get_srgb_descriptor(self):
    """
    Getter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    return self.__srgb_descriptor
      
  def _set_srgb_descriptor(self, v, load=False):
    """
    Setter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srgb_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srgb_descriptor() directly.

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srgb_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__srgb_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srgb_descriptor(self):
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  srgb_descriptor = __builtin__.property(_get_srgb_descriptor)


  _pyangbind_elements = OrderedDict([('srgb_descriptor', srgb_descriptor), ])


from . import srgb_descriptor
class srgb_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SRGB Descriptors included within the SR
capability sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__srgb_descriptor',)

  _yang_name = 'srgb-descriptors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors']

  def _get_srgb_descriptor(self):
    """
    Getter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    return self.__srgb_descriptor
      
  def _set_srgb_descriptor(self, v, load=False):
    """
    Setter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srgb_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srgb_descriptor() directly.

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srgb_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__srgb_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srgb_descriptor(self):
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  srgb_descriptor = __builtin__.property(_get_srgb_descriptor)


  _pyangbind_elements = OrderedDict([('srgb_descriptor', srgb_descriptor), ])


from . import srgb_descriptor
class srgb_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SRGB Descriptors included within the SR
capability sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__srgb_descriptor',)

  _yang_name = 'srgb-descriptors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors']

  def _get_srgb_descriptor(self):
    """
    Getter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    return self.__srgb_descriptor
      
  def _set_srgb_descriptor(self, v, load=False):
    """
    Setter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srgb_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srgb_descriptor() directly.

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srgb_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__srgb_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srgb_descriptor(self):
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  srgb_descriptor = __builtin__.property(_get_srgb_descriptor)


  _pyangbind_elements = OrderedDict([('srgb_descriptor', srgb_descriptor), ])


from . import srgb_descriptor
class srgb_descriptors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/router-capabilities/capability/subtlvs/subtlv/segment-routing-capability/srgb-descriptors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SRGB Descriptors included within the SR
capability sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__srgb_descriptor',)

  _yang_name = 'srgb-descriptors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'router-capabilities', 'capability', 'subtlvs', 'subtlv', 'segment-routing-capability', 'srgb-descriptors']

  def _get_srgb_descriptor(self):
    """
    Getter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    return self.__srgb_descriptor
      
  def _set_srgb_descriptor(self, v, load=False):
    """
    Setter method for srgb_descriptor, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/router_capabilities/capability/subtlvs/subtlv/segment_routing_capability/srgb_descriptors/srgb_descriptor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srgb_descriptor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srgb_descriptor() directly.

    YANG Description: Descriptor entry within the SR capabilty
sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srgb_descriptor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__srgb_descriptor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srgb_descriptor(self):
    self.__srgb_descriptor = YANGDynClass(base=YANGListType("range",srgb_descriptor.srgb_descriptor, yang_name="srgb-descriptor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='range', extensions=None), is_container='list', yang_name="srgb-descriptor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  srgb_descriptor = __builtin__.property(_get_srgb_descriptor)


  _pyangbind_elements = OrderedDict([('srgb_descriptor', srgb_descriptor), ])



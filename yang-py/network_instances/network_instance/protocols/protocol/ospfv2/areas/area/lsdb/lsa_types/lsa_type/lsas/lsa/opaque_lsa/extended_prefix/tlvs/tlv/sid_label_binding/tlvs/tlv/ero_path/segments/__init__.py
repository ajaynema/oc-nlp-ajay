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

from . import segment
class segments(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path/segments. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__segment',)

  _yang_name = 'segments'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__segment = YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'ero-path', 'segments']

  def _get_segment(self):
    """
    Getter method for segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment (list)

    YANG Description: A segment of the path described within the sub-TLV
    """
    return self.__segment
      
  def _set_segment(self, v, load=False):
    """
    Setter method for segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segment() directly.

    YANG Description: A segment of the path described within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segment must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__segment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segment(self):
    self.__segment = YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  segment = __builtin__.property(_get_segment)


  _pyangbind_elements = OrderedDict([('segment', segment), ])


from . import segment
class segments(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/extended-prefix/tlvs/tlv/sid-label-binding/tlvs/tlv/ero-path/segments. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Segments of the path described within the SID/Label
Binding sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__segment',)

  _yang_name = 'segments'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__segment = YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'areas', 'area', 'lsdb', 'lsa-types', 'lsa-type', 'lsas', 'lsa', 'opaque-lsa', 'extended-prefix', 'tlvs', 'tlv', 'sid-label-binding', 'tlvs', 'tlv', 'ero-path', 'segments']

  def _get_segment(self):
    """
    Getter method for segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment (list)

    YANG Description: A segment of the path described within the sub-TLV
    """
    return self.__segment
      
  def _set_segment(self, v, load=False):
    """
    Setter method for segment, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/extended_prefix/tlvs/tlv/sid_label_binding/tlvs/tlv/ero_path/segments/segment (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_segment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_segment() directly.

    YANG Description: A segment of the path described within the sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """segment must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__segment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_segment(self):
    self.__segment = YANGDynClass(base=YANGListType(False,segment.segment, yang_name="segment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="segment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  segment = __builtin__.property(_get_segment)


  _pyangbind_elements = OrderedDict([('segment', segment), ])


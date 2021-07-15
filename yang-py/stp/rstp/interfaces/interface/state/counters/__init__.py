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

class counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-spanning-tree - based on the path /stp/rstp/interfaces/interface/state/counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The BPDU packet transmition statistics
  """
  __slots__ = ('_path_helper', '_extmethods', '__bpdu_sent','__bpdu_received',)

  _yang_name = 'counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bpdu_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)
    self.__bpdu_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)

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
      return ['stp', 'rstp', 'interfaces', 'interface', 'state', 'counters']

  def _get_bpdu_sent(self):
    """
    Getter method for bpdu_sent, mapped from YANG variable /stp/rstp/interfaces/interface/state/counters/bpdu_sent (oc-yang:counter64)

    YANG Description: The number of BPDU packet sent
    """
    return self.__bpdu_sent
      
  def _set_bpdu_sent(self, v, load=False):
    """
    Setter method for bpdu_sent, mapped from YANG variable /stp/rstp/interfaces/interface/state/counters/bpdu_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_sent() directly.

    YANG Description: The number of BPDU packet sent
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__bpdu_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_sent(self):
    self.__bpdu_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)


  def _get_bpdu_received(self):
    """
    Getter method for bpdu_received, mapped from YANG variable /stp/rstp/interfaces/interface/state/counters/bpdu_received (oc-yang:counter64)

    YANG Description: The number of BPDU packet received
    """
    return self.__bpdu_received
      
  def _set_bpdu_received(self, v, load=False):
    """
    Setter method for bpdu_received, mapped from YANG variable /stp/rstp/interfaces/interface/state/counters/bpdu_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_received() directly.

    YANG Description: The number of BPDU packet received
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__bpdu_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_received(self):
    self.__bpdu_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="bpdu-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-yang:counter64', is_config=False)

  bpdu_sent = __builtin__.property(_get_bpdu_sent)
  bpdu_received = __builtin__.property(_get_bpdu_received)


  _pyangbind_elements = OrderedDict([('bpdu_sent', bpdu_sent), ('bpdu_received', bpdu_received), ])



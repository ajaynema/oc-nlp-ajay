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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/aggregation/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state variables for logical
aggregate / LAG interfaces
  """
  __slots__ = ('_path_helper', '_extmethods', '__lag_type','__min_links','__lag_speed','__member',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lag_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'LACP': {}, 'STATIC': {}},), is_leaf=True, yang_name="lag-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='aggregation-type', is_config=False)
    self.__min_links = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="min-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint16', is_config=False)
    self.__lag_speed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint32', is_config=False)
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='oc-if:base-interface-ref', is_config=False)

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
      return ['interfaces', 'interface', 'aggregation', 'state']

  def _get_lag_type(self):
    """
    Getter method for lag_type, mapped from YANG variable /interfaces/interface/aggregation/state/lag_type (aggregation-type)

    YANG Description: Sets the type of LAG, i.e., how it is
configured / maintained
    """
    return self.__lag_type
      
  def _set_lag_type(self, v, load=False):
    """
    Setter method for lag_type, mapped from YANG variable /interfaces/interface/aggregation/state/lag_type (aggregation-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lag_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lag_type() directly.

    YANG Description: Sets the type of LAG, i.e., how it is
configured / maintained
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'LACP': {}, 'STATIC': {}},), is_leaf=True, yang_name="lag-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='aggregation-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lag_type must be of a type compatible with aggregation-type""",
          'defined-type': "openconfig-if-aggregate:aggregation-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'LACP': {}, 'STATIC': {}},), is_leaf=True, yang_name="lag-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='aggregation-type', is_config=False)""",
        })

    self.__lag_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lag_type(self):
    self.__lag_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'LACP': {}, 'STATIC': {}},), is_leaf=True, yang_name="lag-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='aggregation-type', is_config=False)


  def _get_min_links(self):
    """
    Getter method for min_links, mapped from YANG variable /interfaces/interface/aggregation/state/min_links (uint16)

    YANG Description: Specifies the mininum number of member
interfaces that must be active for the aggregate interface
to be available
    """
    return self.__min_links
      
  def _set_min_links(self, v, load=False):
    """
    Setter method for min_links, mapped from YANG variable /interfaces/interface/aggregation/state/min_links (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_links is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_links() directly.

    YANG Description: Specifies the mininum number of member
interfaces that must be active for the aggregate interface
to be available
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="min-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_links must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="min-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint16', is_config=False)""",
        })

    self.__min_links = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_links(self):
    self.__min_links = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="min-links", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint16', is_config=False)


  def _get_lag_speed(self):
    """
    Getter method for lag_speed, mapped from YANG variable /interfaces/interface/aggregation/state/lag_speed (uint32)

    YANG Description: Reports effective speed of the aggregate interface,
based on speed of active member interfaces
    """
    return self.__lag_speed
      
  def _set_lag_speed(self, v, load=False):
    """
    Setter method for lag_speed, mapped from YANG variable /interfaces/interface/aggregation/state/lag_speed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lag_speed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lag_speed() directly.

    YANG Description: Reports effective speed of the aggregate interface,
based on speed of active member interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lag_speed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint32', is_config=False)""",
        })

    self.__lag_speed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lag_speed(self):
    self.__lag_speed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="lag-speed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='uint32', is_config=False)


  def _get_member(self):
    """
    Getter method for member, mapped from YANG variable /interfaces/interface/aggregation/state/member (oc-if:base-interface-ref)

    YANG Description: List of current member interfaces for the aggregate,
expressed as references to existing interfaces
    """
    return self.__member
      
  def _set_member(self, v, load=False):
    """
    Setter method for member, mapped from YANG variable /interfaces/interface/aggregation/state/member (oc-if:base-interface-ref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member() directly.

    YANG Description: List of current member interfaces for the aggregate,
expressed as references to existing interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='oc-if:base-interface-ref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member must be of a type compatible with oc-if:base-interface-ref""",
          'defined-type': "oc-if:base-interface-ref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='oc-if:base-interface-ref', is_config=False)""",
        })

    self.__member = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member(self):
    self.__member = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="member", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/aggregate', defining_module='openconfig-if-aggregate', yang_type='oc-if:base-interface-ref', is_config=False)

  lag_type = __builtin__.property(_get_lag_type)
  min_links = __builtin__.property(_get_min_links)
  lag_speed = __builtin__.property(_get_lag_speed)
  member = __builtin__.property(_get_member)


  _pyangbind_elements = OrderedDict([('lag_type', lag_type), ('min_links', min_links), ('lag_speed', lag_speed), ('member', member), ])



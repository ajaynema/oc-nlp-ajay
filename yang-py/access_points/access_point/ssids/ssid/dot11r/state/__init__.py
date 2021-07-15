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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/dot11r/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for 802.11r state elements.
  """
  __slots__ = ('_path_helper', '_extmethods', '__dot11r','__dot11r_domainid','__dot11r_method','__dot11r_r1key_timeout',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__dot11r = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11r", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    self.__dot11r_domainid = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-domainid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    self.__dot11r_method = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OVA': {}, 'ODS': {}},), default=six.text_type("OVA"), is_leaf=True, yang_name="dot11r-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)
    self.__dot11r_r1key_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-r1key-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'dot11r', 'state']

  def _get_dot11r(self):
    """
    Getter method for dot11r, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r (boolean)

    YANG Description: Enable/disable 802.11r FT.
    """
    return self.__dot11r
      
  def _set_dot11r(self, v, load=False):
    """
    Setter method for dot11r, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11r is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11r() directly.

    YANG Description: Enable/disable 802.11r FT.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot11r", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11r must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11r", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)""",
        })

    self.__dot11r = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11r(self):
    self.__dot11r = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot11r", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='boolean', is_config=False)


  def _get_dot11r_domainid(self):
    """
    Getter method for dot11r_domainid, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_domainid (uint16)

    YANG Description: Specify the mobility domain id (MDID) where PMK-R0
distribution will occur. Specifically, which APs will recieve
PMK-R0 if using 802.11r (FT).
    """
    return self.__dot11r_domainid
      
  def _set_dot11r_domainid(self, v, load=False):
    """
    Setter method for dot11r_domainid, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_domainid (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11r_domainid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11r_domainid() directly.

    YANG Description: Specify the mobility domain id (MDID) where PMK-R0
distribution will occur. Specifically, which APs will recieve
PMK-R0 if using 802.11r (FT).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-domainid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11r_domainid must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-domainid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__dot11r_domainid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11r_domainid(self):
    self.__dot11r_domainid = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-domainid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)


  def _get_dot11r_method(self):
    """
    Getter method for dot11r_method, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_method (enumeration)

    YANG Description: The type of 802.11r FT in use.
    """
    return self.__dot11r_method
      
  def _set_dot11r_method(self, v, load=False):
    """
    Setter method for dot11r_method, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_method (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11r_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11r_method() directly.

    YANG Description: The type of 802.11r FT in use.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OVA': {}, 'ODS': {}},), default=six.text_type("OVA"), is_leaf=True, yang_name="dot11r-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11r_method must be of a type compatible with enumeration""",
          'defined-type': "openconfig-access-points:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OVA': {}, 'ODS': {}},), default=six.text_type("OVA"), is_leaf=True, yang_name="dot11r-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)""",
        })

    self.__dot11r_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11r_method(self):
    self.__dot11r_method = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'OVA': {}, 'ODS': {}},), default=six.text_type("OVA"), is_leaf=True, yang_name="dot11r-method", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=False)


  def _get_dot11r_r1key_timeout(self):
    """
    Getter method for dot11r_r1key_timeout, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_r1key_timeout (uint16)

    YANG Description: TTL for the Pairwise Master Key R1.
    """
    return self.__dot11r_r1key_timeout
      
  def _set_dot11r_r1key_timeout(self, v, load=False):
    """
    Setter method for dot11r_r1key_timeout, mapped from YANG variable /access_points/access_point/ssids/ssid/dot11r/state/dot11r_r1key_timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot11r_r1key_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot11r_r1key_timeout() directly.

    YANG Description: TTL for the Pairwise Master Key R1.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-r1key-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot11r_r1key_timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-r1key-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__dot11r_r1key_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot11r_r1key_timeout(self):
    self.__dot11r_r1key_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="dot11r-r1key-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)

  dot11r = __builtin__.property(_get_dot11r)
  dot11r_domainid = __builtin__.property(_get_dot11r_domainid)
  dot11r_method = __builtin__.property(_get_dot11r_method)
  dot11r_r1key_timeout = __builtin__.property(_get_dot11r_r1key_timeout)


  _pyangbind_elements = OrderedDict([('dot11r', dot11r), ('dot11r_domainid', dot11r_domainid), ('dot11r_method', dot11r_method), ('dot11r_r1key_timeout', dot11r_r1key_timeout), ])



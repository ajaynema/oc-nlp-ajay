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

from . import bssid
class bssids(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/ssids/ssid/bssids. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for BSSIDs operational state data.
  """
  __slots__ = ('_path_helper', '_extmethods', '__bssid',)

  _yang_name = 'bssids'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bssid = YANGDynClass(base=YANGListType("radio_id bssid",bssid.bssid, yang_name="bssid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='radio-id bssid', extensions=None), is_container='list', yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=True)

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
      return ['access-points', 'access-point', 'ssids', 'ssid', 'bssids']

  def _get_bssid(self):
    """
    Getter method for bssid, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid (list)

    YANG Description: List of BSSIDs and what radio-id they utilize. Radio-id
included here to allocate for APs with dual 5GHz radios.
Usage of paths allows for discovery and subscription of
State data per BSSID, regardless of radio.
    """
    return self.__bssid
      
  def _set_bssid(self, v, load=False):
    """
    Setter method for bssid, mapped from YANG variable /access_points/access_point/ssids/ssid/bssids/bssid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bssid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bssid() directly.

    YANG Description: List of BSSIDs and what radio-id they utilize. Radio-id
included here to allocate for APs with dual 5GHz radios.
Usage of paths allows for discovery and subscription of
State data per BSSID, regardless of radio.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("radio_id bssid",bssid.bssid, yang_name="bssid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='radio-id bssid', extensions=None), is_container='list', yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bssid must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("radio_id bssid",bssid.bssid, yang_name="bssid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='radio-id bssid', extensions=None), is_container='list', yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=True)""",
        })

    self.__bssid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bssid(self):
    self.__bssid = YANGDynClass(base=YANGListType("radio_id bssid",bssid.bssid, yang_name="bssid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='radio-id bssid', extensions=None), is_container='list', yang_name="bssid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='list', is_config=True)

  bssid = __builtin__.property(_get_bssid, _set_bssid)


  _pyangbind_elements = OrderedDict([('bssid', bssid), ])


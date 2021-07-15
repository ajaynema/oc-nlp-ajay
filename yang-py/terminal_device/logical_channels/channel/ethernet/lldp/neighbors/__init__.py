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

from . import neighbor
class neighbors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/ethernet/lldp/neighbors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for list of LLDP neighbors on
a logical channel
  """
  __slots__ = ('_path_helper', '_extmethods', '__neighbor',)

  _yang_name = 'neighbors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbor = YANGDynClass(base=YANGListType("id",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=False)

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
      return ['terminal-device', 'logical-channels', 'channel', 'ethernet', 'lldp', 'neighbors']

  def _get_neighbor(self):
    """
    Getter method for neighbor, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor (list)

    YANG Description: List of LLDP neighbors. If the implementation only
supports one neighbor, this would always be a list with
one item. If the device and neighbor supported multiple
neighbors, which can be achieved via LLDP forwarding, then
this would be supported
    """
    return self.__neighbor
      
  def _set_neighbor(self, v, load=False):
    """
    Setter method for neighbor, mapped from YANG variable /terminal_device/logical_channels/channel/ethernet/lldp/neighbors/neighbor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor() directly.

    YANG Description: List of LLDP neighbors. If the implementation only
supports one neighbor, this would always be a list with
one item. If the device and neighbor supported multiple
neighbors, which can be achieved via LLDP forwarding, then
this would be supported
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("id",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("id",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=False)""",
        })

    self.__neighbor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor(self):
    self.__neighbor = YANGDynClass(base=YANGListType("id",neighbor.neighbor, yang_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='id', extensions=None), is_container='list', yang_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=False)

  neighbor = __builtin__.property(_get_neighbor)


  _pyangbind_elements = OrderedDict([('neighbor', neighbor), ])



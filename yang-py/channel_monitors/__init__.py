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

from . import channel_monitor
class channel_monitors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-channel-monitor - based on the path /channel-monitors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for optical channel monitors
  """
  __slots__ = ('_path_helper', '_extmethods', '__channel_monitor',)

  _yang_name = 'channel-monitors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__channel_monitor = YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)

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
      return ['channel-monitors']

  def _get_channel_monitor(self):
    """
    Getter method for channel_monitor, mapped from YANG variable /channel_monitors/channel_monitor (list)

    YANG Description: List of channel monitors, keyed by channel monitor name.
    """
    return self.__channel_monitor
      
  def _set_channel_monitor(self, v, load=False):
    """
    Setter method for channel_monitor, mapped from YANG variable /channel_monitors/channel_monitor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_channel_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_channel_monitor() directly.

    YANG Description: List of channel monitors, keyed by channel monitor name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """channel_monitor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)""",
        })

    self.__channel_monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_channel_monitor(self):
    self.__channel_monitor = YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)

  channel_monitor = __builtin__.property(_get_channel_monitor, _set_channel_monitor)


  _pyangbind_elements = OrderedDict([('channel_monitor', channel_monitor), ])


from . import channel_monitor
class channel_monitors(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-channel-monitor - based on the path /channel-monitors. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for optical channel monitors
  """
  __slots__ = ('_path_helper', '_extmethods', '__channel_monitor',)

  _yang_name = 'channel-monitors'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__channel_monitor = YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)

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
      return ['channel-monitors']

  def _get_channel_monitor(self):
    """
    Getter method for channel_monitor, mapped from YANG variable /channel_monitors/channel_monitor (list)

    YANG Description: List of channel monitors, keyed by channel monitor name.
    """
    return self.__channel_monitor
      
  def _set_channel_monitor(self, v, load=False):
    """
    Setter method for channel_monitor, mapped from YANG variable /channel_monitors/channel_monitor (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_channel_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_channel_monitor() directly.

    YANG Description: List of channel monitors, keyed by channel monitor name.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """channel_monitor must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)""",
        })

    self.__channel_monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_channel_monitor(self):
    self.__channel_monitor = YANGDynClass(base=YANGListType("name",channel_monitor.channel_monitor, yang_name="channel-monitor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="channel-monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/channel-monitor', defining_module='openconfig-channel-monitor', yang_type='list', is_config=True)

  channel_monitor = __builtin__.property(_get_channel_monitor, _set_channel_monitor)


  _pyangbind_elements = OrderedDict([('channel_monitor', channel_monitor), ])



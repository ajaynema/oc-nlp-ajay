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

from . import amplifiers
from . import supervisory_channels
class optical_amplifier(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-optical-amplifier - based on the path /optical-amplifier. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for amplifiers and supervisory channels
  """
  __slots__ = ('_path_helper', '_extmethods', '__amplifiers','__supervisory_channels',)

  _yang_name = 'optical-amplifier'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__amplifiers = YANGDynClass(base=amplifiers.amplifiers, is_container='container', yang_name="amplifiers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)
    self.__supervisory_channels = YANGDynClass(base=supervisory_channels.supervisory_channels, is_container='container', yang_name="supervisory-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)

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
      return ['optical-amplifier']

  def _get_amplifiers(self):
    """
    Getter method for amplifiers, mapped from YANG variable /optical_amplifier/amplifiers (container)

    YANG Description: Enclosing container for list of amplifiers
    """
    return self.__amplifiers
      
  def _set_amplifiers(self, v, load=False):
    """
    Setter method for amplifiers, mapped from YANG variable /optical_amplifier/amplifiers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_amplifiers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_amplifiers() directly.

    YANG Description: Enclosing container for list of amplifiers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=amplifiers.amplifiers, is_container='container', yang_name="amplifiers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """amplifiers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=amplifiers.amplifiers, is_container='container', yang_name="amplifiers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)""",
        })

    self.__amplifiers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_amplifiers(self):
    self.__amplifiers = YANGDynClass(base=amplifiers.amplifiers, is_container='container', yang_name="amplifiers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)


  def _get_supervisory_channels(self):
    """
    Getter method for supervisory_channels, mapped from YANG variable /optical_amplifier/supervisory_channels (container)

    YANG Description: Enclosing container for list of supervisory channels
    """
    return self.__supervisory_channels
      
  def _set_supervisory_channels(self, v, load=False):
    """
    Setter method for supervisory_channels, mapped from YANG variable /optical_amplifier/supervisory_channels (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_supervisory_channels is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_supervisory_channels() directly.

    YANG Description: Enclosing container for list of supervisory channels
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=supervisory_channels.supervisory_channels, is_container='container', yang_name="supervisory-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """supervisory_channels must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=supervisory_channels.supervisory_channels, is_container='container', yang_name="supervisory-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)""",
        })

    self.__supervisory_channels = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_supervisory_channels(self):
    self.__supervisory_channels = YANGDynClass(base=supervisory_channels.supervisory_channels, is_container='container', yang_name="supervisory-channels", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/optical-amplfier', defining_module='openconfig-optical-amplifier', yang_type='container', is_config=True)

  amplifiers = __builtin__.property(_get_amplifiers, _set_amplifiers)
  supervisory_channels = __builtin__.property(_get_supervisory_channels, _set_supervisory_channels)


  _pyangbind_elements = OrderedDict([('amplifiers', amplifiers), ('supervisory_channels', supervisory_channels), ])



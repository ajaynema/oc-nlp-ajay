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

from . import persistent_subscriptions
from . import dynamic_subscriptions
class subscriptions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-telemetry - based on the path /telemetry-system/subscriptions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container holds information for both persistent
and dynamic telemetry subscriptions.
  """
  __slots__ = ('_path_helper', '_extmethods', '__persistent_subscriptions','__dynamic_subscriptions',)

  _yang_name = 'subscriptions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__persistent_subscriptions = YANGDynClass(base=persistent_subscriptions.persistent_subscriptions, is_container='container', yang_name="persistent-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    self.__dynamic_subscriptions = YANGDynClass(base=dynamic_subscriptions.dynamic_subscriptions, is_container='container', yang_name="dynamic-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

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
      return ['telemetry-system', 'subscriptions']

  def _get_persistent_subscriptions(self):
    """
    Getter method for persistent_subscriptions, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions (container)

    YANG Description: This container holds information relating to persistent
telemetry subscriptions. A persistent telemetry
subscription is configued locally on the device through
configuration, and is persistent across device restarts or
other redundancy changes.
    """
    return self.__persistent_subscriptions
      
  def _set_persistent_subscriptions(self, v, load=False):
    """
    Setter method for persistent_subscriptions, mapped from YANG variable /telemetry_system/subscriptions/persistent_subscriptions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_persistent_subscriptions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_persistent_subscriptions() directly.

    YANG Description: This container holds information relating to persistent
telemetry subscriptions. A persistent telemetry
subscription is configued locally on the device through
configuration, and is persistent across device restarts or
other redundancy changes.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=persistent_subscriptions.persistent_subscriptions, is_container='container', yang_name="persistent-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """persistent_subscriptions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=persistent_subscriptions.persistent_subscriptions, is_container='container', yang_name="persistent-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__persistent_subscriptions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_persistent_subscriptions(self):
    self.__persistent_subscriptions = YANGDynClass(base=persistent_subscriptions.persistent_subscriptions, is_container='container', yang_name="persistent-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)


  def _get_dynamic_subscriptions(self):
    """
    Getter method for dynamic_subscriptions, mapped from YANG variable /telemetry_system/subscriptions/dynamic_subscriptions (container)

    YANG Description: This container holds information relating to dynamic
telemetry subscriptions. A dynamic subscription is
typically configured through an RPC channel, and does not
persist across device restarts, or if the RPC channel is
reset or otherwise torn down.
    """
    return self.__dynamic_subscriptions
      
  def _set_dynamic_subscriptions(self, v, load=False):
    """
    Setter method for dynamic_subscriptions, mapped from YANG variable /telemetry_system/subscriptions/dynamic_subscriptions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dynamic_subscriptions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dynamic_subscriptions() directly.

    YANG Description: This container holds information relating to dynamic
telemetry subscriptions. A dynamic subscription is
typically configured through an RPC channel, and does not
persist across device restarts, or if the RPC channel is
reset or otherwise torn down.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=dynamic_subscriptions.dynamic_subscriptions, is_container='container', yang_name="dynamic-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dynamic_subscriptions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dynamic_subscriptions.dynamic_subscriptions, is_container='container', yang_name="dynamic-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)""",
        })

    self.__dynamic_subscriptions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dynamic_subscriptions(self):
    self.__dynamic_subscriptions = YANGDynClass(base=dynamic_subscriptions.dynamic_subscriptions, is_container='container', yang_name="dynamic-subscriptions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/telemetry', defining_module='openconfig-telemetry', yang_type='container', is_config=True)

  persistent_subscriptions = __builtin__.property(_get_persistent_subscriptions, _set_persistent_subscriptions)
  dynamic_subscriptions = __builtin__.property(_get_dynamic_subscriptions, _set_dynamic_subscriptions)


  _pyangbind_elements = OrderedDict([('persistent_subscriptions', persistent_subscriptions), ('dynamic_subscriptions', dynamic_subscriptions), ])



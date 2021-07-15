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

class wait(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/cpus/cpu/state/wait. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Percentage of CPU time spent waiting for I/O.
  """
  __slots__ = ('_path_helper', '_extmethods', '__instant','__avg','__min_','__max_','__interval','__min_time','__max_time',)

  _yang_name = 'wait'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__instant = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__avg = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__min_ = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__max_ = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:stat-interval', is_config=False)
    self.__min_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="min-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    self.__max_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)

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
      return ['system', 'cpus', 'cpu', 'state', 'wait']

  def _get_instant(self):
    """
    Getter method for instant, mapped from YANG variable /system/cpus/cpu/state/wait/instant (oc-types:percentage)

    YANG Description: The instantaneous percentage value.
    """
    return self.__instant
      
  def _set_instant(self, v, load=False):
    """
    Setter method for instant, mapped from YANG variable /system/cpus/cpu/state/wait/instant (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instant is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instant() directly.

    YANG Description: The instantaneous percentage value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instant must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__instant = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instant(self):
    self.__instant = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="instant", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)


  def _get_avg(self):
    """
    Getter method for avg, mapped from YANG variable /system/cpus/cpu/state/wait/avg (oc-types:percentage)

    YANG Description: The arithmetic mean value of the percentage measure of the
statistic over the time interval.
    """
    return self.__avg
      
  def _set_avg(self, v, load=False):
    """
    Setter method for avg, mapped from YANG variable /system/cpus/cpu/state/wait/avg (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_avg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_avg() directly.

    YANG Description: The arithmetic mean value of the percentage measure of the
statistic over the time interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """avg must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__avg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_avg(self):
    self.__avg = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="avg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)


  def _get_min_(self):
    """
    Getter method for min_, mapped from YANG variable /system/cpus/cpu/state/wait/min (oc-types:percentage)

    YANG Description: The minimum value of the percentage measure of the
statistic over the time interval.
    """
    return self.__min_
      
  def _set_min_(self, v, load=False):
    """
    Setter method for min_, mapped from YANG variable /system/cpus/cpu/state/wait/min (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_() directly.

    YANG Description: The minimum value of the percentage measure of the
statistic over the time interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_ must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__min_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_(self):
    self.__min_ = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="min", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)


  def _get_max_(self):
    """
    Getter method for max_, mapped from YANG variable /system/cpus/cpu/state/wait/max (oc-types:percentage)

    YANG Description: The maximum value of the percentage measure of the
statistic over the time interval.
    """
    return self.__max_
      
  def _set_max_(self, v, load=False):
    """
    Setter method for max_, mapped from YANG variable /system/cpus/cpu/state/wait/max (oc-types:percentage)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_() directly.

    YANG Description: The maximum value of the percentage measure of the
statistic over the time interval.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_ must be of a type compatible with oc-types:percentage""",
          'defined-type': "oc-types:percentage",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)""",
        })

    self.__max_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_(self):
    self.__max_ = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..100']}), is_leaf=True, yang_name="max", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:percentage', is_config=False)


  def _get_interval(self):
    """
    Getter method for interval, mapped from YANG variable /system/cpus/cpu/state/wait/interval (oc-types:stat-interval)

    YANG Description: If supported by the system, this reports the time interval
over which the min/max/average statistics are computed by
the system.
    """
    return self.__interval
      
  def _set_interval(self, v, load=False):
    """
    Setter method for interval, mapped from YANG variable /system/cpus/cpu/state/wait/interval (oc-types:stat-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interval() directly.

    YANG Description: If supported by the system, this reports the time interval
over which the min/max/average statistics are computed by
the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:stat-interval', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interval must be of a type compatible with oc-types:stat-interval""",
          'defined-type': "oc-types:stat-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:stat-interval', is_config=False)""",
        })

    self.__interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interval(self):
    self.__interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:stat-interval', is_config=False)


  def _get_min_time(self):
    """
    Getter method for min_time, mapped from YANG variable /system/cpus/cpu/state/wait/min_time (oc-types:timeticks64)

    YANG Description: The absolute time at which the minimum value occurred.
The value is the timestamp in nanoseconds relative to
 the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    return self.__min_time
      
  def _set_min_time(self, v, load=False):
    """
    Setter method for min_time, mapped from YANG variable /system/cpus/cpu/state/wait/min_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_time() directly.

    YANG Description: The absolute time at which the minimum value occurred.
The value is the timestamp in nanoseconds relative to
 the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="min-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="min-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__min_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_time(self):
    self.__min_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="min-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)


  def _get_max_time(self):
    """
    Getter method for max_time, mapped from YANG variable /system/cpus/cpu/state/wait/max_time (oc-types:timeticks64)

    YANG Description: The absolute time at which the maximum value occurred.
The value is the timestamp in nanoseconds relative to
 the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    return self.__max_time
      
  def _set_max_time(self, v, load=False):
    """
    Setter method for max_time, mapped from YANG variable /system/cpus/cpu/state/wait/max_time (oc-types:timeticks64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_time() directly.

    YANG Description: The absolute time at which the maximum value occurred.
The value is the timestamp in nanoseconds relative to
 the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_time must be of a type compatible with oc-types:timeticks64""",
          'defined-type': "oc-types:timeticks64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)""",
        })

    self.__max_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_time(self):
    self.__max_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="max-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='oc-types:timeticks64', is_config=False)

  instant = __builtin__.property(_get_instant)
  avg = __builtin__.property(_get_avg)
  min_ = __builtin__.property(_get_min_)
  max_ = __builtin__.property(_get_max_)
  interval = __builtin__.property(_get_interval)
  min_time = __builtin__.property(_get_min_time)
  max_time = __builtin__.property(_get_max_time)


  _pyangbind_elements = OrderedDict([('instant', instant), ('avg', avg), ('min_', min_), ('max_', max_), ('interval', interval), ('min_time', min_time), ('max_time', max_time), ])



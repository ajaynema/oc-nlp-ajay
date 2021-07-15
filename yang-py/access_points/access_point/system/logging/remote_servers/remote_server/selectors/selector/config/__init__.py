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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/logging/remote-servers/remote-server/selectors/selector/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__facility','__severity',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__facility = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='syslog-severity', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'logging', 'remote-servers', 'remote-server', 'selectors', 'selector', 'config']

  def _get_facility(self):
    """
    Getter method for facility, mapped from YANG variable /access_points/access_point/system/logging/remote_servers/remote_server/selectors/selector/config/facility (identityref)

    YANG Description: Specifies the facility, or class of messages to log
    """
    return self.__facility
      
  def _set_facility(self, v, load=False):
    """
    Setter method for facility, mapped from YANG variable /access_points/access_point/system/logging/remote_servers/remote_server/selectors/selector/config/facility (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_facility is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_facility() directly.

    YANG Description: Specifies the facility, or class of messages to log
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """facility must be of a type compatible with identityref""",
          'defined-type': "openconfig-access-points:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)""",
        })

    self.__facility = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_facility(self):
    self.__facility = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:ALL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:KERNEL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:USER': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:MAIL': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSTEM_DAEMON': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTH': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:SYSLOG': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUTHPRIV': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:NTP': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:AUDIT': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:CONSOLE': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL0': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL1': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL2': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL3': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL4': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL5': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL6': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}, 'oc-log:LOCAL7': {'@module': 'openconfig-system-logging', '@namespace': 'http://openconfig.net/yang/system/logging'}},), is_leaf=True, yang_name="facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)


  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /access_points/access_point/system/logging/remote_servers/remote_server/selectors/selector/config/severity (syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) for the corresonding facility are logged
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /access_points/access_point/system/logging/remote_servers/remote_server/selectors/selector/config/severity (syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) for the corresonding facility are logged
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='syslog-severity', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with syslog-severity""",
          'defined-type': "openconfig-access-points:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='syslog-severity', is_config=True)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='syslog-severity', is_config=True)

  facility = __builtin__.property(_get_facility, _set_facility)
  severity = __builtin__.property(_get_severity, _set_severity)


  _pyangbind_elements = OrderedDict([('facility', facility), ('severity', severity), ])


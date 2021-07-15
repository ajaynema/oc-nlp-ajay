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

from . import message
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/messages/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for a Syslog messages.
  """
  __slots__ = ('_path_helper', '_extmethods', '__severity','__message',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'messages', 'state']

  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /access_points/access_point/system/messages/state/severity (oc-log:syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /access_points/access_point/system/messages/state/severity (oc-log:syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with oc-log:syslog-severity""",
          'defined-type': "oc-log:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /access_points/access_point/system/messages/state/message (container)

    YANG Description: Syslog messages the client is Subscribing to. This is all
messages currently configured to be sent according to
syslog-severity.
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /access_points/access_point/system/messages/state/message (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.

    YANG Description: Syslog messages the client is Subscribing to. This is all
messages currently configured to be sent according to
syslog-severity.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)

  severity = __builtin__.property(_get_severity)
  message = __builtin__.property(_get_message)


  _pyangbind_elements = OrderedDict([('severity', severity), ('message', message), ])


from . import message
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/messages/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for a Syslog messages.
  """
  __slots__ = ('_path_helper', '_extmethods', '__severity','__message',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'messages', 'state']

  def _get_severity(self):
    """
    Getter method for severity, mapped from YANG variable /access_points/access_point/system/messages/state/severity (oc-log:syslog-severity)

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    return self.__severity
      
  def _set_severity(self, v, load=False):
    """
    Setter method for severity, mapped from YANG variable /access_points/access_point/system/messages/state/severity (oc-log:syslog-severity)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_severity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_severity() directly.

    YANG Description: Specifies that only messages of the given severity (or
greater severity) are sent over the RPC.

This is analogous to differentiating which severity is to be
sent to legacy Syslog servers, as opposed to local buffer or
files.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """severity must be of a type compatible with oc-log:syslog-severity""",
          'defined-type': "oc-log:syslog-severity",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)""",
        })

    self.__severity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_severity(self):
    self.__severity = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'EMERGENCY': {}, 'ALERT': {}, 'CRITICAL': {}, 'ERROR': {}, 'WARNING': {}, 'NOTICE': {}, 'INFORMATIONAL': {}, 'DEBUG': {}},), is_leaf=True, yang_name="severity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-log:syslog-severity', is_config=False)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /access_points/access_point/system/messages/state/message (container)

    YANG Description: Syslog messages the client is Subscribing to. This is all
messages currently configured to be sent according to
syslog-severity.
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /access_points/access_point/system/messages/state/message (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.

    YANG Description: Syslog messages the client is Subscribing to. This is all
messages currently configured to be sent according to
syslog-severity.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='container', is_config=False)

  severity = __builtin__.property(_get_severity)
  message = __builtin__.property(_get_message)


  _pyangbind_elements = OrderedDict([('severity', severity), ('message', message), ])



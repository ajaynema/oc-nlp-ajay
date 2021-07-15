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

class message(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/messages/state/message. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Syslog messages the client is Subscribing to. This is all
messages currently configured to be sent according to
syslog-severity.
  """
  __slots__ = ('_path_helper', '_extmethods', '__msg','__priority','__app_name','__procid','__msgid',)

  _yang_name = 'message'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__msg = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint8', is_config=False)
    self.__app_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="app-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__procid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="procid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    self.__msgid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

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
      return ['system', 'messages', 'state', 'message']

  def _get_msg(self):
    """
    Getter method for msg, mapped from YANG variable /system/messages/state/message/msg (string)

    YANG Description: Message payload. If other leafs within this container not
supported, this leaf MAY include the entire message,
inclding pri, procid, app-name etc..
    """
    return self.__msg
      
  def _set_msg(self, v, load=False):
    """
    Setter method for msg, mapped from YANG variable /system/messages/state/message/msg (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msg() directly.

    YANG Description: Message payload. If other leafs within this container not
supported, this leaf MAY include the entire message,
inclding pri, procid, app-name etc..
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msg must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__msg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msg(self):
    self.__msg = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /system/messages/state/message/priority (uint8)

    YANG Description: The Priority value (PRIVAL) represents both the
Facility and Severity.
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /system/messages/state/message/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: The Priority value (PRIVAL) represents both the
Facility and Severity.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='uint8', is_config=False)


  def _get_app_name(self):
    """
    Getter method for app_name, mapped from YANG variable /system/messages/state/message/app_name (string)

    YANG Description: The APP-NAME field SHOULD identify the device or
application that originated the message.
    """
    return self.__app_name
      
  def _set_app_name(self, v, load=False):
    """
    Setter method for app_name, mapped from YANG variable /system/messages/state/message/app_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_app_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_app_name() directly.

    YANG Description: The APP-NAME field SHOULD identify the device or
application that originated the message.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="app-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """app_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="app-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__app_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_app_name(self):
    self.__app_name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="app-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_procid(self):
    """
    Getter method for procid, mapped from YANG variable /system/messages/state/message/procid (string)

    YANG Description: PROCID is a value that is included in the message, having
no interoperable meaning, except that a change in the value
indicates there has been a discontinuity in syslog
reporting.
    """
    return self.__procid
      
  def _set_procid(self, v, load=False):
    """
    Setter method for procid, mapped from YANG variable /system/messages/state/message/procid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_procid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_procid() directly.

    YANG Description: PROCID is a value that is included in the message, having
no interoperable meaning, except that a change in the value
indicates there has been a discontinuity in syslog
reporting.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="procid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """procid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="procid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__procid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_procid(self):
    self.__procid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="procid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)


  def _get_msgid(self):
    """
    Getter method for msgid, mapped from YANG variable /system/messages/state/message/msgid (string)

    YANG Description: The MSGID SHOULD identify the type of message. For
example, a firewall might use the MSGID 'TCPIN' for
incoming TCP traffic and the MSGID 'TCPOUT' for outgoing
TCP traffic.
    """
    return self.__msgid
      
  def _set_msgid(self, v, load=False):
    """
    Setter method for msgid, mapped from YANG variable /system/messages/state/message/msgid (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msgid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msgid() directly.

    YANG Description: The MSGID SHOULD identify the type of message. For
example, a firewall might use the MSGID 'TCPIN' for
incoming TCP traffic and the MSGID 'TCPOUT' for outgoing
TCP traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="msgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msgid must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)""",
        })

    self.__msgid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msgid(self):
    self.__msgid = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="msgid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='string', is_config=False)

  msg = __builtin__.property(_get_msg)
  priority = __builtin__.property(_get_priority)
  app_name = __builtin__.property(_get_app_name)
  procid = __builtin__.property(_get_procid)
  msgid = __builtin__.property(_get_msgid)


  _pyangbind_elements = OrderedDict([('msg', msg), ('priority', priority), ('app_name', app_name), ('procid', procid), ('msgid', msgid), ])



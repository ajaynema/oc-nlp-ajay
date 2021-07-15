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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/server-groups/server-group/servers/server/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__address','__timeout','__connection_opens','__connection_closes','__connection_aborts','__connection_failures','__connection_timeouts','__messages_sent','__messages_received','__errors_received',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=False)
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    self.__connection_opens = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-opens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__connection_closes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-closes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__connection_aborts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-aborts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__connection_failures = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__connection_timeouts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-timeouts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__messages_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__messages_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    self.__errors_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="errors-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'server-groups', 'server-group', 'servers', 'server', 'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/name (string)

    YANG Description: Name assigned to the server
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name assigned to the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='string', is_config=False)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/address (oc-inet:ip-address)

    YANG Description: Address of the authentication server
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: Address of the authentication server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=False)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-inet:ip-address', is_config=False)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/timeout (uint16)

    YANG Description: Set the timeout in seconds on responses from the AAA
server
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.

    YANG Description: Set the timeout in seconds on responses from the AAA
server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='uint16', is_config=False)


  def _get_connection_opens(self):
    """
    Getter method for connection_opens, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_opens (oc-yang:counter64)

    YANG Description: Number of new connection requests sent to the server, e.g.
socket open
    """
    return self.__connection_opens
      
  def _set_connection_opens(self, v, load=False):
    """
    Setter method for connection_opens, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_opens (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_opens is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_opens() directly.

    YANG Description: Number of new connection requests sent to the server, e.g.
socket open
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-opens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_opens must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-opens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__connection_opens = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_opens(self):
    self.__connection_opens = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-opens", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_connection_closes(self):
    """
    Getter method for connection_closes, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_closes (oc-yang:counter64)

    YANG Description: Number of connection close requests sent to the server, e.g.
socket close
    """
    return self.__connection_closes
      
  def _set_connection_closes(self, v, load=False):
    """
    Setter method for connection_closes, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_closes (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_closes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_closes() directly.

    YANG Description: Number of connection close requests sent to the server, e.g.
socket close
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-closes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_closes must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-closes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__connection_closes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_closes(self):
    self.__connection_closes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-closes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_connection_aborts(self):
    """
    Getter method for connection_aborts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_aborts (oc-yang:counter64)

    YANG Description: Number of aborted connections to the server.  These do
not include connections that are close gracefully.
    """
    return self.__connection_aborts
      
  def _set_connection_aborts(self, v, load=False):
    """
    Setter method for connection_aborts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_aborts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_aborts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_aborts() directly.

    YANG Description: Number of aborted connections to the server.  These do
not include connections that are close gracefully.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-aborts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_aborts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-aborts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__connection_aborts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_aborts(self):
    self.__connection_aborts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-aborts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_connection_failures(self):
    """
    Getter method for connection_failures, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_failures (oc-yang:counter64)

    YANG Description: Number of connection failures to the server
    """
    return self.__connection_failures
      
  def _set_connection_failures(self, v, load=False):
    """
    Setter method for connection_failures, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_failures (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_failures is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_failures() directly.

    YANG Description: Number of connection failures to the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_failures must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__connection_failures = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_failures(self):
    self.__connection_failures = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-failures", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_connection_timeouts(self):
    """
    Getter method for connection_timeouts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_timeouts (oc-yang:counter64)

    YANG Description: Number of connection timeouts to the server
    """
    return self.__connection_timeouts
      
  def _set_connection_timeouts(self, v, load=False):
    """
    Setter method for connection_timeouts, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/connection_timeouts (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_timeouts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_timeouts() directly.

    YANG Description: Number of connection timeouts to the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-timeouts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_timeouts must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-timeouts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__connection_timeouts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_timeouts(self):
    self.__connection_timeouts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="connection-timeouts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_messages_sent(self):
    """
    Getter method for messages_sent, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/messages_sent (oc-yang:counter64)

    YANG Description: Number of messages sent to the server
    """
    return self.__messages_sent
      
  def _set_messages_sent(self, v, load=False):
    """
    Setter method for messages_sent, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/messages_sent (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_messages_sent is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_messages_sent() directly.

    YANG Description: Number of messages sent to the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """messages_sent must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__messages_sent = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_messages_sent(self):
    self.__messages_sent = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-sent", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_messages_received(self):
    """
    Getter method for messages_received, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/messages_received (oc-yang:counter64)

    YANG Description: Number of messages received by the server
    """
    return self.__messages_received
      
  def _set_messages_received(self, v, load=False):
    """
    Setter method for messages_received, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/messages_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_messages_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_messages_received() directly.

    YANG Description: Number of messages received by the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """messages_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__messages_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_messages_received(self):
    self.__messages_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="messages-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)


  def _get_errors_received(self):
    """
    Getter method for errors_received, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/errors_received (oc-yang:counter64)

    YANG Description: Number of error messages received from the server
    """
    return self.__errors_received
      
  def _set_errors_received(self, v, load=False):
    """
    Setter method for errors_received, mapped from YANG variable /access_points/access_point/system/aaa/server_groups/server_group/servers/server/state/errors_received (oc-yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_errors_received is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_errors_received() directly.

    YANG Description: Number of error messages received from the server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="errors-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """errors_received must be of a type compatible with oc-yang:counter64""",
          'defined-type': "oc-yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="errors-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)""",
        })

    self.__errors_received = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_errors_received(self):
    self.__errors_received = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="errors-received", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='oc-yang:counter64', is_config=False)

  name = __builtin__.property(_get_name)
  address = __builtin__.property(_get_address)
  timeout = __builtin__.property(_get_timeout)
  connection_opens = __builtin__.property(_get_connection_opens)
  connection_closes = __builtin__.property(_get_connection_closes)
  connection_aborts = __builtin__.property(_get_connection_aborts)
  connection_failures = __builtin__.property(_get_connection_failures)
  connection_timeouts = __builtin__.property(_get_connection_timeouts)
  messages_sent = __builtin__.property(_get_messages_sent)
  messages_received = __builtin__.property(_get_messages_received)
  errors_received = __builtin__.property(_get_errors_received)


  _pyangbind_elements = OrderedDict([('name', name), ('address', address), ('timeout', timeout), ('connection_opens', connection_opens), ('connection_closes', connection_closes), ('connection_aborts', connection_aborts), ('connection_failures', connection_failures), ('connection_timeouts', connection_timeouts), ('messages_sent', messages_sent), ('messages_received', messages_received), ('errors_received', errors_received), ])



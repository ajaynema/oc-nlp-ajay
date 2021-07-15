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
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcpv6/interfaces/interface/options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for DHCPv6 agent option on an
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable_interface_id','__enable_remote_id','__interface_id','__remote_id','__sent_interface_id','__sent_remote_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable_interface_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__enable_remote_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

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
      return ['relay-agent', 'dhcpv6', 'interfaces', 'interface', 'options', 'state']

  def _get_enable_interface_id(self):
    """
    Getter method for enable_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_interface_id (boolean)

    YANG Description: Enables DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    return self.__enable_interface_id
      
  def _set_enable_interface_id(self, v, load=False):
    """
    Setter method for enable_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_interface_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_interface_id() directly.

    YANG Description: Enables DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_interface_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_interface_id(self):
    self.__enable_interface_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_enable_remote_id(self):
    """
    Getter method for enable_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_remote_id (boolean)

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    return self.__enable_remote_id
      
  def _set_enable_remote_id(self, v, load=False):
    """
    Setter method for enable_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_remote_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_remote_id() directly.

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_remote_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_remote_id(self):
    self.__enable_remote_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/interface_id (string)

    YANG Description: Sets DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Sets DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_remote_id(self):
    """
    Getter method for remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/remote_id (string)

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    return self.__remote_id
      
  def _set_remote_id(self, v, load=False):
    """
    Setter method for remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_id() directly.

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_id(self):
    self.__remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_interface_id(self):
    """
    Getter method for sent_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_interface_id (string)

    YANG Description: Reflects the DHCPv6 OPTION_INTERFACE_ID (18) sent to the
server by the system.
    """
    return self.__sent_interface_id
      
  def _set_sent_interface_id(self, v, load=False):
    """
    Setter method for sent_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_interface_id() directly.

    YANG Description: Reflects the DHCPv6 OPTION_INTERFACE_ID (18) sent to the
server by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_interface_id(self):
    self.__sent_interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_remote_id(self):
    """
    Getter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_remote_id (string)

    YANG Description: Reflects the DHCPv6 OPTION_REMOTE_ID (37) sent to the
server by the system.
    """
    return self.__sent_remote_id
      
  def _set_sent_remote_id(self, v, load=False):
    """
    Setter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_remote_id() directly.

    YANG Description: Reflects the DHCPv6 OPTION_REMOTE_ID (37) sent to the
server by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_remote_id(self):
    self.__sent_remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

  enable_interface_id = __builtin__.property(_get_enable_interface_id)
  enable_remote_id = __builtin__.property(_get_enable_remote_id)
  interface_id = __builtin__.property(_get_interface_id)
  remote_id = __builtin__.property(_get_remote_id)
  sent_interface_id = __builtin__.property(_get_sent_interface_id)
  sent_remote_id = __builtin__.property(_get_sent_remote_id)


  _pyangbind_elements = OrderedDict([('enable_interface_id', enable_interface_id), ('enable_remote_id', enable_remote_id), ('interface_id', interface_id), ('remote_id', remote_id), ('sent_interface_id', sent_interface_id), ('sent_remote_id', sent_remote_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-relay-agent - based on the path /relay-agent/dhcpv6/interfaces/interface/options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for DHCPv6 agent option on an
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__enable_interface_id','__enable_remote_id','__interface_id','__remote_id','__sent_interface_id','__sent_remote_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__enable_interface_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__enable_remote_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    self.__sent_remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

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
      return ['relay-agent', 'dhcpv6', 'interfaces', 'interface', 'options', 'state']

  def _get_enable_interface_id(self):
    """
    Getter method for enable_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_interface_id (boolean)

    YANG Description: Enables DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    return self.__enable_interface_id
      
  def _set_enable_interface_id(self, v, load=False):
    """
    Setter method for enable_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_interface_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_interface_id() directly.

    YANG Description: Enables DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_interface_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_interface_id(self):
    self.__enable_interface_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_enable_remote_id(self):
    """
    Getter method for enable_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_remote_id (boolean)

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    return self.__enable_remote_id
      
  def _set_enable_remote_id(self, v, load=False):
    """
    Setter method for enable_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/enable_remote_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_remote_id() directly.

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_remote_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)""",
        })

    self.__enable_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_remote_id(self):
    self.__enable_remote_id = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='boolean', is_config=False)


  def _get_interface_id(self):
    """
    Getter method for interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/interface_id (string)

    YANG Description: Sets DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    return self.__interface_id
      
  def _set_interface_id(self, v, load=False):
    """
    Setter method for interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Sets DHCPv6 OPTION_INTERFACE_ID (18) to identify the
interface on which the client message was received.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_id(self):
    self.__interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_remote_id(self):
    """
    Getter method for remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/remote_id (string)

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    return self.__remote_id
      
  def _set_remote_id(self, v, load=False):
    """
    Setter method for remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_id() directly.

    YANG Description: Sets DHCPv6 OPTION_REMOTE_ID (37).  This option is the
DHCPv6 equivalent for the IPv4 (DHCPv4) Relay Agent Option's
Remote-ID suboption as specified in RFC 3046. The remote-id
field may be used to encode a user name, remote IP address,
interface/port identifier, etc.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_id(self):
    self.__remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_interface_id(self):
    """
    Getter method for sent_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_interface_id (string)

    YANG Description: Reflects the DHCPv6 OPTION_INTERFACE_ID (18) sent to the
server by the system.
    """
    return self.__sent_interface_id
      
  def _set_sent_interface_id(self, v, load=False):
    """
    Setter method for sent_interface_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_interface_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_interface_id() directly.

    YANG Description: Reflects the DHCPv6 OPTION_INTERFACE_ID (18) sent to the
server by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_interface_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_interface_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_interface_id(self):
    self.__sent_interface_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)


  def _get_sent_remote_id(self):
    """
    Getter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_remote_id (string)

    YANG Description: Reflects the DHCPv6 OPTION_REMOTE_ID (37) sent to the
server by the system.
    """
    return self.__sent_remote_id
      
  def _set_sent_remote_id(self, v, load=False):
    """
    Setter method for sent_remote_id, mapped from YANG variable /relay_agent/dhcpv6/interfaces/interface/options/state/sent_remote_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sent_remote_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sent_remote_id() directly.

    YANG Description: Reflects the DHCPv6 OPTION_REMOTE_ID (37) sent to the
server by the system.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sent_remote_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)""",
        })

    self.__sent_remote_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sent_remote_id(self):
    self.__sent_remote_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="sent-remote-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/relay-agent', defining_module='openconfig-relay-agent', yang_type='string', is_config=False)

  enable_interface_id = __builtin__.property(_get_enable_interface_id)
  enable_remote_id = __builtin__.property(_get_enable_remote_id)
  interface_id = __builtin__.property(_get_interface_id)
  remote_id = __builtin__.property(_get_remote_id)
  sent_interface_id = __builtin__.property(_get_sent_interface_id)
  sent_remote_id = __builtin__.property(_get_sent_remote_id)


  _pyangbind_elements = OrderedDict([('enable_interface_id', enable_interface_id), ('enable_remote_id', enable_remote_id), ('interface_id', interface_id), ('remote_id', remote_id), ('sent_interface_id', sent_interface_id), ('sent_remote_id', sent_remote_id), ])



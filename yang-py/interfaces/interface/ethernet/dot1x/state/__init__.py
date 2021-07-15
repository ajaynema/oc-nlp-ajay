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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/dot1x/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top level state container for 802.1X.
  """
  __slots__ = ('_path_helper', '_extmethods', '__authenticate_port','__host_mode','__reauthenticate_interval','__retransmit_interval','__supplicant_timeout','__max_requests','__server_fail_vlan','__auth_fail_vlan',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__authenticate_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authenticate-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='boolean', is_config=False)
    self.__host_mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'SINGLE_HOST': {}, 'MULTI_HOST': {}, 'MULTI_DOMAIN': {}},), is_leaf=True, yang_name="host-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='enumeration', is_config=False)
    self.__reauthenticate_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="reauthenticate-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    self.__supplicant_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="supplicant-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    self.__max_requests = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="max-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    self.__server_fail_vlan = YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="server-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)
    self.__auth_fail_vlan = YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="auth-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)

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
      return ['interfaces', 'interface', 'ethernet', 'dot1x', 'state']

  def _get_authenticate_port(self):
    """
    Getter method for authenticate_port, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/authenticate_port (boolean)

    YANG Description: Enable 802.1X port control on an interface.
    """
    return self.__authenticate_port
      
  def _set_authenticate_port(self, v, load=False):
    """
    Setter method for authenticate_port, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/authenticate_port (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authenticate_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authenticate_port() directly.

    YANG Description: Enable 802.1X port control on an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="authenticate-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authenticate_port must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authenticate-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='boolean', is_config=False)""",
        })

    self.__authenticate_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authenticate_port(self):
    self.__authenticate_port = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authenticate-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='boolean', is_config=False)


  def _get_host_mode(self):
    """
    Getter method for host_mode, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/host_mode (enumeration)

    YANG Description: Allow for single or multiple hosts to communicate through
an 802.1X controlled port.
    """
    return self.__host_mode
      
  def _set_host_mode(self, v, load=False):
    """
    Setter method for host_mode, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/host_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host_mode() directly.

    YANG Description: Allow for single or multiple hosts to communicate through
an 802.1X controlled port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'SINGLE_HOST': {}, 'MULTI_HOST': {}, 'MULTI_DOMAIN': {}},), is_leaf=True, yang_name="host-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host_mode must be of a type compatible with enumeration""",
          'defined-type': "openconfig-if-8021x:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'SINGLE_HOST': {}, 'MULTI_HOST': {}, 'MULTI_DOMAIN': {}},), is_leaf=True, yang_name="host-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='enumeration', is_config=False)""",
        })

    self.__host_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host_mode(self):
    self.__host_mode = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'SINGLE_HOST': {}, 'MULTI_HOST': {}, 'MULTI_DOMAIN': {}},), is_leaf=True, yang_name="host-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='enumeration', is_config=False)


  def _get_reauthenticate_interval(self):
    """
    Getter method for reauthenticate_interval, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/reauthenticate_interval (uint16)

    YANG Description: Enable periodic re-authentication of the device connected
to this port. Setting a value of 0 disabled reauthentication
on this port.
    """
    return self.__reauthenticate_interval
      
  def _set_reauthenticate_interval(self, v, load=False):
    """
    Setter method for reauthenticate_interval, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/reauthenticate_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reauthenticate_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reauthenticate_interval() directly.

    YANG Description: Enable periodic re-authentication of the device connected
to this port. Setting a value of 0 disabled reauthentication
on this port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="reauthenticate-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reauthenticate_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="reauthenticate-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)""",
        })

    self.__reauthenticate_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reauthenticate_interval(self):
    self.__reauthenticate_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="reauthenticate-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)


  def _get_retransmit_interval(self):
    """
    Getter method for retransmit_interval, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/retransmit_interval (uint16)

    YANG Description: How long the interface waits for a response from an
EAPoL Start before restarting 802.1X authentication on the
port.
    """
    return self.__retransmit_interval
      
  def _set_retransmit_interval(self, v, load=False):
    """
    Setter method for retransmit_interval, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/retransmit_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retransmit_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retransmit_interval() directly.

    YANG Description: How long the interface waits for a response from an
EAPoL Start before restarting 802.1X authentication on the
port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retransmit_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)""",
        })

    self.__retransmit_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retransmit_interval(self):
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)


  def _get_supplicant_timeout(self):
    """
    Getter method for supplicant_timeout, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/supplicant_timeout (uint16)

    YANG Description: Time to wait for a response from the supplicant before
restarting the 802.1X authentication process.
    """
    return self.__supplicant_timeout
      
  def _set_supplicant_timeout(self, v, load=False):
    """
    Setter method for supplicant_timeout, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/supplicant_timeout (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_supplicant_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_supplicant_timeout() directly.

    YANG Description: Time to wait for a response from the supplicant before
restarting the 802.1X authentication process.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="supplicant-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """supplicant_timeout must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="supplicant-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)""",
        })

    self.__supplicant_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_supplicant_timeout(self):
    self.__supplicant_timeout = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="supplicant-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)


  def _get_max_requests(self):
    """
    Getter method for max_requests, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/max_requests (uint16)

    YANG Description: Maximum number of times an EAPoL request packet is retransmitted
to the supplicant before the authentication session fails.
    """
    return self.__max_requests
      
  def _set_max_requests(self, v, load=False):
    """
    Setter method for max_requests, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/max_requests (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_requests is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_requests() directly.

    YANG Description: Maximum number of times an EAPoL request packet is retransmitted
to the supplicant before the authentication session fails.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="max-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_requests must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="max-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)""",
        })

    self.__max_requests = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_requests(self):
    self.__max_requests = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="max-requests", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='uint16', is_config=False)


  def _get_server_fail_vlan(self):
    """
    Getter method for server_fail_vlan, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/server_fail_vlan (union)

    YANG Description: If RADIUS is unresponsive, the supplicant shall be placed in
this VLAN. If this VLAN is configured as a VLAN name, the
vlan-map must be populated for the Authenticator to map this
VLAN name to a VLAN id.
    """
    return self.__server_fail_vlan
      
  def _set_server_fail_vlan(self, v, load=False):
    """
    Setter method for server_fail_vlan, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/server_fail_vlan (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_fail_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_fail_vlan() directly.

    YANG Description: If RADIUS is unresponsive, the supplicant shall be placed in
this VLAN. If this VLAN is configured as a VLAN name, the
vlan-map must be populated for the Authenticator to map this
VLAN name to a VLAN id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="server-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_fail_vlan must be of a type compatible with union""",
          'defined-type': "openconfig-if-8021x:union",
          'generated-type': """YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="server-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)""",
        })

    self.__server_fail_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_fail_vlan(self):
    self.__server_fail_vlan = YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="server-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)


  def _get_auth_fail_vlan(self):
    """
    Getter method for auth_fail_vlan, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/auth_fail_vlan (union)

    YANG Description: Upon failure to authenticate, the port is set to this VLAN.
If this VLAN is a configured as a VLAN name, the vlan-map must
be populated for the Authenticator to map this VLAN name to a
VLAN id.
    """
    return self.__auth_fail_vlan
      
  def _set_auth_fail_vlan(self, v, load=False):
    """
    Setter method for auth_fail_vlan, mapped from YANG variable /interfaces/interface/ethernet/dot1x/state/auth_fail_vlan (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_fail_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_fail_vlan() directly.

    YANG Description: Upon failure to authenticate, the port is set to this VLAN.
If this VLAN is a configured as a VLAN name, the vlan-map must
be populated for the Authenticator to map this VLAN name to a
VLAN id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="auth-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_fail_vlan must be of a type compatible with union""",
          'defined-type': "openconfig-if-8021x:union",
          'generated-type': """YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="auth-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)""",
        })

    self.__auth_fail_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_fail_vlan(self):
    self.__auth_fail_vlan = YANGDynClass(base=[six.text_type,RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['1..4094']}),], is_leaf=True, yang_name="auth-fail-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/8021x', defining_module='openconfig-if-8021x', yang_type='union', is_config=False)

  authenticate_port = __builtin__.property(_get_authenticate_port)
  host_mode = __builtin__.property(_get_host_mode)
  reauthenticate_interval = __builtin__.property(_get_reauthenticate_interval)
  retransmit_interval = __builtin__.property(_get_retransmit_interval)
  supplicant_timeout = __builtin__.property(_get_supplicant_timeout)
  max_requests = __builtin__.property(_get_max_requests)
  server_fail_vlan = __builtin__.property(_get_server_fail_vlan)
  auth_fail_vlan = __builtin__.property(_get_auth_fail_vlan)


  _pyangbind_elements = OrderedDict([('authenticate_port', authenticate_port), ('host_mode', host_mode), ('reauthenticate_interval', reauthenticate_interval), ('retransmit_interval', retransmit_interval), ('supplicant_timeout', supplicant_timeout), ('max_requests', max_requests), ('server_fail_vlan', server_fail_vlan), ('auth_fail_vlan', auth_fail_vlan), ])



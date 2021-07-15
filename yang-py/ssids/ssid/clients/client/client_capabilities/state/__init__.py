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
  from YANG module openconfig-wifi-mac - based on the path /ssids/ssid/clients/client/client-capabilities/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Container for Client capabilities, as reported by Assoc. Req.
or Probe Req. frames. Capability is supported, if present.
  """
  __slots__ = ('_path_helper', '_extmethods', '__client_capabilities','__channel_support',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__client_capabilities = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}},)), is_leaf=False, yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='identityref', is_config=False)
    self.__channel_support = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="channel-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=False)

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
      return ['ssids', 'ssid', 'clients', 'client', 'client-capabilities', 'state']

  def _get_client_capabilities(self):
    """
    Getter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities/state/client_capabilities (identityref)

    YANG Description: Features supported by client that are Optional
within the 802.11 specifications.
    """
    return self.__client_capabilities
      
  def _set_client_capabilities(self, v, load=False):
    """
    Setter method for client_capabilities, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities/state/client_capabilities (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_capabilities is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_capabilities() directly.

    YANG Description: Features supported by client that are Optional
within the 802.11 specifications.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}},)), is_leaf=False, yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_capabilities must be of a type compatible with identityref""",
          'defined-type': "openconfig-wifi-mac:identityref",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}},)), is_leaf=False, yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='identityref', is_config=False)""",
        })

    self.__client_capabilities = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_capabilities(self):
    self.__client_capabilities = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMER': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:MU_BEAMFORMEE': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11R': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi-types:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}, 'oc-wifi:DOT_11V': {'@module': 'openconfig-wifi-types', '@namespace': 'http://openconfig.net/yang/wifi/wifi-types'}},)), is_leaf=False, yang_name="client-capabilities", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='identityref', is_config=False)


  def _get_channel_support(self):
    """
    Getter method for channel_support, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities/state/channel_support (uint8)

    YANG Description: List of supported channels.
    """
    return self.__channel_support
      
  def _set_channel_support(self, v, load=False):
    """
    Setter method for channel_support, mapped from YANG variable /ssids/ssid/clients/client/client_capabilities/state/channel_support (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_channel_support is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_channel_support() directly.

    YANG Description: List of supported channels.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="channel-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """channel_support must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="channel-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=False)""",
        })

    self.__channel_support = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_channel_support(self):
    self.__channel_support = YANGDynClass(unique=True, base=TypedListType(allowed_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)), is_leaf=False, yang_name="channel-support", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi-mac', defining_module='openconfig-wifi-mac', yang_type='uint8', is_config=False)

  client_capabilities = __builtin__.property(_get_client_capabilities)
  channel_support = __builtin__.property(_get_channel_support)


  _pyangbind_elements = OrderedDict([('client_capabilities', client_capabilities), ('channel_support', channel_support), ])


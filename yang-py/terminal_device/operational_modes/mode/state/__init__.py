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
  from YANG module openconfig-terminal-device - based on the path /terminal-device/operational-modes/mode/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the platform-defined
operational mode
  """
  __slots__ = ('_path_helper', '_extmethods', '__mode_id','__description','__vendor_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mode_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='uint16', is_config=False)
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)
    self.__vendor_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="vendor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)

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
      return ['terminal-device', 'operational-modes', 'mode', 'state']

  def _get_mode_id(self):
    """
    Getter method for mode_id, mapped from YANG variable /terminal_device/operational_modes/mode/state/mode_id (uint16)

    YANG Description: Two-octet encoding of the vendor-defined operational
mode
    """
    return self.__mode_id
      
  def _set_mode_id(self, v, load=False):
    """
    Setter method for mode_id, mapped from YANG variable /terminal_device/operational_modes/mode/state/mode_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode_id() directly.

    YANG Description: Two-octet encoding of the vendor-defined operational
mode
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='uint16', is_config=False)""",
        })

    self.__mode_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode_id(self):
    self.__mode_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mode-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='uint16', is_config=False)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /terminal_device/operational_modes/mode/state/description (string)

    YANG Description: Vendor-supplied textual description of the characteristics
of this operational mode to enable operators to select the
appropriate mode for the application.
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /terminal_device/operational_modes/mode/state/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Vendor-supplied textual description of the characteristics
of this operational mode to enable operators to select the
appropriate mode for the application.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)


  def _get_vendor_id(self):
    """
    Getter method for vendor_id, mapped from YANG variable /terminal_device/operational_modes/mode/state/vendor_id (string)

    YANG Description: Identifier to represent the vendor / supplier of the
platform and the associated operational mode information
    """
    return self.__vendor_id
      
  def _set_vendor_id(self, v, load=False):
    """
    Setter method for vendor_id, mapped from YANG variable /terminal_device/operational_modes/mode/state/vendor_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor_id() directly.

    YANG Description: Identifier to represent the vendor / supplier of the
platform and the associated operational mode information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="vendor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="vendor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)""",
        })

    self.__vendor_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor_id(self):
    self.__vendor_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="vendor-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='string', is_config=False)

  mode_id = __builtin__.property(_get_mode_id)
  description = __builtin__.property(_get_description)
  vendor_id = __builtin__.property(_get_vendor_id)


  _pyangbind_elements = OrderedDict([('mode_id', mode_id), ('description', description), ('vendor_id', vendor_id), ])


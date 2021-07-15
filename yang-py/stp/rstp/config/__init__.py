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
  from YANG module openconfig-spanning-tree - based on the path /stp/rstp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for RSTP
  """
  __slots__ = ('_path_helper', '_extmethods', '__hello_time','__max_age','__forwarding_delay','__hold_count','__bridge_priority',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__forwarding_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__hold_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)

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
      return ['stp', 'rstp', 'config']

  def _get_hello_time(self):
    """
    Getter method for hello_time, mapped from YANG variable /stp/rstp/config/hello_time (uint8)

    YANG Description: The interval between periodic transmissions of
configuration messages by designated ports
    """
    return self.__hello_time
      
  def _set_hello_time(self, v, load=False):
    """
    Setter method for hello_time, mapped from YANG variable /stp/rstp/config/hello_time (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_time() directly.

    YANG Description: The interval between periodic transmissions of
configuration messages by designated ports
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_time must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__hello_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_time(self):
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_max_age(self):
    """
    Getter method for max_age, mapped from YANG variable /stp/rstp/config/max_age (uint8)

    YANG Description: The maximum age of the information transmitted by the
bridge when it is the root bridge
    """
    return self.__max_age
      
  def _set_max_age(self, v, load=False):
    """
    Setter method for max_age, mapped from YANG variable /stp/rstp/config/max_age (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_age() directly.

    YANG Description: The maximum age of the information transmitted by the
bridge when it is the root bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_age must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__max_age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_age(self):
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_forwarding_delay(self):
    """
    Getter method for forwarding_delay, mapped from YANG variable /stp/rstp/config/forwarding_delay (uint8)

    YANG Description: The delay used by STP bridges to transition root and
designated ports to forwarding
    """
    return self.__forwarding_delay
      
  def _set_forwarding_delay(self, v, load=False):
    """
    Setter method for forwarding_delay, mapped from YANG variable /stp/rstp/config/forwarding_delay (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_delay() directly.

    YANG Description: The delay used by STP bridges to transition root and
designated ports to forwarding
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_delay must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__forwarding_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_delay(self):
    self.__forwarding_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_hold_count(self):
    """
    Getter method for hold_count, mapped from YANG variable /stp/rstp/config/hold_count (uint8)

    YANG Description: the maximum number of BPDUs per second that the
switch can send from an interface
    """
    return self.__hold_count
      
  def _set_hold_count(self, v, load=False):
    """
    Setter method for hold_count, mapped from YANG variable /stp/rstp/config/hold_count (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_count() directly.

    YANG Description: the maximum number of BPDUs per second that the
switch can send from an interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_count must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__hold_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_count(self):
    self.__hold_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_bridge_priority(self):
    """
    Getter method for bridge_priority, mapped from YANG variable /stp/rstp/config/bridge_priority (oc-stp-types:stp-bridge-priority-type)

    YANG Description: The manageable component of the Bridge Identifier
    """
    return self.__bridge_priority
      
  def _set_bridge_priority(self, v, load=False):
    """
    Setter method for bridge_priority, mapped from YANG variable /stp/rstp/config/bridge_priority (oc-stp-types:stp-bridge-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_priority() directly.

    YANG Description: The manageable component of the Bridge Identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_priority must be of a type compatible with oc-stp-types:stp-bridge-priority-type""",
          'defined-type': "oc-stp-types:stp-bridge-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)""",
        })

    self.__bridge_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_priority(self):
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)

  hello_time = __builtin__.property(_get_hello_time, _set_hello_time)
  max_age = __builtin__.property(_get_max_age, _set_max_age)
  forwarding_delay = __builtin__.property(_get_forwarding_delay, _set_forwarding_delay)
  hold_count = __builtin__.property(_get_hold_count, _set_hold_count)
  bridge_priority = __builtin__.property(_get_bridge_priority, _set_bridge_priority)


  _pyangbind_elements = OrderedDict([('hello_time', hello_time), ('max_age', max_age), ('forwarding_delay', forwarding_delay), ('hold_count', hold_count), ('bridge_priority', bridge_priority), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-spanning-tree - based on the path /stp/rstp/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for RSTP
  """
  __slots__ = ('_path_helper', '_extmethods', '__hello_time','__max_age','__forwarding_delay','__hold_count','__bridge_priority',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__forwarding_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__hold_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)

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
      return ['stp', 'rstp', 'config']

  def _get_hello_time(self):
    """
    Getter method for hello_time, mapped from YANG variable /stp/rstp/config/hello_time (uint8)

    YANG Description: The interval between periodic transmissions of
configuration messages by designated ports
    """
    return self.__hello_time
      
  def _set_hello_time(self, v, load=False):
    """
    Setter method for hello_time, mapped from YANG variable /stp/rstp/config/hello_time (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_time() directly.

    YANG Description: The interval between periodic transmissions of
configuration messages by designated ports
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_time must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__hello_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_time(self):
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), is_leaf=True, yang_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_max_age(self):
    """
    Getter method for max_age, mapped from YANG variable /stp/rstp/config/max_age (uint8)

    YANG Description: The maximum age of the information transmitted by the
bridge when it is the root bridge
    """
    return self.__max_age
      
  def _set_max_age(self, v, load=False):
    """
    Setter method for max_age, mapped from YANG variable /stp/rstp/config/max_age (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_age() directly.

    YANG Description: The maximum age of the information transmitted by the
bridge when it is the root bridge
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_age must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__max_age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_age(self):
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['6..40']}), is_leaf=True, yang_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_forwarding_delay(self):
    """
    Getter method for forwarding_delay, mapped from YANG variable /stp/rstp/config/forwarding_delay (uint8)

    YANG Description: The delay used by STP bridges to transition root and
designated ports to forwarding
    """
    return self.__forwarding_delay
      
  def _set_forwarding_delay(self, v, load=False):
    """
    Setter method for forwarding_delay, mapped from YANG variable /stp/rstp/config/forwarding_delay (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_delay() directly.

    YANG Description: The delay used by STP bridges to transition root and
designated ports to forwarding
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_delay must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__forwarding_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_delay(self):
    self.__forwarding_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['4..30']}), is_leaf=True, yang_name="forwarding-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_hold_count(self):
    """
    Getter method for hold_count, mapped from YANG variable /stp/rstp/config/hold_count (uint8)

    YANG Description: the maximum number of BPDUs per second that the
switch can send from an interface
    """
    return self.__hold_count
      
  def _set_hold_count(self, v, load=False):
    """
    Setter method for hold_count, mapped from YANG variable /stp/rstp/config/hold_count (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_count() directly.

    YANG Description: the maximum number of BPDUs per second that the
switch can send from an interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_count must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)""",
        })

    self.__hold_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_count(self):
    self.__hold_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..10']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(6), is_leaf=True, yang_name="hold-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='uint8', is_config=True)


  def _get_bridge_priority(self):
    """
    Getter method for bridge_priority, mapped from YANG variable /stp/rstp/config/bridge_priority (oc-stp-types:stp-bridge-priority-type)

    YANG Description: The manageable component of the Bridge Identifier
    """
    return self.__bridge_priority
      
  def _set_bridge_priority(self, v, load=False):
    """
    Setter method for bridge_priority, mapped from YANG variable /stp/rstp/config/bridge_priority (oc-stp-types:stp-bridge-priority-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_priority() directly.

    YANG Description: The manageable component of the Bridge Identifier
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_priority must be of a type compatible with oc-stp-types:stp-bridge-priority-type""",
          'defined-type': "oc-stp-types:stp-bridge-priority-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)""",
        })

    self.__bridge_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_priority(self):
    self.__bridge_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..61440']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(32768), is_leaf=True, yang_name="bridge-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/spanning-tree', defining_module='openconfig-spanning-tree', yang_type='oc-stp-types:stp-bridge-priority-type', is_config=True)

  hello_time = __builtin__.property(_get_hello_time, _set_hello_time)
  max_age = __builtin__.property(_get_max_age, _set_max_age)
  forwarding_delay = __builtin__.property(_get_forwarding_delay, _set_forwarding_delay)
  hold_count = __builtin__.property(_get_hold_count, _set_hold_count)
  bridge_priority = __builtin__.property(_get_bridge_priority, _set_bridge_priority)


  _pyangbind_elements = OrderedDict([('hello_time', hello_time), ('max_age', max_age), ('forwarding_delay', forwarding_delay), ('hold_count', hold_count), ('bridge_priority', bridge_priority), ])



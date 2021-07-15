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
  from YANG module openconfig-access-points - based on the path /access-points/access-point/system/aaa/accounting/events/event/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for accounting events
  """
  __slots__ = ('_path_helper', '_extmethods', '__event_type','__record',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__event_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},), is_leaf=True, yang_name="event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    self.__record = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'START_STOP': {}, 'STOP': {}},), is_leaf=True, yang_name="record", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=True)

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
      return ['access-points', 'access-point', 'system', 'aaa', 'accounting', 'events', 'event', 'config']

  def _get_event_type(self):
    """
    Getter method for event_type, mapped from YANG variable /access_points/access_point/system/aaa/accounting/events/event/config/event_type (identityref)

    YANG Description: The type of activity to record at the AAA accounting
server
    """
    return self.__event_type
      
  def _set_event_type(self, v, load=False):
    """
    Setter method for event_type, mapped from YANG variable /access_points/access_point/system/aaa/accounting/events/event/config/event_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_event_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_event_type() directly.

    YANG Description: The type of activity to record at the AAA accounting
server
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},), is_leaf=True, yang_name="event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """event_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-access-points:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},), is_leaf=True, yang_name="event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)""",
        })

    self.__event_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_event_type(self):
    self.__event_type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_COMMAND': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}, 'oc-aaa-types:AAA_ACCOUNTING_EVENT_LOGIN': {'@module': 'openconfig-aaa-types', '@namespace': 'http://openconfig.net/yang/aaa/types'}},), is_leaf=True, yang_name="event-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='identityref', is_config=True)


  def _get_record(self):
    """
    Getter method for record, mapped from YANG variable /access_points/access_point/system/aaa/accounting/events/event/config/record (enumeration)

    YANG Description: Type of record to send to the accounting server for this
activity type
    """
    return self.__record
      
  def _set_record(self, v, load=False):
    """
    Setter method for record, mapped from YANG variable /access_points/access_point/system/aaa/accounting/events/event/config/record (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_record is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_record() directly.

    YANG Description: Type of record to send to the accounting server for this
activity type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'START_STOP': {}, 'STOP': {}},), is_leaf=True, yang_name="record", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """record must be of a type compatible with enumeration""",
          'defined-type': "openconfig-access-points:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'START_STOP': {}, 'STOP': {}},), is_leaf=True, yang_name="record", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=True)""",
        })

    self.__record = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_record(self):
    self.__record = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'START_STOP': {}, 'STOP': {}},), is_leaf=True, yang_name="record", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/wifi/access-points', defining_module='openconfig-access-points', yang_type='enumeration', is_config=True)

  event_type = __builtin__.property(_get_event_type, _set_event_type)
  record = __builtin__.property(_get_record, _set_record)


  _pyangbind_elements = OrderedDict([('event_type', event_type), ('record', record), ])



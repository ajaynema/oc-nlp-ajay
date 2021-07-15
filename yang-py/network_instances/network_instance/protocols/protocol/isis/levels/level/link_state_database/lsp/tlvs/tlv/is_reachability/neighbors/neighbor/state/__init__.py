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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/is-reachability/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS standard neighbor.
  """
  __slots__ = ('_path_helper', '_extmethods', '__system_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'is-reachability', 'neighbors', 'neighbor', 'state']

  def _get_system_id(self):
    """
    Getter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)

    YANG Description: System-ID of IS neighbor.
    """
    return self.__system_id
      
  def _set_system_id(self, v, load=False):
    """
    Setter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_id() directly.

    YANG Description: System-ID of IS neighbor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__system_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_id(self):
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  system_id = __builtin__.property(_get_system_id)


  _pyangbind_elements = OrderedDict([('system_id', system_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/is-reachability/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS standard neighbor.
  """
  __slots__ = ('_path_helper', '_extmethods', '__system_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'is-reachability', 'neighbors', 'neighbor', 'state']

  def _get_system_id(self):
    """
    Getter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)

    YANG Description: System-ID of IS neighbor.
    """
    return self.__system_id
      
  def _set_system_id(self, v, load=False):
    """
    Setter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_id() directly.

    YANG Description: System-ID of IS neighbor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__system_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_id(self):
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  system_id = __builtin__.property(_get_system_id)


  _pyangbind_elements = OrderedDict([('system_id', system_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/is-reachability/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS standard neighbor.
  """
  __slots__ = ('_path_helper', '_extmethods', '__system_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'is-reachability', 'neighbors', 'neighbor', 'state']

  def _get_system_id(self):
    """
    Getter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)

    YANG Description: System-ID of IS neighbor.
    """
    return self.__system_id
      
  def _set_system_id(self, v, load=False):
    """
    Setter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_id() directly.

    YANG Description: System-ID of IS neighbor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__system_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_id(self):
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  system_id = __builtin__.property(_get_system_id)


  _pyangbind_elements = OrderedDict([('system_id', system_id), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/is-reachability/neighbors/neighbor/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS standard neighbor.
  """
  __slots__ = ('_path_helper', '_extmethods', '__system_id',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'is-reachability', 'neighbors', 'neighbor', 'state']

  def _get_system_id(self):
    """
    Getter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)

    YANG Description: System-ID of IS neighbor.
    """
    return self.__system_id
      
  def _set_system_id(self, v, load=False):
    """
    Setter method for system_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/is_reachability/neighbors/neighbor/state/system_id (oc-isis-types:system-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_id() directly.

    YANG Description: System-ID of IS neighbor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_id must be of a type compatible with oc-isis-types:system-id""",
          'defined-type': "oc-isis-types:system-id",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)""",
        })

    self.__system_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_id(self):
    self.__system_id = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}\\.[0-9A-Fa-f]{4}$'}), is_leaf=True, yang_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:system-id', is_config=False)

  system_id = __builtin__.property(_get_system_id)


  _pyangbind_elements = OrderedDict([('system_id', system_id), ])



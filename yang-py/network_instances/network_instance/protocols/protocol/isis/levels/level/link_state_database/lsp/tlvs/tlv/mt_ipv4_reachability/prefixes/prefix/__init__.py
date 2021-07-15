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

from . import state
from . import subtlvs
from . import undefined_subtlvs
class prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 prefixes that are contained within MT
reachability TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mt_id','__prefix','__state','__subtlvs','__undefined_subtlvs',)

  _yang_name = 'prefix'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mt_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__prefix = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__subtlvs = YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-ipv4-reachability', 'prefixes', 'prefix']

  def _get_mt_id(self):
    """
    Getter method for mt_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt_id (leafref)

    YANG Description: Reference to the topology ID of the topology that
the prefix is within.
    """
    return self.__mt_id
      
  def _set_mt_id(self, v, load=False):
    """
    Setter method for mt_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mt_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mt_id() directly.

    YANG Description: Reference to the topology ID of the topology that
the prefix is within.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mt_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__mt_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mt_id(self):
    self.__mt_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/prefix (leafref)

    YANG Description: Reference to the prefix to which reachability is
being advertised.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/prefix (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: Reference to the prefix to which reachability is
being advertised.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_subtlvs(self):
    """
    Getter method for subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs (container)

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    return self.__subtlvs
      
  def _set_subtlvs(self, v, load=False):
    """
    Setter method for subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subtlvs() directly.

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subtlvs(self):
    self.__subtlvs = YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_undefined_subtlvs(self):
    """
    Getter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)

    YANG Description: This container describes undefined ISIS TLVs.
    """
    return self.__undefined_subtlvs
      
  def _set_undefined_subtlvs(self, v, load=False):
    """
    Setter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_undefined_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_undefined_subtlvs() directly.

    YANG Description: This container describes undefined ISIS TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """undefined_subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__undefined_subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_undefined_subtlvs(self):
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mt_id = __builtin__.property(_get_mt_id)
  prefix = __builtin__.property(_get_prefix)
  state = __builtin__.property(_get_state)
  subtlvs = __builtin__.property(_get_subtlvs)
  undefined_subtlvs = __builtin__.property(_get_undefined_subtlvs)


  _pyangbind_elements = OrderedDict([('mt_id', mt_id), ('prefix', prefix), ('state', state), ('subtlvs', subtlvs), ('undefined_subtlvs', undefined_subtlvs), ])


from . import state
from . import subtlvs
from . import undefined_subtlvs
class prefix(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 prefixes that are contained within MT
reachability TLV.
  """
  __slots__ = ('_path_helper', '_extmethods', '__mt_id','__prefix','__state','__subtlvs','__undefined_subtlvs',)

  _yang_name = 'prefix'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__mt_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__prefix = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__subtlvs = YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'levels', 'level', 'link-state-database', 'lsp', 'tlvs', 'tlv', 'mt-ipv4-reachability', 'prefixes', 'prefix']

  def _get_mt_id(self):
    """
    Getter method for mt_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt_id (leafref)

    YANG Description: Reference to the topology ID of the topology that
the prefix is within.
    """
    return self.__mt_id
      
  def _set_mt_id(self, v, load=False):
    """
    Setter method for mt_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/mt_id (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mt_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mt_id() directly.

    YANG Description: Reference to the topology ID of the topology that
the prefix is within.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mt_id must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__mt_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mt_id(self):
    self.__mt_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="mt-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_prefix(self):
    """
    Getter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/prefix (leafref)

    YANG Description: Reference to the prefix to which reachability is
being advertised.
    """
    return self.__prefix
      
  def _set_prefix(self, v, load=False):
    """
    Setter method for prefix, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/prefix (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix() directly.

    YANG Description: Reference to the prefix to which reachability is
being advertised.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix(self):
    self.__prefix = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of an IPv4 extended prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_subtlvs(self):
    """
    Getter method for subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs (container)

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    return self.__subtlvs
      
  def _set_subtlvs(self, v, load=False):
    """
    Setter method for subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_subtlvs() directly.

    YANG Description: This container describes IS prefix sub-TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_subtlvs(self):
    self.__subtlvs = YANGDynClass(base=subtlvs.subtlvs, is_container='container', yang_name="subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_undefined_subtlvs(self):
    """
    Getter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)

    YANG Description: This container describes undefined ISIS TLVs.
    """
    return self.__undefined_subtlvs
      
  def _set_undefined_subtlvs(self, v, load=False):
    """
    Setter method for undefined_subtlvs, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_undefined_subtlvs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_undefined_subtlvs() directly.

    YANG Description: This container describes undefined ISIS TLVs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """undefined_subtlvs must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__undefined_subtlvs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_undefined_subtlvs(self):
    self.__undefined_subtlvs = YANGDynClass(base=undefined_subtlvs.undefined_subtlvs, is_container='container', yang_name="undefined-subtlvs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  mt_id = __builtin__.property(_get_mt_id)
  prefix = __builtin__.property(_get_prefix)
  state = __builtin__.property(_get_state)
  subtlvs = __builtin__.property(_get_subtlvs)
  undefined_subtlvs = __builtin__.property(_get_undefined_subtlvs)


  _pyangbind_elements = OrderedDict([('mt_id', mt_id), ('prefix', prefix), ('state', state), ('subtlvs', subtlvs), ('undefined_subtlvs', undefined_subtlvs), ])



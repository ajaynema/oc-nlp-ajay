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

from . import config
from . import state
from . import timers
from . import graceful_restart
from . import mpls
from . import inter_area_propagation_policies
class global_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__timers','__graceful_restart','__mpls','__inter_area_propagation_policies',)

  _yang_name = 'global'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__timers = YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__inter_area_propagation_policies = YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'global']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config (container)

    YANG Description: Global configuration parameters for OSPFv2
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Global configuration parameters for OSPFv2
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/state (container)

    YANG Description: Operational state parameters for OSPFv2
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters for OSPFv2
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_timers(self):
    """
    Getter method for timers, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers (container)

    YANG Description: Configuration and operational state parameters for OSPFv2
timers
    """
    return self.__timers
      
  def _set_timers(self, v, load=False):
    """
    Setter method for timers, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timers() directly.

    YANG Description: Configuration and operational state parameters for OSPFv2
timers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__timers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timers(self):
    self.__timers = YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_graceful_restart(self):
    """
    Getter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart (container)

    YANG Description: Configuration and operational state parameters for OSPFv2
graceful restart
    """
    return self.__graceful_restart
      
  def _set_graceful_restart(self, v, load=False):
    """
    Setter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart() directly.

    YANG Description: Configuration and operational state parameters for OSPFv2
graceful restart
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__graceful_restart = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart(self):
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_mpls(self):
    """
    Getter method for mpls, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/mpls (container)

    YANG Description: OSPFv2 parameters relating to MPLS
    """
    return self.__mpls
      
  def _set_mpls(self, v, load=False):
    """
    Setter method for mpls, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/mpls (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls() directly.

    YANG Description: OSPFv2 parameters relating to MPLS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__mpls = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls(self):
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_inter_area_propagation_policies(self):
    """
    Getter method for inter_area_propagation_policies, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/inter_area_propagation_policies (container)

    YANG Description: Policies defining how inter-area propagation should be performed
by the OSPF instance
    """
    return self.__inter_area_propagation_policies
      
  def _set_inter_area_propagation_policies(self, v, load=False):
    """
    Setter method for inter_area_propagation_policies, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/inter_area_propagation_policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inter_area_propagation_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inter_area_propagation_policies() directly.

    YANG Description: Policies defining how inter-area propagation should be performed
by the OSPF instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inter_area_propagation_policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__inter_area_propagation_policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inter_area_propagation_policies(self):
    self.__inter_area_propagation_policies = YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  timers = __builtin__.property(_get_timers, _set_timers)
  graceful_restart = __builtin__.property(_get_graceful_restart, _set_graceful_restart)
  mpls = __builtin__.property(_get_mpls, _set_mpls)
  inter_area_propagation_policies = __builtin__.property(_get_inter_area_propagation_policies, _set_inter_area_propagation_policies)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('timers', timers), ('graceful_restart', graceful_restart), ('mpls', mpls), ('inter_area_propagation_policies', inter_area_propagation_policies), ])


from . import config
from . import state
from . import timers
from . import graceful_restart
from . import mpls
from . import inter_area_propagation_policies
class global_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__timers','__graceful_restart','__mpls','__inter_area_propagation_policies',)

  _yang_name = 'global'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__timers = YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__inter_area_propagation_policies = YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'ospfv2', 'global']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config (container)

    YANG Description: Global configuration parameters for OSPFv2
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Global configuration parameters for OSPFv2
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/state (container)

    YANG Description: Operational state parameters for OSPFv2
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters for OSPFv2
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_timers(self):
    """
    Getter method for timers, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers (container)

    YANG Description: Configuration and operational state parameters for OSPFv2
timers
    """
    return self.__timers
      
  def _set_timers(self, v, load=False):
    """
    Setter method for timers, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/timers (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timers() directly.

    YANG Description: Configuration and operational state parameters for OSPFv2
timers
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timers must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__timers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timers(self):
    self.__timers = YANGDynClass(base=timers.timers, is_container='container', yang_name="timers", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_graceful_restart(self):
    """
    Getter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart (container)

    YANG Description: Configuration and operational state parameters for OSPFv2
graceful restart
    """
    return self.__graceful_restart
      
  def _set_graceful_restart(self, v, load=False):
    """
    Setter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/graceful_restart (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart() directly.

    YANG Description: Configuration and operational state parameters for OSPFv2
graceful restart
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """graceful_restart must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__graceful_restart = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_graceful_restart(self):
    self.__graceful_restart = YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_mpls(self):
    """
    Getter method for mpls, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/mpls (container)

    YANG Description: OSPFv2 parameters relating to MPLS
    """
    return self.__mpls
      
  def _set_mpls(self, v, load=False):
    """
    Setter method for mpls, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/mpls (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls() directly.

    YANG Description: OSPFv2 parameters relating to MPLS
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__mpls = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls(self):
    self.__mpls = YANGDynClass(base=mpls.mpls, is_container='container', yang_name="mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_inter_area_propagation_policies(self):
    """
    Getter method for inter_area_propagation_policies, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/inter_area_propagation_policies (container)

    YANG Description: Policies defining how inter-area propagation should be performed
by the OSPF instance
    """
    return self.__inter_area_propagation_policies
      
  def _set_inter_area_propagation_policies(self, v, load=False):
    """
    Setter method for inter_area_propagation_policies, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global/inter_area_propagation_policies (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_inter_area_propagation_policies is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_inter_area_propagation_policies() directly.

    YANG Description: Policies defining how inter-area propagation should be performed
by the OSPF instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """inter_area_propagation_policies must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__inter_area_propagation_policies = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_inter_area_propagation_policies(self):
    self.__inter_area_propagation_policies = YANGDynClass(base=inter_area_propagation_policies.inter_area_propagation_policies, is_container='container', yang_name="inter-area-propagation-policies", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  timers = __builtin__.property(_get_timers, _set_timers)
  graceful_restart = __builtin__.property(_get_graceful_restart, _set_graceful_restart)
  mpls = __builtin__.property(_get_mpls, _set_mpls)
  inter_area_propagation_policies = __builtin__.property(_get_inter_area_propagation_policies, _set_inter_area_propagation_policies)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('timers', timers), ('graceful_restart', graceful_restart), ('mpls', mpls), ('inter_area_propagation_policies', inter_area_propagation_policies), ])



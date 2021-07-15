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
from . import match
from . import ingress_mapping
from . import egress_mapping
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for VLAN interface-specific
data on subinterfaces
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__match','__ingress_mapping','__egress_mapping',)

  _yang_name = 'vlan'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__ingress_mapping = YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__egress_mapping = YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/config (container)

    YANG Description: Configuration parameters for VLANs
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for VLANs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/state (container)

    YANG Description: State variables for VLANs
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for VLANs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_match(self):
    """
    Getter method for match, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match (container)

    YANG Description: Configuration for various VLAN tag matching schemes,
including single-tagged 802.1q packets and double-tagged
802.1ad 'Q-in-Q' packets. Typically only one of the subordinate
containers should be specified.

Wildcards may be matched by specifying range values of 2-4094.
If implementations have a more efficient way to match Wildcards
then they should recognize this pattern and translate accordingly.

Implementations are expected to return errors for combinations
that they do not support, or provide deviations to the same effect.

For simple VLAN configurations without an 'egress-mapping' then
using the 'single-tagged' and 'double-tagged' VLAN matches that
resolve to specific values, these specify the VLAN identifiers
applied to packets on egress.
    """
    return self.__match
      
  def _set_match(self, v, load=False):
    """
    Setter method for match, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match() directly.

    YANG Description: Configuration for various VLAN tag matching schemes,
including single-tagged 802.1q packets and double-tagged
802.1ad 'Q-in-Q' packets. Typically only one of the subordinate
containers should be specified.

Wildcards may be matched by specifying range values of 2-4094.
If implementations have a more efficient way to match Wildcards
then they should recognize this pattern and translate accordingly.

Implementations are expected to return errors for combinations
that they do not support, or provide deviations to the same effect.

For simple VLAN configurations without an 'egress-mapping' then
using the 'single-tagged' and 'double-tagged' VLAN matches that
resolve to specific values, these specify the VLAN identifiers
applied to packets on egress.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__match = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match(self):
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_ingress_mapping(self):
    """
    Getter method for ingress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/ingress_mapping (container)

    YANG Description: Ingress VLAN stack behaviors for packets that arrive on
this subinterface after their VLAN idenitifer(s) have been
matched.
    """
    return self.__ingress_mapping
      
  def _set_ingress_mapping(self, v, load=False):
    """
    Setter method for ingress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/ingress_mapping (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_mapping() directly.

    YANG Description: Ingress VLAN stack behaviors for packets that arrive on
this subinterface after their VLAN idenitifer(s) have been
matched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_mapping must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__ingress_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_mapping(self):
    self.__ingress_mapping = YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_egress_mapping(self):
    """
    Getter method for egress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping (container)

    YANG Description: Egress VLAN and label behaviors for packets that are
destined for output via this subinterface.
    """
    return self.__egress_mapping
      
  def _set_egress_mapping(self, v, load=False):
    """
    Setter method for egress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress_mapping() directly.

    YANG Description: Egress VLAN and label behaviors for packets that are
destined for output via this subinterface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress_mapping must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__egress_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress_mapping(self):
    self.__egress_mapping = YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  match = __builtin__.property(_get_match, _set_match)
  ingress_mapping = __builtin__.property(_get_ingress_mapping, _set_ingress_mapping)
  egress_mapping = __builtin__.property(_get_egress_mapping, _set_egress_mapping)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('match', match), ('ingress_mapping', ingress_mapping), ('egress_mapping', egress_mapping), ])


from . import config
from . import state
from . import match
from . import ingress_mapping
from . import egress_mapping
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for VLAN interface-specific
data on subinterfaces
  """
  __slots__ = ('_path_helper', '_extmethods', '__config','__state','__match','__ingress_mapping','__egress_mapping',)

  _yang_name = 'vlan'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__ingress_mapping = YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    self.__egress_mapping = YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

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
      return ['interfaces', 'interface', 'subinterfaces', 'subinterface', 'vlan']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/config (container)

    YANG Description: Configuration parameters for VLANs
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for VLANs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/state (container)

    YANG Description: State variables for VLANs
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State variables for VLANs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_match(self):
    """
    Getter method for match, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match (container)

    YANG Description: Configuration for various VLAN tag matching schemes,
including single-tagged 802.1q packets and double-tagged
802.1ad 'Q-in-Q' packets. Typically only one of the subordinate
containers should be specified.

Wildcards may be matched by specifying range values of 2-4094.
If implementations have a more efficient way to match Wildcards
then they should recognize this pattern and translate accordingly.

Implementations are expected to return errors for combinations
that they do not support, or provide deviations to the same effect.

For simple VLAN configurations without an 'egress-mapping' then
using the 'single-tagged' and 'double-tagged' VLAN matches that
resolve to specific values, these specify the VLAN identifiers
applied to packets on egress.
    """
    return self.__match
      
  def _set_match(self, v, load=False):
    """
    Setter method for match, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/match (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_match is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_match() directly.

    YANG Description: Configuration for various VLAN tag matching schemes,
including single-tagged 802.1q packets and double-tagged
802.1ad 'Q-in-Q' packets. Typically only one of the subordinate
containers should be specified.

Wildcards may be matched by specifying range values of 2-4094.
If implementations have a more efficient way to match Wildcards
then they should recognize this pattern and translate accordingly.

Implementations are expected to return errors for combinations
that they do not support, or provide deviations to the same effect.

For simple VLAN configurations without an 'egress-mapping' then
using the 'single-tagged' and 'double-tagged' VLAN matches that
resolve to specific values, these specify the VLAN identifiers
applied to packets on egress.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """match must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__match = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_match(self):
    self.__match = YANGDynClass(base=match.match, is_container='container', yang_name="match", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_ingress_mapping(self):
    """
    Getter method for ingress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/ingress_mapping (container)

    YANG Description: Ingress VLAN stack behaviors for packets that arrive on
this subinterface after their VLAN idenitifer(s) have been
matched.
    """
    return self.__ingress_mapping
      
  def _set_ingress_mapping(self, v, load=False):
    """
    Setter method for ingress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/ingress_mapping (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_mapping() directly.

    YANG Description: Ingress VLAN stack behaviors for packets that arrive on
this subinterface after their VLAN idenitifer(s) have been
matched.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_mapping must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__ingress_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_mapping(self):
    self.__ingress_mapping = YANGDynClass(base=ingress_mapping.ingress_mapping, is_container='container', yang_name="ingress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)


  def _get_egress_mapping(self):
    """
    Getter method for egress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping (container)

    YANG Description: Egress VLAN and label behaviors for packets that are
destined for output via this subinterface.
    """
    return self.__egress_mapping
      
  def _set_egress_mapping(self, v, load=False):
    """
    Setter method for egress_mapping, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/vlan/egress_mapping (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_egress_mapping is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_egress_mapping() directly.

    YANG Description: Egress VLAN and label behaviors for packets that are
destined for output via this subinterface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """egress_mapping must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)""",
        })

    self.__egress_mapping = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_egress_mapping(self):
    self.__egress_mapping = YANGDynClass(base=egress_mapping.egress_mapping, is_container='container', yang_name="egress-mapping", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  match = __builtin__.property(_get_match, _set_match)
  ingress_mapping = __builtin__.property(_get_ingress_mapping, _set_ingress_mapping)
  egress_mapping = __builtin__.property(_get_egress_mapping, _set_egress_mapping)


  _pyangbind_elements = OrderedDict([('config', config), ('state', state), ('match', match), ('ingress_mapping', ingress_mapping), ('egress_mapping', egress_mapping), ])



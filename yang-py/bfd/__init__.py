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

from . import interfaces
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters for BFD.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interfaces',)

  _yang_name = 'bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

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
      return ['bfd']

  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /bfd/interfaces (container)

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /bfd/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('interfaces', interfaces), ])


from . import interfaces
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters for BFD.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interfaces',)

  _yang_name = 'bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

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
      return ['bfd']

  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /bfd/interfaces (container)

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /bfd/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('interfaces', interfaces), ])


from . import interfaces
class bfd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bfd - based on the path /bfd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration and operational state parameters for BFD.
  """
  __slots__ = ('_path_helper', '_extmethods', '__interfaces',)

  _yang_name = 'bfd'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

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
      return ['bfd']

  def _get_interfaces(self):
    """
    Getter method for interfaces, mapped from YANG variable /bfd/interfaces (container)

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    return self.__interfaces
      
  def _set_interfaces(self, v, load=False):
    """
    Setter method for interfaces, mapped from YANG variable /bfd/interfaces (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interfaces is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interfaces() directly.

    YANG Description: Interfaces on which BFD sessions are to be enabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interfaces must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)""",
        })

    self.__interfaces = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interfaces(self):
    self.__interfaces = YANGDynClass(base=interfaces.interfaces, is_container='container', yang_name="interfaces", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/bfd', defining_module='openconfig-bfd', yang_type='container', is_config=True)

  interfaces = __builtin__.property(_get_interfaces, _set_interfaces)


  _pyangbind_elements = OrderedDict([('interfaces', interfaces), ])


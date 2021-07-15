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

from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])


from . import ingress_acl_set
class ingress_acl_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-acl - based on the path /acl/interfaces/interface/ingress-acl-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of ingress ACLs on the
interface
  """
  __slots__ = ('_path_helper', '_extmethods', '__ingress_acl_set',)

  _yang_name = 'ingress-acl-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

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
      return ['acl', 'interfaces', 'interface', 'ingress-acl-sets']

  def _get_ingress_acl_set(self):
    """
    Getter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)

    YANG Description: List of ingress ACLs on the interface
    """
    return self.__ingress_acl_set
      
  def _set_ingress_acl_set(self, v, load=False):
    """
    Setter method for ingress_acl_set, mapped from YANG variable /acl/interfaces/interface/ingress_acl_sets/ingress_acl_set (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ingress_acl_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ingress_acl_set() directly.

    YANG Description: List of ingress ACLs on the interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ingress_acl_set must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)""",
        })

    self.__ingress_acl_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ingress_acl_set(self):
    self.__ingress_acl_set = YANGDynClass(base=YANGListType("set_name type",ingress_acl_set.ingress_acl_set, yang_name="ingress-acl-set", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='set-name type', extensions=None), is_container='list', yang_name="ingress-acl-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/acl', defining_module='openconfig-acl', yang_type='list', is_config=True)

  ingress_acl_set = __builtin__.property(_get_ingress_acl_set, _set_ingress_acl_set)


  _pyangbind_elements = OrderedDict([('ingress_acl_set', ingress_acl_set), ])



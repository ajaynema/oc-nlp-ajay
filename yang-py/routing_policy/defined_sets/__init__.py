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

from . import prefix_sets
from . import neighbor_sets
from . import tag_sets
class defined_sets(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-routing-policy - based on the path /routing-policy/defined-sets. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Predefined sets of attributes used in policy match
statements
  """
  __slots__ = ('_path_helper', '_extmethods', '__prefix_sets','__neighbor_sets','__tag_sets',)

  _yang_name = 'defined-sets'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__prefix_sets = YANGDynClass(base=prefix_sets.prefix_sets, is_container='container', yang_name="prefix-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__neighbor_sets = YANGDynClass(base=neighbor_sets.neighbor_sets, is_container='container', yang_name="neighbor-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    self.__tag_sets = YANGDynClass(base=tag_sets.tag_sets, is_container='container', yang_name="tag-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

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
      return ['routing-policy', 'defined-sets']

  def _get_prefix_sets(self):
    """
    Getter method for prefix_sets, mapped from YANG variable /routing_policy/defined_sets/prefix_sets (container)

    YANG Description: Enclosing container 
    """
    return self.__prefix_sets
      
  def _set_prefix_sets(self, v, load=False):
    """
    Setter method for prefix_sets, mapped from YANG variable /routing_policy/defined_sets/prefix_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_sets() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_sets.prefix_sets, is_container='container', yang_name="prefix-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_sets.prefix_sets, is_container='container', yang_name="prefix-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__prefix_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_sets(self):
    self.__prefix_sets = YANGDynClass(base=prefix_sets.prefix_sets, is_container='container', yang_name="prefix-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_neighbor_sets(self):
    """
    Getter method for neighbor_sets, mapped from YANG variable /routing_policy/defined_sets/neighbor_sets (container)

    YANG Description: Enclosing container for the list of neighbor set
definitions
    """
    return self.__neighbor_sets
      
  def _set_neighbor_sets(self, v, load=False):
    """
    Setter method for neighbor_sets, mapped from YANG variable /routing_policy/defined_sets/neighbor_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_sets() directly.

    YANG Description: Enclosing container for the list of neighbor set
definitions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbor_sets.neighbor_sets, is_container='container', yang_name="neighbor-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor_sets.neighbor_sets, is_container='container', yang_name="neighbor-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__neighbor_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_sets(self):
    self.__neighbor_sets = YANGDynClass(base=neighbor_sets.neighbor_sets, is_container='container', yang_name="neighbor-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)


  def _get_tag_sets(self):
    """
    Getter method for tag_sets, mapped from YANG variable /routing_policy/defined_sets/tag_sets (container)

    YANG Description: Enclosing container for the list of tag sets.
    """
    return self.__tag_sets
      
  def _set_tag_sets(self, v, load=False):
    """
    Setter method for tag_sets, mapped from YANG variable /routing_policy/defined_sets/tag_sets (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag_sets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag_sets() directly.

    YANG Description: Enclosing container for the list of tag sets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tag_sets.tag_sets, is_container='container', yang_name="tag-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag_sets must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tag_sets.tag_sets, is_container='container', yang_name="tag-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)""",
        })

    self.__tag_sets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag_sets(self):
    self.__tag_sets = YANGDynClass(base=tag_sets.tag_sets, is_container='container', yang_name="tag-sets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='container', is_config=True)

  prefix_sets = __builtin__.property(_get_prefix_sets, _set_prefix_sets)
  neighbor_sets = __builtin__.property(_get_neighbor_sets, _set_neighbor_sets)
  tag_sets = __builtin__.property(_get_tag_sets, _set_tag_sets)


  _pyangbind_elements = OrderedDict([('prefix_sets', prefix_sets), ('neighbor_sets', neighbor_sets), ('tag_sets', tag_sets), ])



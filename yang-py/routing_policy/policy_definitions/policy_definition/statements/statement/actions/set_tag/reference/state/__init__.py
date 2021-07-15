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
  from YANG module openconfig-routing-policy - based on the path /routing-policy/policy-definitions/policy-definition/statements/statement/actions/set-tag/reference/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state related to specifying a tag-set to be applied to a
route.
  """
  __slots__ = ('_path_helper', '_extmethods', '__tag_set',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__tag_set = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)

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
      return ['routing-policy', 'policy-definitions', 'policy-definition', 'statements', 'statement', 'actions', 'set-tag', 'reference', 'state']

  def _get_tag_set(self):
    """
    Getter method for tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/reference/state/tag_set (leafref)

    YANG Description: Use the referenced tag-set to set tags on the prefixes that match the
specified conditions. When a tag is set it MUST be possible to match the
value set in subsequent policies on the local device. where the protocol that
is carrying the prefix has a tag field (OSPF, and IS-IS for in particular)
the tag MUST be set in the corresponding protocol advertisements of the
prefix.
    """
    return self.__tag_set
      
  def _set_tag_set(self, v, load=False):
    """
    Setter method for tag_set, mapped from YANG variable /routing_policy/policy_definitions/policy_definition/statements/statement/actions/set_tag/reference/state/tag_set (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag_set() directly.

    YANG Description: Use the referenced tag-set to set tags on the prefixes that match the
specified conditions. When a tag is set it MUST be possible to match the
value set in subsequent policies on the local device. where the protocol that
is carrying the prefix has a tag field (OSPF, and IS-IS for in particular)
the tag MUST be set in the corresponding protocol advertisements of the
prefix.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag_set must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)""",
        })

    self.__tag_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag_set(self):
    self.__tag_set = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="tag-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/routing-policy', defining_module='openconfig-routing-policy', yang_type='leafref', is_config=False)

  tag_set = __builtin__.property(_get_tag_set)


  _pyangbind_elements = OrderedDict([('tag_set', tag_set), ])



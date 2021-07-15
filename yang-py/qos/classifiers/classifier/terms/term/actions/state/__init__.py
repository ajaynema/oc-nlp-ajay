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
  from YANG module openconfig-qos - based on the path /qos/classifiers/classifier/terms/term/actions/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters associated with classifier term
actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__target_group',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

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
      return ['qos', 'classifiers', 'classifier', 'terms', 'term', 'actions', 'state']

  def _get_target_group(self):
    """
    Getter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    return self.__target_group
      
  def _set_target_group(self, v, load=False):
    """
    Setter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_group() directly.

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)""",
        })

    self.__target_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_group(self):
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

  target_group = __builtin__.property(_get_target_group)


  _pyangbind_elements = OrderedDict([('target_group', target_group), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/classifiers/classifier/terms/term/actions/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters associated with classifier term
actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__target_group',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

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
      return ['qos', 'classifiers', 'classifier', 'terms', 'term', 'actions', 'state']

  def _get_target_group(self):
    """
    Getter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    return self.__target_group
      
  def _set_target_group(self, v, load=False):
    """
    Setter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_group() directly.

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)""",
        })

    self.__target_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_group(self):
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

  target_group = __builtin__.property(_get_target_group)


  _pyangbind_elements = OrderedDict([('target_group', target_group), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/classifiers/classifier/terms/term/actions/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters associated with classifier term
actions
  """
  __slots__ = ('_path_helper', '_extmethods', '__target_group',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

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
      return ['qos', 'classifiers', 'classifier', 'terms', 'term', 'actions', 'state']

  def _get_target_group(self):
    """
    Getter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    return self.__target_group
      
  def _set_target_group(self, v, load=False):
    """
    Setter method for target_group, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state/target_group (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_group() directly.

    YANG Description: References the forwarding group or class to which the
matched packets should be assigned
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_group must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)""",
        })

    self.__target_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_group(self):
    self.__target_group = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="target-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=False)

  target_group = __builtin__.property(_get_target_group)


  _pyangbind_elements = OrderedDict([('target_group', target_group), ])



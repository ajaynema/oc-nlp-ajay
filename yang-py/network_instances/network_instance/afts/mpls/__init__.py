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

from . import label_entry
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for MPLS label based
forwarding entries. Entries within the table are keyed based
on the top-most MPLS label in the stack on the ingress
packet.
  """
  __slots__ = ('_path_helper', '_extmethods', '__label_entry',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__label_entry = YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'mpls']

  def _get_label_entry(self):
    """
    Getter method for label_entry, mapped from YANG variable /network_instances/network_instance/afts/mpls/label_entry (list)

    YANG Description: List of the MPLS entries within the abstract
forwarding table. This list is keyed by the top-most MPLS
label.
    """
    return self.__label_entry
      
  def _set_label_entry(self, v, load=False):
    """
    Setter method for label_entry, mapped from YANG variable /network_instances/network_instance/afts/mpls/label_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label_entry() directly.

    YANG Description: List of the MPLS entries within the abstract
forwarding table. This list is keyed by the top-most MPLS
label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__label_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label_entry(self):
    self.__label_entry = YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  label_entry = __builtin__.property(_get_label_entry)


  _pyangbind_elements = OrderedDict([('label_entry', label_entry), ])


from . import label_entry
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding table for MPLS label based
forwarding entries. Entries within the table are keyed based
on the top-most MPLS label in the stack on the ingress
packet.
  """
  __slots__ = ('_path_helper', '_extmethods', '__label_entry',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__label_entry = YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return ['network-instances', 'network-instance', 'afts', 'mpls']

  def _get_label_entry(self):
    """
    Getter method for label_entry, mapped from YANG variable /network_instances/network_instance/afts/mpls/label_entry (list)

    YANG Description: List of the MPLS entries within the abstract
forwarding table. This list is keyed by the top-most MPLS
label.
    """
    return self.__label_entry
      
  def _set_label_entry(self, v, load=False):
    """
    Setter method for label_entry, mapped from YANG variable /network_instances/network_instance/afts/mpls/label_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label_entry() directly.

    YANG Description: List of the MPLS entries within the abstract
forwarding table. This list is keyed by the top-most MPLS
label.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__label_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label_entry(self):
    self.__label_entry = YANGDynClass(base=YANGListType("label",label_entry.label_entry, yang_name="label-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='label', extensions=None), is_container='list', yang_name="label-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  label_entry = __builtin__.property(_get_label_entry)


  _pyangbind_elements = OrderedDict([('label_entry', label_entry), ])


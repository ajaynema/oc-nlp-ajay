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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/evpn/evpn-instances/evpn-instance/pbb/b-component/i-components/i-component/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State variables for the i-sid
  """
  __slots__ = ('_path_helper', '_extmethods', '__i_sid',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__i_sid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'evpn', 'evpn-instances', 'evpn-instance', 'pbb', 'b-component', 'i-components', 'i-component', 'state']

  def _get_i_sid(self):
    """
    Getter method for i_sid, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components/i_component/state/i_sid (uint32)

    YANG Description: Service Instance Identifier 24 bits and global within a PBB
network. I-SID defines the service instance that the frame should be
mapped to.
    """
    return self.__i_sid
      
  def _set_i_sid(self, v, load=False):
    """
    Setter method for i_sid, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components/i_component/state/i_sid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_sid() directly.

    YANG Description: Service Instance Identifier 24 bits and global within a PBB
network. I-SID defines the service instance that the frame should be
mapped to.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_sid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__i_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_sid(self):
    self.__i_sid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  i_sid = __builtin__.property(_get_i_sid)


  _pyangbind_elements = OrderedDict([('i_sid', i_sid), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/evpn/evpn-instances/evpn-instance/pbb/b-component/i-components/i-component/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State variables for the i-sid
  """
  __slots__ = ('_path_helper', '_extmethods', '__i_sid',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__i_sid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return ['network-instances', 'network-instance', 'evpn', 'evpn-instances', 'evpn-instance', 'pbb', 'b-component', 'i-components', 'i-component', 'state']

  def _get_i_sid(self):
    """
    Getter method for i_sid, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components/i_component/state/i_sid (uint32)

    YANG Description: Service Instance Identifier 24 bits and global within a PBB
network. I-SID defines the service instance that the frame should be
mapped to.
    """
    return self.__i_sid
      
  def _set_i_sid(self, v, load=False):
    """
    Setter method for i_sid, mapped from YANG variable /network_instances/network_instance/evpn/evpn_instances/evpn_instance/pbb/b_component/i_components/i_component/state/i_sid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_i_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_i_sid() directly.

    YANG Description: Service Instance Identifier 24 bits and global within a PBB
network. I-SID defines the service instance that the frame should be
mapped to.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """i_sid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__i_sid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_i_sid(self):
    self.__i_sid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['0..16777215']}), is_leaf=True, yang_name="i-sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  i_sid = __builtin__.property(_get_i_sid)


  _pyangbind_elements = OrderedDict([('i_sid', i_sid), ])



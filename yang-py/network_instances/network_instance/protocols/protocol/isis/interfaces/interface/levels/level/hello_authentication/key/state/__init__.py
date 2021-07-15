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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/hello-authentication/key/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication key state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__auth_password',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'hello-authentication', 'key', 'state']

  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)

    YANG Description: Authentication key string.
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.

    YANG Description: Authentication key string.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

  auth_password = __builtin__.property(_get_auth_password)


  _pyangbind_elements = OrderedDict([('auth_password', auth_password), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/hello-authentication/key/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication key state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__auth_password',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'hello-authentication', 'key', 'state']

  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)

    YANG Description: Authentication key string.
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.

    YANG Description: Authentication key string.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

  auth_password = __builtin__.property(_get_auth_password)


  _pyangbind_elements = OrderedDict([('auth_password', auth_password), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/hello-authentication/key/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication key state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__auth_password',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'hello-authentication', 'key', 'state']

  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)

    YANG Description: Authentication key string.
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.

    YANG Description: Authentication key string.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

  auth_password = __builtin__.property(_get_auth_password)


  _pyangbind_elements = OrderedDict([('auth_password', auth_password), ])


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/hello-authentication/key/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS authentication key state.
  """
  __slots__ = ('_path_helper', '_extmethods', '__auth_password',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

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
      return ['network-instances', 'network-instance', 'protocols', 'protocol', 'isis', 'interfaces', 'interface', 'levels', 'level', 'hello-authentication', 'key', 'state']

  def _get_auth_password(self):
    """
    Getter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)

    YANG Description: Authentication key string.
    """
    return self.__auth_password
      
  def _set_auth_password(self, v, load=False):
    """
    Setter method for auth_password, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/hello_authentication/key/state/auth_password (oc-types:routing-password)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_password() directly.

    YANG Description: Authentication key string.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_password must be of a type compatible with oc-types:routing-password""",
          'defined-type': "oc-types:routing-password",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)""",
        })

    self.__auth_password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_password(self):
    self.__auth_password = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="auth-password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-types:routing-password', is_config=False)

  auth_password = __builtin__.property(_get_auth_password)


  _pyangbind_elements = OrderedDict([('auth_password', auth_password), ])



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

from . import modules
from . import release_bundles
from . import feature_bundles
from . import implementations
class organization(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of organizations publishing YANG modules or
module bundles
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__type','__contact','__modules','__release_bundles','__feature_bundles','__implementations',)

  _yang_name = 'organization'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)
    self.__contact = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    self.__modules = YANGDynClass(base=modules.modules, is_container='container', yang_name="modules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    self.__release_bundles = YANGDynClass(base=release_bundles.release_bundles, is_container='container', yang_name="release-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    self.__feature_bundles = YANGDynClass(base=feature_bundles.feature_bundles, is_container='container', yang_name="feature-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    self.__implementations = YANGDynClass(base=implementations.implementations, is_container='container', yang_name="implementations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)

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
      return ['organizations', 'organization']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /organizations/organization/name (string)

    YANG Description: Name of the maintaining organization -- the name should be
supplied in the official format used by the organization.
Standards Body examples:
 IETF, IEEE, MEF, ONF, etc.
Commercial entity examples:
 AT&T, Facebook, <Vendor>
Name of industry forum examples:
 OpenConfig, OpenDaylight, ON.Lab
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /organizations/organization/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the maintaining organization -- the name should be
supplied in the official format used by the organization.
Standards Body examples:
 IETF, IEEE, MEF, ONF, etc.
Commercial entity examples:
 AT&T, Facebook, <Vendor>
Name of industry forum examples:
 OpenConfig, OpenDaylight, ON.Lab
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /organizations/organization/type (identityref)

    YANG Description: Type of the publishing organization
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /organizations/organization/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: Type of the publishing organization
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-module-catalog:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:STANDARDS': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDUSTRY': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:COMMERCIAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:INDIVIDUAL': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)


  def _get_contact(self):
    """
    Getter method for contact, mapped from YANG variable /organizations/organization/contact (string)

    YANG Description: Contact information for the publishing organization (web
site, email address, etc.)
    """
    return self.__contact
      
  def _set_contact(self, v, load=False):
    """
    Setter method for contact, mapped from YANG variable /organizations/organization/contact (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_contact is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_contact() directly.

    YANG Description: Contact information for the publishing organization (web
site, email address, etc.)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """contact must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)""",
        })

    self.__contact = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_contact(self):
    self.__contact = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)


  def _get_modules(self):
    """
    Getter method for modules, mapped from YANG variable /organizations/organization/modules (container)

    YANG Description: Modules published by this organization
    """
    return self.__modules
      
  def _set_modules(self, v, load=False):
    """
    Setter method for modules, mapped from YANG variable /organizations/organization/modules (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_modules is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_modules() directly.

    YANG Description: Modules published by this organization
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=modules.modules, is_container='container', yang_name="modules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """modules must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=modules.modules, is_container='container', yang_name="modules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)""",
        })

    self.__modules = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_modules(self):
    self.__modules = YANGDynClass(base=modules.modules, is_container='container', yang_name="modules", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)


  def _get_release_bundles(self):
    """
    Getter method for release_bundles, mapped from YANG variable /organizations/organization/release_bundles (container)

    YANG Description: List of release bundles
    """
    return self.__release_bundles
      
  def _set_release_bundles(self, v, load=False):
    """
    Setter method for release_bundles, mapped from YANG variable /organizations/organization/release_bundles (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_release_bundles is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_release_bundles() directly.

    YANG Description: List of release bundles
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=release_bundles.release_bundles, is_container='container', yang_name="release-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """release_bundles must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=release_bundles.release_bundles, is_container='container', yang_name="release-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)""",
        })

    self.__release_bundles = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_release_bundles(self):
    self.__release_bundles = YANGDynClass(base=release_bundles.release_bundles, is_container='container', yang_name="release-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)


  def _get_feature_bundles(self):
    """
    Getter method for feature_bundles, mapped from YANG variable /organizations/organization/feature_bundles (container)

    YANG Description: Enclosing container for the list of feature bundles
    """
    return self.__feature_bundles
      
  def _set_feature_bundles(self, v, load=False):
    """
    Setter method for feature_bundles, mapped from YANG variable /organizations/organization/feature_bundles (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_feature_bundles is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_feature_bundles() directly.

    YANG Description: Enclosing container for the list of feature bundles
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=feature_bundles.feature_bundles, is_container='container', yang_name="feature-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """feature_bundles must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=feature_bundles.feature_bundles, is_container='container', yang_name="feature-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)""",
        })

    self.__feature_bundles = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_feature_bundles(self):
    self.__feature_bundles = YANGDynClass(base=feature_bundles.feature_bundles, is_container='container', yang_name="feature-bundles", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)


  def _get_implementations(self):
    """
    Getter method for implementations, mapped from YANG variable /organizations/organization/implementations (container)

    YANG Description: Container for module implementation information
    """
    return self.__implementations
      
  def _set_implementations(self, v, load=False):
    """
    Setter method for implementations, mapped from YANG variable /organizations/organization/implementations (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_implementations is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_implementations() directly.

    YANG Description: Container for module implementation information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=implementations.implementations, is_container='container', yang_name="implementations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """implementations must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=implementations.implementations, is_container='container', yang_name="implementations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)""",
        })

    self.__implementations = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_implementations(self):
    self.__implementations = YANGDynClass(base=implementations.implementations, is_container='container', yang_name="implementations", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='container', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  type = __builtin__.property(_get_type, _set_type)
  contact = __builtin__.property(_get_contact, _set_contact)
  modules = __builtin__.property(_get_modules, _set_modules)
  release_bundles = __builtin__.property(_get_release_bundles, _set_release_bundles)
  feature_bundles = __builtin__.property(_get_feature_bundles, _set_feature_bundles)
  implementations = __builtin__.property(_get_implementations, _set_implementations)


  _pyangbind_elements = OrderedDict([('name', name), ('type', type), ('contact', contact), ('modules', modules), ('release_bundles', release_bundles), ('feature_bundles', feature_bundles), ('implementations', implementations), ])


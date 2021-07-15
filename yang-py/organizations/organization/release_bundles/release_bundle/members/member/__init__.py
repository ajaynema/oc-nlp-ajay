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

class member(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-module-catalog - based on the path /organizations/organization/release-bundles/release-bundle/members/member. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A set of modules or bundles which are part of the bundle
of models. For example, if 'ietf-yang-types' were to be
specified within the bundle, then this would refer to the
individual entry within the module catalogue. If the type
of the entry is set to bundle, then for example,
openconfig-bgp could be referenced - which itself consists
of separate modules.
  """
  __slots__ = ('_path_helper', '_extmethods', '__id','__type','__module','__release_bundle','__publisher','__compatible_versions',)

  _yang_name = 'member'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)
    self.__module = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__release_bundle = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="release-bundle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__publisher = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    self.__compatible_versions = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="compatible-versions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

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
      return ['organizations', 'organization', 'release-bundles', 'release-bundle', 'members', 'member']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/id (string)

    YANG Description: Identifier for the bundle member
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: Identifier for the bundle member
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='string', is_config=True)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/type (identityref)

    YANG Description: The type of member that is to be included within the
release bundle. Release bundles may include modules and
other release bundles.  Both member modules and member
bundles should specify the list of compatible versions.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type of member that is to be included within the
release bundle. Release bundles may include modules and
other release bundles.  Both member modules and member
bundles should specify the list of compatible versions.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with identityref""",
          'defined-type': "openconfig-module-catalog:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:MODULE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:RELEASE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}, 'oc-cat-types:FEATURE_BUNDLE': {'@module': 'openconfig-catalog-types', '@namespace': 'http://openconfig.net/yang/catalog-types'}},), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='identityref', is_config=True)


  def _get_module(self):
    """
    Getter method for module, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/module (leafref)

    YANG Description: Name of the module set which is included in this bundle -
for example, 'openconfig-bgp'
    """
    return self.__module
      
  def _set_module(self, v, load=False):
    """
    Setter method for module, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/module (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_module is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_module() directly.

    YANG Description: Name of the module set which is included in this bundle -
for example, 'openconfig-bgp'
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """module must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__module = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_module(self):
    self.__module = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_release_bundle(self):
    """
    Getter method for release_bundle, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/release_bundle (leafref)

    YANG Description: Name of the module set which is included in this bundle -
for example, 'openconfig-bgp'
    """
    return self.__release_bundle
      
  def _set_release_bundle(self, v, load=False):
    """
    Setter method for release_bundle, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/release_bundle (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_release_bundle is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_release_bundle() directly.

    YANG Description: Name of the module set which is included in this bundle -
for example, 'openconfig-bgp'
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="release-bundle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """release_bundle must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="release-bundle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__release_bundle = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_release_bundle(self):
    self.__release_bundle = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="release-bundle", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_publisher(self):
    """
    Getter method for publisher, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/publisher (leafref)

    YANG Description: Reference to the name of the publishing organization
    """
    return self.__publisher
      
  def _set_publisher(self, v, load=False):
    """
    Setter method for publisher, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/publisher (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_publisher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_publisher() directly.

    YANG Description: Reference to the name of the publishing organization
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=six.text_type, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """publisher must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)""",
        })

    self.__publisher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_publisher(self):
    self.__publisher = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="publisher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='leafref', is_config=True)


  def _get_compatible_versions(self):
    """
    Getter method for compatible_versions, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/compatible_versions (oc-cat-types:module-version-type)

    YANG Description: A list of semantic version specification of the versions
of the specified module or release bundle which are
compatible when building this version of the bundle.

Version specifications may be added when changes are made
to a module within a bundle, and this does not affect the
interaction between it and other modules. It is expected
that backwards compatible changes to an individual module or
member bundle do not affect the compatibility of that
with other members, and hence wildcard matches are allowed
within this list.
    """
    return self.__compatible_versions
      
  def _set_compatible_versions(self, v, load=False):
    """
    Setter method for compatible_versions, mapped from YANG variable /organizations/organization/release_bundles/release_bundle/members/member/compatible_versions (oc-cat-types:module-version-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_compatible_versions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_compatible_versions() directly.

    YANG Description: A list of semantic version specification of the versions
of the specified module or release bundle which are
compatible when building this version of the bundle.

Version specifications may be added when changes are made
to a module within a bundle, and this does not affect the
interaction between it and other modules. It is expected
that backwards compatible changes to an individual module or
member bundle do not affect the compatibility of that
with other members, and hence wildcard matches are allowed
within this list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="compatible-versions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """compatible_versions must be of a type compatible with oc-cat-types:module-version-type""",
          'defined-type': "oc-cat-types:module-version-type",
          'generated-type': """YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="compatible-versions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)""",
        })

    self.__compatible_versions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_compatible_versions(self):
    self.__compatible_versions = YANGDynClass(unique=True, base=TypedListType(allowed_type=six.text_type), is_leaf=False, yang_name="compatible-versions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/module-catalog', defining_module='openconfig-module-catalog', yang_type='oc-cat-types:module-version-type', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  type = __builtin__.property(_get_type, _set_type)
  module = __builtin__.property(_get_module, _set_module)
  release_bundle = __builtin__.property(_get_release_bundle, _set_release_bundle)
  publisher = __builtin__.property(_get_publisher, _set_publisher)
  compatible_versions = __builtin__.property(_get_compatible_versions, _set_compatible_versions)


  _pyangbind_elements = OrderedDict([('id', id), ('type', type), ('module', module), ('release_bundle', release_bundle), ('publisher', publisher), ('compatible_versions', compatible_versions), ])



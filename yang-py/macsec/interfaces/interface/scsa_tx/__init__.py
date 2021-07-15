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

from . import scsa_tx_
class scsa_tx(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-macsec - based on the path /macsec/interfaces/interface/scsa-tx. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for transmitted packets for Secure Channel and
Secure Association
  """
  __slots__ = ('_path_helper', '_extmethods', '__scsa_tx',)

  _yang_name = 'scsa-tx'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scsa_tx = YANGDynClass(base=YANGListType("sci_tx",scsa_tx_.scsa_tx, yang_name="scsa-tx", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sci-tx', extensions=None), is_container='list', yang_name="scsa-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='list', is_config=False)

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
      return ['macsec', 'interfaces', 'interface', 'scsa-tx']

  def _get_scsa_tx(self):
    """
    Getter method for scsa_tx, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx (list)

    YANG Description: TX Secure Channel and Secure Association Statistics
    """
    return self.__scsa_tx
      
  def _set_scsa_tx(self, v, load=False):
    """
    Setter method for scsa_tx, mapped from YANG variable /macsec/interfaces/interface/scsa_tx/scsa_tx (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scsa_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scsa_tx() directly.

    YANG Description: TX Secure Channel and Secure Association Statistics
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sci_tx",scsa_tx_.scsa_tx, yang_name="scsa-tx", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sci-tx', extensions=None), is_container='list', yang_name="scsa-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scsa_tx must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sci_tx",scsa_tx_.scsa_tx, yang_name="scsa-tx", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sci-tx', extensions=None), is_container='list', yang_name="scsa-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='list', is_config=False)""",
        })

    self.__scsa_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scsa_tx(self):
    self.__scsa_tx = YANGDynClass(base=YANGListType("sci_tx",scsa_tx_.scsa_tx, yang_name="scsa-tx", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sci-tx', extensions=None), is_container='list', yang_name="scsa-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/macsec', defining_module='openconfig-macsec', yang_type='list', is_config=False)

  scsa_tx = __builtin__.property(_get_scsa_tx)


  _pyangbind_elements = OrderedDict([('scsa_tx', scsa_tx), ])


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

from . import backplane_facing_capacity
from . import pipeline_counters
class integrated_circuit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/integrated-circuit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Data for chip components, such as ASIC, NPUs, etc.
  """
  __slots__ = ('_path_helper', '_extmethods', '__backplane_facing_capacity','__pipeline_counters',)

  _yang_name = 'integrated-circuit'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__backplane_facing_capacity = YANGDynClass(base=backplane_facing_capacity.backplane_facing_capacity, is_container='container', yang_name="backplane-facing-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='container', is_config=True)
    self.__pipeline_counters = YANGDynClass(base=pipeline_counters.pipeline_counters, is_container='container', yang_name="pipeline-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='container', is_config=True)

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
      return ['components', 'component', 'integrated-circuit']

  def _get_backplane_facing_capacity(self):
    """
    Getter method for backplane_facing_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity (container)

    YANG Description: This container allows a particular INTEGRATED_CIRCUIT to report its
available backplane-facing bandwidth. Wheere an integrated circuit is connected
by one or more links to the system's backplane, the capacity is the total cross-
sectional bandwidfth available from the input ports of the integrated circuit
across the fabric. The capacity should also reflect the operational status of
the links.
    """
    return self.__backplane_facing_capacity
      
  def _set_backplane_facing_capacity(self, v, load=False):
    """
    Setter method for backplane_facing_capacity, mapped from YANG variable /components/component/integrated_circuit/backplane_facing_capacity (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_backplane_facing_capacity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_backplane_facing_capacity() directly.

    YANG Description: This container allows a particular INTEGRATED_CIRCUIT to report its
available backplane-facing bandwidth. Wheere an integrated circuit is connected
by one or more links to the system's backplane, the capacity is the total cross-
sectional bandwidfth available from the input ports of the integrated circuit
across the fabric. The capacity should also reflect the operational status of
the links.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=backplane_facing_capacity.backplane_facing_capacity, is_container='container', yang_name="backplane-facing-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """backplane_facing_capacity must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=backplane_facing_capacity.backplane_facing_capacity, is_container='container', yang_name="backplane-facing-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='container', is_config=True)""",
        })

    self.__backplane_facing_capacity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_backplane_facing_capacity(self):
    self.__backplane_facing_capacity = YANGDynClass(base=backplane_facing_capacity.backplane_facing_capacity, is_container='container', yang_name="backplane-facing-capacity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform/integrated-circuit', defining_module='openconfig-platform-integrated-circuit', yang_type='container', is_config=True)


  def _get_pipeline_counters(self):
    """
    Getter method for pipeline_counters, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters (container)

    YANG Description: Top-level container for the packet, drop, and error counters for the
five NPU sub-blocks.
    """
    return self.__pipeline_counters
      
  def _set_pipeline_counters(self, v, load=False):
    """
    Setter method for pipeline_counters, mapped from YANG variable /components/component/integrated_circuit/pipeline_counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pipeline_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pipeline_counters() directly.

    YANG Description: Top-level container for the packet, drop, and error counters for the
five NPU sub-blocks.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=pipeline_counters.pipeline_counters, is_container='container', yang_name="pipeline-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pipeline_counters must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pipeline_counters.pipeline_counters, is_container='container', yang_name="pipeline-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='container', is_config=True)""",
        })

    self.__pipeline_counters = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pipeline_counters(self):
    self.__pipeline_counters = YANGDynClass(base=pipeline_counters.pipeline_counters, is_container='container', yang_name="pipeline-counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform-pipeline-counters', defining_module='openconfig-platform-pipeline-counters', yang_type='container', is_config=True)

  backplane_facing_capacity = __builtin__.property(_get_backplane_facing_capacity, _set_backplane_facing_capacity)
  pipeline_counters = __builtin__.property(_get_pipeline_counters, _set_pipeline_counters)


  _pyangbind_elements = OrderedDict([('backplane_facing_capacity', backplane_facing_capacity), ('pipeline_counters', pipeline_counters), ])



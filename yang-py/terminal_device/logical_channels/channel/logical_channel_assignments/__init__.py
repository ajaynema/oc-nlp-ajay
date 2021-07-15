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

from . import assignment
class logical_channel_assignments(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-terminal-device - based on the path /terminal-device/logical-channels/channel/logical-channel-assignments. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for tributary assignments
  """
  __slots__ = ('_path_helper', '_extmethods', '__assignment',)

  _yang_name = 'logical-channel-assignments'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__assignment = YANGDynClass(base=YANGListType("index",assignment.assignment, yang_name="assignment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="assignment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=True)

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
      return ['terminal-device', 'logical-channels', 'channel', 'logical-channel-assignments']

  def _get_assignment(self):
    """
    Getter method for assignment, mapped from YANG variable /terminal_device/logical_channels/channel/logical_channel_assignments/assignment (list)

    YANG Description: Logical channel elements may be assigned directly to
optical channels for line-side transmission, or can be
further groomed into additional stages of logical channel
elements.  The grooming can multiplex (i.e., split the
current element into multiple elements in the subsequent
stage) or de-multiplex (i.e., combine the current element
with other elements into the same element in the subsequent
stage) logical elements in each stage.

Note that to support the ability to groom the logical
elements, the list of logical channel elements should be
populated with an entry for the logical elements at
each stage, starting with the initial assignment from the
respective client physical port.

Each logical element assignment consists of a pointer to
an element in the next stage, or to an optical channel,
along with a bandwidth allocation for the corresponding
assignment (e.g., to split or combine signal).
    """
    return self.__assignment
      
  def _set_assignment(self, v, load=False):
    """
    Setter method for assignment, mapped from YANG variable /terminal_device/logical_channels/channel/logical_channel_assignments/assignment (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_assignment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_assignment() directly.

    YANG Description: Logical channel elements may be assigned directly to
optical channels for line-side transmission, or can be
further groomed into additional stages of logical channel
elements.  The grooming can multiplex (i.e., split the
current element into multiple elements in the subsequent
stage) or de-multiplex (i.e., combine the current element
with other elements into the same element in the subsequent
stage) logical elements in each stage.

Note that to support the ability to groom the logical
elements, the list of logical channel elements should be
populated with an entry for the logical elements at
each stage, starting with the initial assignment from the
respective client physical port.

Each logical element assignment consists of a pointer to
an element in the next stage, or to an optical channel,
along with a bandwidth allocation for the corresponding
assignment (e.g., to split or combine signal).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("index",assignment.assignment, yang_name="assignment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="assignment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """assignment must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("index",assignment.assignment, yang_name="assignment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="assignment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=True)""",
        })

    self.__assignment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_assignment(self):
    self.__assignment = YANGDynClass(base=YANGListType("index",assignment.assignment, yang_name="assignment", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='index', extensions=None), is_container='list', yang_name="assignment", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/terminal-device', defining_module='openconfig-terminal-device', yang_type='list', is_config=True)

  assignment = __builtin__.property(_get_assignment, _set_assignment)


  _pyangbind_elements = OrderedDict([('assignment', assignment), ])


import copy


class helper_type_general: 
  """This is a set of general type helpers"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  def is_integer(self, n):
    try:
      if(self.is_numeric(n)):
        float(n)
    except ValueError:
      return False
    else:
      return float(n).is_integer()
  
  def is_numeric(self, n, *args, **kwargs):
    try:
      return str(n).isnumeric()
    except:
      return False
  
  def is_type(self, obj, type_check, *args, **kwargs):
    if isinstance(type_check, list):
      for check in type_check:
        if self.is_type(obj= obj, type_check= check):
          return True
      return False
    try:
      return isinstance(obj, type_check)
    except:
      return type(obj) == type_check
  
  def if_null_default(self, check_val, default_val, enforce_type = None, *args, **kwargs):
    if enforce_type is not None and not self.is_type(check_val, enforce_type):
      return default_val

    if check_val is None:
      return default_val
    
    return check_val
  
  def copy_object(cls, object_copy, deep_copy = True, *args, **kwargs):
    if object_copy is None:
      return None

    if deep_copy:
      return copy.deepcopy(object_copy)
    
    return copy.copy(object_copy)
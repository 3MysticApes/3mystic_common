from base_class.base_common import base


class exception_base(base): 
  """This is a set of library wrappers to help create a cmdb"""

  def __init__(self, exception_type = "generic", *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self._exception_type = exception_type.lower()

  def exception(self, message, name = None, *args, **kwargs):
    if name is not None and self._exception_type != "generic":
      return Exception(f"{self._exception_type}: {name}\n{message}")
    
    if name is not None:
      return Exception(f"{name}\n{message}")
    
    return Exception(message)

  def not_implemented(self, message, name = None, *args, **kwargs):
    if name is not None and self._exception_type != "generic":
      return NotImplementedError(f"{self._exception_type}: {name}\n{message}")
    
    if name is not None:
      return NotImplementedError(f"{name}\n{message}")
    
    return NotImplementedError(message)
  
  def type_error(self, message, name = None, *args, **kwargs):
    if name is not None and self._exception_type != "generic":
      return TypeError(f"{self._exception_type}: {name}\n{message}")
    
    if name is not None:
      return TypeError(f"{name}\n{message}")
    
    return TypeError(message)
  
  def key_error(self, message, name = None, *args, **kwargs):
    if name is not None and self._exception_type != "generic":
      return KeyError(f"{self._exception_type}: {name}\n{message}")
    
    if name is not None:
      return KeyError(f"{name}\n{message}")
    
    return KeyError(message)
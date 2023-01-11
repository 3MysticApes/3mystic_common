

class helper_type_bool: 
  """This is a set of library wrappers to help around expending bool libary"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  def is_true(self, item):
    if self._main_reference.helper_type().general().is_type(item, bool):
      return item == True
    
    if self._main_reference.helper_type().general().is_type(item, int):
      return item > 0
    
    if not self._main_reference.helper_type().general().is_type(item, str):
      raise Exception(f"unknown boolean compare")

    item = item.lower()
    if item in ["true", "t", "yes", "y", "1"]:
      return True
    
    return False
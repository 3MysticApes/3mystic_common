from base_class.base_common import base


class helper_type_bool(base): 
  """This is a set of library wrappers to help around expending bool libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  def is_true(self, check_item):
    if self._main_reference.helper_type().general().is_type(check_item, bool):
      return check_item == True
    
    if self._main_reference.helper_type().general().is_type(check_item, int):
      return check_item > 0
    
    if not self._main_reference.helper_type().general().is_type(check_item, str):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        name = "check_item",
        message = f"Unknown type for comparison ({type(check_item)})"
      )

    item = item.lower()
    if item in ["true", "t", "yes", "y", "1"]:
      return True
    
    return False
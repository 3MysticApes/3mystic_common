from threemystic_common.base_class.base_common import base


class helper_type_bool(base): 
  """This is a set of library wrappers to help around expending bool libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_type_bool", *args, **kwargs)
  
  def is_true_values(self, *args, **kwargs):
    return ["true", "t", "yes", "y", "1"]

  def is_true(self, check_value, *args, **kwargs):
    if self._main_reference.helper_type().general().is_type(check_value, bool):
      return check_value == True
    
    if self._main_reference.helper_type().general().is_type(check_value, int):
      return check_value > 0
    
    if not self._main_reference.helper_type().general().is_type(check_value, str):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "check_value",
        message = f"Unknown type for comparison ({type(check_value)})"
      )

    check_value = check_value.lower()
    if check_value in self.is_true_values():
      return True
    
    return False
from pathlib import Path  
from base_class.base_common import base

class helper_path(base): 
  """This is a set of library wrappers to help around expending json libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_path", *args, **kwargs)
  
  # report_directory
  def get(self, path = None, *args, **kwargs)->Path:
    if not self._main_reference.helper_type().general().is_type(path, str):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "path",
        message = f"Unknown type ({type(path)})"
      )
    
    if self._main_reference.helper_type().string().is_null_or_whitespace(path):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "path",
        message = f"path is either None or an empty string"
      )
    
    return Path(path)
  
  def expandpath_user(self, path) -> Path:
    return self.get(path).expanduser()
  
  
    

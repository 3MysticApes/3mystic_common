from base_class.base_common import base


class helper_type_string(base): 
  """This is a set of library wrappers to help around expending string libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  # isNullOrWhiteSpace
  def is_null_or_whitespace(self, strValue, *args, **kwargs):
    if not strValue:
      return True
    
    if not str(strValue).strip():
      return True
    
    return False
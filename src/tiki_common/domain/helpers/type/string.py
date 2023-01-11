
class helper_type_string: 
  """This is a set of library wrappers to help around expending string libary"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  # isNullOrWhiteSpace
  def is_null_or_whitespace(self, strValue, *args, **kwargs):
    if not strValue:
      return True
    
    if not str(strValue).strip():
      return True
    
    return False
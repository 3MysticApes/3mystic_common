from base_class.base_common import base
import re


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
  
  def split_string(self, string_value, trim_data = True, remove_empty = True, split_value = "[,;]"):
    split_data = re.split(split_value, string_value)
    if not remove_empty:
      return split_data
      
    if not trim_data:
      return [item for item in split_data if not self.is_null_or_whitespace(item)]

    return [item.strip() for item in split_data if not self.is_null_or_whitespace(item)]
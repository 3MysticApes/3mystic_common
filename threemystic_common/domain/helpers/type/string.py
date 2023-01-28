from threemystic_common.base_class.base_common import base


class helper_type_string(base): 
  """This is a set of library wrappers to help around expending string libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_type_string", *args, **kwargs)
  
  def trim(self, string_value, trim_chars = None, *args, **kwargs):
    if self.is_null_or_whitespace(string_value= string_value):
      return ""
    
    return string_value.strip() if trim_chars is None else string_value.strip(trim_chars)


  def set_case(self, string_value, case = "upper", *args, **kwargs):
    if self.is_null_or_whitespace(string_value= string_value):
      return string_value
    
    valid_case_options = ["upper", "lower", "camel", "pascal"]
    case = self.trim(string_value=case).lower()
    if case not in valid_case_options:
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "case",
        message = f"case type is unknown. valid options: {valid_case_options}"
      )
    
    if case == "upper":
      return string_value.upper()
    
    if case == "lower":
      return string_value.lower()
    
    if case == "camel":
      str = "".join([word[0].upper() + word[1:] for word in self.split(string_value= string_value, separator="\s")])
      return str[0].lower() + str[1:]
    
    if case == "pascal":
      return "".join([word[0].upper() + word[1:] for word in self.split(string_value= string_value, separator="\s")])
    
    if case == "snake":
      return "_".join([word[0].lower() + word[1:] for word in self.split(string_value= string_value, separator="\s")])
    
  
  # isNullOrWhiteSpace
  def is_null_or_whitespace(self, string_value, *args, **kwargs):
    if not string_value:
      return True
    
    if not str(string_value).strip():
      return True
    
    return False
  
  # split_string
  def split(self, string_value, trim_data = True, remove_empty = True, separator = "[,;]", regex_split = True, *args, **kwargs):
    if regex_split:
      return self._main_reference.helper_type().regex().split(
        string_value= string_value,
        trim_data= trim_data,
        remove_empty= remove_empty,
        separator= separator
      )
    
    split_data = string_value.split(separator)
    
    if not remove_empty:
      return split_data if not trim_data else [str(item).strip() if item is not None else item for item in split_data ]
      
    if not trim_data:
      return [item for item in split_data if not self.is_null_or_whitespace(item)]

    return [item.strip() for item in split_data if not self.is_null_or_whitespace(item)]
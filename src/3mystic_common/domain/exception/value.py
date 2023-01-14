import sys

from domain.exception.base_class.base import exception_base as base


class exception_value(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    super().__init(
      main_reference= main_reference, *args, **kwargs
    )
  
  def exception(self, exception_message, variable_name, variable_value, is_argument = True,  *args, **kwargs):
    if is_argument:
      return ValueError(f"type: argument\nargument: {variable_name}\nvalue: {argument_value}\n{exception_message}")
    return ValueError(f"type: variable\nvariable: {variable_name}\nvalue: {variable_value}\n{exception_message}")
  
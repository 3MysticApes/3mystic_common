import sys

from domain.exception.base_class.base import exception_base as base


class exception_argument(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init(
      exception_type = "argument", *args, **kwargs
    )
  
  
  
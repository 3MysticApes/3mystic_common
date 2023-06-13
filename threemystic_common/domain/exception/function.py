import sys

from threemystic_common.domain.exception.base_class.base import exception_base as base


class exception_function(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(
      exception_type = "function", *args, **kwargs
    )
  
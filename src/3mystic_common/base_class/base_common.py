from base_class.base import base as base_main

class base(base_main): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, main_reference, logger_name, *args, **kwargs) -> None:
    self._main_reference= main_reference
    self._logger_name = logger_name

  

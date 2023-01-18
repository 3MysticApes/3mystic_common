import abc

class base(abc.ABC): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, main_reference, logger_name, *args, **kwargs) -> None:
    self._main_reference= main_reference
    self.logger = self._main_reference.logger.getChild(logger_name)
import abc

class base(abc.ABC): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__()
  
  def get_logger(self):
    if not hasattr(self, "_logger"):
      return self._logger
    
    if not hasattr(self, "_logger_name"):
      self._logger = self._main_reference.logger.getChild(self._logger_name)
      return self.get_logger()
    
    return None
    

  def _unset(self, attribute, *args, **kwargs):
      if not hasattr(self, attribute):
        return

      delattr(self, attribute)
      
import abc

class base(abc.ABC): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, main_reference, logger_name, *args, **kwargs) -> None:
    pass
  
  def _unset(self, attribute, *args, **kwargs):
      if not hasattr(self, attribute):
        return

      delattr(self, attribute)
      
import logging
import sys


class helper_type_logging: 
  """This is a set of library wrappers to help around expending dictionary libary"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  def get_child_logger(cls, child_logger_name, logger: logging.Logger = None):
    if logger is None:
      import logging
      logger = logging.getLogger()
      
    return logger.getChild(child_logger_name)

  def set_logger_level(cls, logger: logging.Logger, level):
    logger.setLevel(level= level)

  def add_handler_logger_stdout(cls, logger: logging.Logger, level):
    handler = logging.StreamHandler(sys.stdout)
    handler.set_name(f"Log STDOUT - {level}")
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
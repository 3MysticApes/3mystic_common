import logging
import sys
from base_class.base_common import base



class helper_type_logging(base): 
  """This is a set of library wrappers to help around expending dictionary libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  def get_child_logger(cls, child_logger_name, logger: logging.Logger = None, *args, **kwargs):
    if logger is None:
      import logging
      logger = logging.getLogger()
      
    return logger.getChild(child_logger_name)

  def set_logger_level(cls, logger: logging.Logger, level, *args, **kwargs):
    logger.setLevel(level= level)

  def add_handler_logger_stdout(cls, logger: logging.Logger, level, *args, **kwargs):
    handler = logging.StreamHandler(sys.stdout)
    handler.set_name(f"Log STDOUT - {level}")
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
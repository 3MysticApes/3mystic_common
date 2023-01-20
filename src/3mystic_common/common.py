class common: 
  """This is a common set of methods and libraries"""

  class emptyclass(object):   
    """This is a class designed for dynamic creation""" 
    def __init__(self):
      pass

  def __init__(self, logger = None, config_path = None, *args, **kwargs) -> None: 
    self.logger = self.helper_type().logging().get_child_logger(
      child_logger_name= "common_lib_logger",
      logger= logger
    )
    self.update_configuration(config_path= config_path)
    
  def update_configuration(self, config_path, merge_existing = False, *args, **kwargs):
    if self.helper_type().string().is_null_or_whitespace(config_path):
      return
    
    self._config_data = {}
    # Add load data code by path

  def get_configuration(self, *args, **kwargs):
    return self._config_data
  
  def exception(self, *args, **kwargs):
    if hasattr(self, "_exception"):
      return self._monitoring
    
    from domain.exception.common import exception_common as exception        
    self._monitoring = exception(
      main_reference= self, *args, **kwargs
    )
    return self.exception(*args, **kwargs)

  def app_monitoring(self, *args, **kwargs):
    if hasattr(self, "_monitoring"):
      return self._monitoring
    
    from domain.app_monitoring.common import \
        app_monitoring_common as app_monitoring
    self._monitoring = app_monitoring(
      main_reference= self, *args, **kwargs
    )
    return self.performance_monitoring(*args, **kwargs)
  
  def encryption(self, *args, **kwargs):
    if hasattr(self, "_encryption"):
      return self._helper_dictionary
    
    from domain.encryption import encryption_common as encryption
    self._helper_dictionary = encryption(
      main_reference= self, *args, **kwargs
    )
    return self.encryption(*args, **kwargs)
  
  def cmdb(self, *args, **kwargs):
    if hasattr(self, "_cmdb"):
      return self._cmdb
    
    from domain.cmdb.common import cmdb_common as cmdb
    self._cmdb = cmdb(
      main_reference= self, *args, **kwargs
    )
    return self.helper_cmdb(*args, **kwargs)
  
  def helper_app(self, *args, **kwargs):
    if hasattr(self, "_helper_app"):
      return self._helper_app
    
    from domain.helpers.app import helper_app as helper
    self._helper_app = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_app(*args, **kwargs)
  
  def helper_path(self, *args, **kwargs):
    if hasattr(self, "_helper_path"):
      return self._helper_path
    
    from domain.helpers.json import helper_path as helper
    self._helper_path = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_path(*args, **kwargs)
  
  def helper_json(self, *args, **kwargs):
    if hasattr(self, "_helper_json"):
      return self._helper_json
    
    from domain.helpers.json import helper_json as helper
    self._helper_json = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_json(*args, **kwargs)
  
  def helper_parallel_processing(self, *args, **kwargs):
    if hasattr(self, "_helper_parallel_processing"):
      return self._helper_parallel_processing
    
    from domain.helpers.parallel_processing import helper_parallel_processing as helper
    self._helper_parallel_processing = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_json(*args, **kwargs)
  
  def helper_config(self, *args, **kwargs):
    if hasattr(self, "_helper_config"):
      return self._helper_json
    
    from domain.helpers.config import helper_config as helper
    self._helper_config = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_config(*args, **kwargs)
  
  def helper_type(self, *args, **kwargs):
    if hasattr(self, "_helper_type"):
      return self._helper_dictionary
    
    from domain.helpers.type.common import helper_type_common as helper
    self._helper_dictionary = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_type(*args, **kwargs)
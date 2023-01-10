class common_main: 
  """This is a common set of methods and libraries"""

  class emptyclass(object):   
    """This is a class designed for dynamic creation""" 
    def __init__(self):
      pass

  def __init__(self, logger = None, *args, **kwargs) -> None: 
    self.logger = self.helper_type().logging().get_child_logger(
      child_logger_name= "common_lib_logger",
      logger= logger
    )
    

  
  def app_monitoring(self, *args, **kwargs):
    if not hasattr(self, "_monitoring"):
      return self._monitoring
    
    from domain.app_monitoring.common import \
        app_monitoring_common as app_monitoring
    self._monitoring = app_monitoring(
      main_reference= self
    )
    return self.performance_monitoring(*args, **kwargs)
  
  def encryption(self, *args, **kwargs):
    if not hasattr(self, "_encryption"):
      return self._helper_dictionary
    
    from domain.encryption import encryption_common as encryption
    self._helper_dictionary = encryption(
      main_reference= self
    )
    return self.encryption(*args, **kwargs)
  
  def helper_cmdb(self, *args, **kwargs):
    if not hasattr(self, "_helper_cmdb"):
      return self._helper_cmdb
    
    from domain.helpers.cmdb import helper_cmdb as helper
    self._helper_cmdb = helper(
      main_reference= self
    )
    return self.helper_cmdb(*args, **kwargs)
  
  def helper_app(self, *args, **kwargs):
    if not hasattr(self, "_helper_app"):
      return self._helper_app
    
    from domain.helpers.app import helper_app as helper
    self._helper_app = helper(
      main_reference= self
    )
    return self.helper_app(*args, **kwargs)
  
  def helper_json(self, *args, **kwargs):
    if not hasattr(self, "_helper_json"):
      return self._helper_json
    
    from domain.helpers.json import helper_json as helper
    self._helper_json = helper(
      main_reference= self
    )
    return self.helper_json(*args, **kwargs)
  
  def helper_type(self, *args, **kwargs):
    if not hasattr(self, "_helper_type"):
      return self._helper_dictionary
    
    from domain.helpers.type.common import helper_type_common as helper
    self._helper_dictionary = helper(
      main_reference= self
    )
    return self.helper_type(*args, **kwargs)
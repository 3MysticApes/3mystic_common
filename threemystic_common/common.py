from threemystic_common.base_class.base import base


class common(base): 
  """This is a common set of methods and libraries"""

  class emptyclass(object):   
    """This is a class designed for dynamic creation""" 
    def __init__(self):
      pass

  def __init__(self, logger = None, config_path = None, *args, **kwargs) -> None:     
    super().__init__(*args, **kwargs)
    self._logger = self.helper_type().logging().get_child_logger(
      child_logger_name= "3mystic_common_lib_logger",
      logger= logger
    )
    self.update_configuration(config_path= config_path)
  
  def get_threemystic_config_path(self, *args, **kwargs):
    general_path = self.helper_path().expandpath_user(
      path= "~/.3mystic"
    )
    if not general_path.exists():
      general_path.mkdir(parents= True)
    
    return general_path

  def version(self):
    if hasattr(self, "_version"):
      return self._version
    import threemystic_common.__version__ as __version__
    self._version = __version__.__version__
    return self.version()

    
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
    
    from threemystic_common.domain.exception.common import exception_common as exception        
    self._monitoring = exception(
      main_reference= self, *args, **kwargs
    )
    return self.exception(*args, **kwargs)

  def app_monitoring(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_exception")
      return
    
    if hasattr(self, "_monitoring"):
      return self._monitoring
    
    from threemystic_common.domain.app_monitoring.common import \
        app_monitoring_common as app_monitoring
    self._monitoring = app_monitoring(
      main_reference= self, *args, **kwargs
    )
    return self.performance_monitoring(*args, **kwargs)

  def generate_data(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_generate_data")
      return
    
    if hasattr(self, "_generate_data"):
      return self._generate_data
    
    from threemystic_common.domain.generate_data.generate import generate_data as generate
    self._generate_data = generate(
      main_reference= self, *args, **kwargs
    )
    return self.generate_data(*args, **kwargs)
  
  def encryption(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_encryption")
      return
    
    if hasattr(self, "_encryption"):
      return self._helper_dictionary
    
    from threemystic_common.domain.encryption import encryption_common as encryption
    self._helper_dictionary = encryption(
      main_reference= self, *args, **kwargs
    )
    return self.encryption(*args, **kwargs)
  
  def cmdb(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_cmdb")
      return
    
    if hasattr(self, "_cmdb"):
      return self._cmdb
    
    from threemystic_common.domain.cmdb.common import cmdb_common as cmdb
    self._cmdb = cmdb(
      main_reference= self, *args, **kwargs
    )
    return self.helper_cmdb(*args, **kwargs)
  
  def helper_app(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_app")
      return
    
    if hasattr(self, "_helper_app"):
      return self._helper_app
    
    from threemystic_common.domain.helpers.app import helper_app as helper
    self._helper_app = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_app(*args, **kwargs)
  
  def helper_path(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_path")
      return
    
    if hasattr(self, "_helper_path"):
      return self._helper_path
    
    from threemystic_common.domain.helpers.path import helper_path as helper
    self._helper_path = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_path(*args, **kwargs)
  
  def helper_json(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_json")
      return
    
    if hasattr(self, "_helper_json"):
      return self._helper_json
    
    from threemystic_common.domain.helpers.json import helper_json as helper
    self._helper_json = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_json(*args, **kwargs)
  
  def helper_yaml(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_yaml")
      return
    
    if hasattr(self, "_helper_yaml"):
      return self._helper_yaml
    
    from threemystic_common.domain.helpers.yaml import helper_yaml as helper
    self._helper_yaml = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_yaml(*args, **kwargs)
  
  def helper_parallel_processing(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_parallel_processing")
      return
    
    if hasattr(self, "_helper_parallel_processing"):
      return self._helper_parallel_processing
    
    from threemystic_common.domain.helpers.parallel_processing import helper_parallel_processing as helper
    self._helper_parallel_processing = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_json(*args, **kwargs)
  
  def helper_config(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_config")
      return
    
    if hasattr(self, "_helper_config"):
      return self._helper_config
    
    from threemystic_common.domain.helpers.config import helper_config as helper
    self._helper_config = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_config(*args, **kwargs)
  
  def helper_type(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_helper_type")
      return
    
    if hasattr(self, "_helper_type"):
      return self._helper_type
    
    from threemystic_common.domain.helpers.type.common import helper_type_common as helper
    self._helper_type = helper(
      main_reference= self, *args, **kwargs
    )
    return self.helper_type(*args, **kwargs)

from threemystic_common.base_class.base_common import base


class helper_type_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_type", *args, **kwargs)
  
  def logging(self, *args, **kwargs):    
    if hasattr(self, "_logging"):
      return self._logging
    
    from threemystic_common.domain.helpers.type.logging import helper_type_logging as helper
    self._logging = helper(
      main_reference= self._main_reference
    )
    return self.logging(*args, **kwargs)
  
  def general(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_general")
      return

    if hasattr(self, "_general"):
      return self._general
    
    from threemystic_common.domain.helpers.type.general import helper_type_general as helper
    self._general = helper(
      main_reference= self._main_reference
    )
    return self.general(*args, **kwargs)

  def string(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_string")
      return      
    
    if hasattr(self, "_string"):
      return self._string
    
    from threemystic_common.domain.helpers.type.string import helper_type_string as helper
    self._string = helper(
      main_reference= self._main_reference
    )
    return self.string(*args, **kwargs)
  
  def dictionary(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_dictionary")
      return      
    
    if hasattr(self, "_dictionary"):
      return self._dictionary
    
    from threemystic_common.domain.helpers.type.dictionary import helper_type_dictionary as helper
    self._dictionary = helper(
      main_reference= self._main_reference
    )
    return self.dictionary(*args, **kwargs)
  
  def list(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_list")
      return
    
    if hasattr(self, "_list"):
      return self._list
    
    from threemystic_common.domain.helpers.type.list import helper_type_list as helper
    self._list = helper(
      main_reference= self._main_reference
    )
    return self.list(*args, **kwargs)
  
  def datetime(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_datetime")
      return
      
    if hasattr(self, "_datetime"):
      return self._datetime
    
    from threemystic_common.domain.helpers.type.datetime import helper_type_datetime as helper
    self._datetime = helper(
      main_reference= self._main_reference
    )
    return self.datetime(*args, **kwargs)
  
  def bool(self, unset = False, *args, **kwargs):
    if(unset):
      self._unset("_bool")
      return
      
    if hasattr(self, "_bool"):
      return self._bool
    
    from threemystic_common.domain.helpers.type.bool import helper_type_bool as helper
    self._bool = helper(
      main_reference= self._main_reference
    )
    return self.bool(*args, **kwargs)
  
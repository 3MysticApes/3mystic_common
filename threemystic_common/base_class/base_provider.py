from threemystic_common.base_class.base_general import base as main_base

class base(main_base): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, provider, *args, **kwargs) -> None:
    if not "main_reference" in kwargs:
      kwargs["main_reference"] = None

    
    super().__init__(*args, **kwargs)
    self.__provider = provider

  @classmethod
  def get_supported_providers(cls, *args, **kwargs):
    return ["aws", "azure"]
  
  @classmethod
  def get_supported_output_format(self, *args, **kwargs):
    return ["json", "yaml"]
  
  def get_provider(self, *args, **kwargs):
    return self.__provider
  
  
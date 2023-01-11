from domain.cmdb.base_class.base import cmdb_base as base


class cmdb_azure(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    super().__init(
      main_reference= main_reference, *args, **kwargs
    )
  
  def get_source(self, *args, **kwargs):
    return "azure"
    
    
    
  
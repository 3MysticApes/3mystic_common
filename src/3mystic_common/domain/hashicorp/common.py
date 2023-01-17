from base_class.base_common import base


class hashi_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  
  def vault(self, *args, **kwargs):
    if hasattr(self, "_hashi_vault"):
      return self._hashi_vault
    
    from domain.hashicorp.vault import hashi_vault as hashi
    self._hashi_vault = hashi(
      main_reference= self, *args, **kwargs
    )
    return self.vault(*args, **kwargs)
  
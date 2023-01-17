from base_class.base_common import base

class encryption_hash(base): 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self._hash_method = self.__get_hash_method(*args, **kwargs)
  
  # bring in the hasi vault helper I did for python
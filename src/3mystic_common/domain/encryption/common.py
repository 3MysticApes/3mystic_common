from base_class.base_common import base


class encryption_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  
  def hash(self, hash_method, *args, **kwargs):
    if not hasattr(self, "_hash_methods"):
      if self._hash_methods.get(hash_method.lower()) is not None:
        return self._hash_methods[hash_method.lower()]
    
    if not hasattr(self, "_hash"):
      from domain.encryption.hash import encryption_hash as encryption
      self._hash = encryption
      self._hash_methods = {}
    
    self._hash_methods[hash_method.lower()] = self._hash(
      main_reference= self._main_reference,
      hash_method= hash_method
    )
    return self.hash(*args, **kwargs)
  
from base_class.base_common import base


class encryption_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= "encryption", *args, **kwargs)
  
  
  def hash(self, hash_method, *args, **kwargs):
    hash_method = hash_method.lower() if hash_method is not None else ""
    if not hasattr(self, "_hash_method"):
      if self._hash_method.get(hash_method) is not None:
        return self._hash_method[hash_method]
    
    if not hasattr(self, "_hash"):
      from domain.encryption.hash import encryption_hash as encryption
      self._hash = encryption
      self._hash_method = {}
    
    self._hash_method[hash_method] = self._hash(
      main_reference= self._main_reference,
      hash_method= hash_method
    )
    return self.hash(*args, **kwargs)
  
class encryption_hash: 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
    self._hash_method = self.__get_hash_method(*args, **kwargs)
  
  def __get_hash_method(self, hash_method):
    if self._main_reference.helper_type().general().is_null_or_whitespace(hash_method):
      raise Exception("No Hash Method Provided")

    if hash_method.lower() == "sha1":
      from hashlib import sha1
      return sha1
    
    raise Exception(f"Unknown Hash Method Provided: {hash_method}")
    

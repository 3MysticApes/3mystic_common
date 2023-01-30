from threemystic_common.base_class.base_common import base


class helper_type_list(base): 
  """This is a set of library wrappers to help around expending list libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_type_list", *args, **kwargs)
  
  def unique_list(self, data, *args, **kwargs):
    if len(data) < 2:
      return data
      
    unique_data = {}
    for item in data:
      unique_data[self._main_reference.encryption().hash(hash_method="sha1").generate_hash(self._main_reference.helper_json().dumps(data= item))] = item

    return [ val for val in unique_data.values()]
  
  def __flatten(self, data, flatten_list, *args, **kwargs):
    if self._main_reference.helper_type().general().is_type(data, list):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "data",
        message = f"Unknown type: {type(data)}\n expected list"
      )
    
    flatten_list = []

    for item in data:
      if self._main_reference.helper_type().general().is_type(item, list):
        self.flatten(data = item, flatten_list = flatten_list)
        continue
      
      flatten_list.append(item)
    
    return flatten_list

  def flatten(self, data, *args, **kwargs):
    if self._main_reference.helper_type().general().is_type(data, list):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "data",
        message = f"Unknown type: {type(data)}\n expected list"
      )
    
    flatten_list = []
    return self.__flatten(data= data, flatten_list= flatten_list)
  
  # flatten_array_length
  def flatten_length(self, *args, **kwargs):
    # this shouldn't be needed I Can just do a len off the flatten
    raise self._main_reference.exception().exception(
      exception_type = "function"
    ).exception(
        logger = self.get_logger(),
      name = "flatten_length",
      message = f"Not Needed"
    )
  
  def array_chucked(self, data, chunk_size):
    if self._main_reference.helper_type().general().is_type(data, list):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "data",
        message = f"Unknown type: {type(data)}\n expected list"
      )
    
    return [data[index:index + chunk_size] for index in range(0, len(data), chunk_size)]

  # FindListItem
  def find_item(self, data, filter):
    for item in data:
      if filter(item):
        return item
    return None
  
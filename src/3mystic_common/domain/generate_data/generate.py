from base_class.base_common import base


class generate_data(base): 
  
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"generate_data", *args, **kwargs)
  
  def _get_restricted_keynames(self, *args, **kwargs):
    if hasattr(self, "_restricted_keynames"):
      return self._restricted_keynames

    self._restricted_keynames = ["meta_data"]
    return self._get_restricted_keynames(*args, **kwargs)

  def generate(self, generate_data_config, *args, **kwargs):
    return self._generate(generate_data_config= generate_data_config, *args, **kwargs)s

  def _generate(self, generate_data_config, is_child_elemement = False, *args, **kwargs):
    
    return_data = {}

    for key, item in generate_data_config.items():
      if key.lower() in self._get_restricted_keynames() and not is_child_elemement:
        raise self._main_reference.exception().exception(
          exception_type = "argument"
        ).exception(
          logger = self.logger,
          name = "generate_data_config",
          message = f"Contains an element using a reserved key: {key}. Reserved Keys: {self._get_restricted_keynames()}"
        )   

      if item.get("handler") is not None:
        raise self._main_reference.exception().exception(
            exception_type = "argument"
          ).type_error(
            logger = self.logger,
            name = "generate_data_config",
            message = f"Handler cannot be None for key: {key}."
          )
        
      if item.get("children") is not None:
        item.get("handler").print_descrinption(item)

        if self._main_reference.helper_type().general().is_type(item["children"], dict):
          return_data[key] = self._generate(generate_data_config= item, *args, **kwargs)
          continue
        
        if self._main_reference.helper_type().general().is_type(item["children"], list):
          return_data[key] = [
            self._generate(generate_data_config= child, *args, **kwargs) for child in self._generate(generate_data_config= item, return_data= return_data, *args, **kwargs)
          ]
            
          continue
        
        if key.lower() in self._get_restricted_keynames() and not is_child_elemement:
          raise self._main_reference.exception().exception(
            exception_type = "argument"
          ).type_error(
            logger = self.logger,
            name = "generate_data_config",
            message = f"Unknown children type. Should be either a Dictrionary of children or a list. Got Type {type(item['children'])}"
          )
        continue
      
      return_data[key] = item.get("handler").generate()

      if return_data[key].get("raw") is None or return_data[key].get("raw") is None:
        raise self._main_reference.exception().exception(
            exception_type = "function"
          ).exception(
            logger = self.logger,
            name = "handler",
            message = f"Handler for Key: {key} did not return proper response. Should return a dictionary with raw and formated"
          )
      
      


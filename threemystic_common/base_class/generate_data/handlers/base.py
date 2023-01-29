from threemystic_common.exceptions.generate_data.quit import quit_exception

class base_handler:
  def __init__(self, *args, **kwargs):
    pass
  
  def _response_is_valid(self, response_value, item):
    if self._response_is_required(item= item) and self._is_response_empty(response_value= response_value):
      return False
    
    if item.get("validation") is not None:
      return True if item.get("validation")(response_value) else False
    
    return True

  def _quit_options(self, *args, **kwargs):
    return ["exit", "quit"]
  
  def _quit_display_text(self, allow_quit, *args, **kwargs):
    if allow_quit or self._is_array():
      print(f"To exit please type one of the following:\n{self._quit_options()}")

  def _type(self, *args, **kwargs):
    return None

  def _is_array(self, *args, **kwargs):
    return False
    
  def _is_response_empty(self, response_value):
    if not response_value:
      return True
    
    if not str(response_value).strip():
      return True
    
    return False

  def print_descrinption(self, item, *args, **kwargs):

    if item.get("desc") is not None:
      print(item["desc"])
    
    if item.get("description") is not None:
      print(item["description"])
      
  
  def _response_is_required_not_required(self, item, *args, **kwargs):
    print(f"Default: {item.get('default')}")   

  def _response_is_required_required(self, item, *args, **kwargs):
    print("Required")

  def _get_formated(self, return_value, item, *args, **kwargs):
      return return_value  if item.get("conversion") is None else item.get("conversion")(return_value)

  def _get_default(self, item, *args, **kwargs):
    return item.get("default")

  def _response_is_required(self, item, *args, **kwargs):
    if item.get("optional") is not None:
      if item.get("optional") == False:
        return True
      
      return False
    
    if item.get("default") is None:
      return True

    return False 
  
  def _get_validation_message(self, item, *args, **kwargs):
    if item.get("messages") is not None:
      if item.get("messages").get("validation") is not None:
        return item.get("messages").get("validation")
    
    return "Not Valid"

  def _display_response_is_required(self, item, *args, **kwargs):
    print("-------------------------------------------------------------------------\n")
    print(self._get_validation_message(item= item))
    
    print("Input is not valid")

  def _get_user_input_header_prompt(self, attribute_name, item, *args, **kwargs):
    if item.get("messages") is not None:
      if item.get("messages").get("prompt") is not None:
        print(item.get("messages").get("prompt").format(attribute_name= attribute_name))
        return

    print(f"Enter your value for {attribute_name}: ")

  def _get_user_input_header(self, allow_quit, attribute_name = None, item = {}, *args, **kwargs):
    self._get_user_input_header_prompt(attribute_name= attribute_name, item= item)
    
    self.print_descrinption(item= item)
    
    if self._response_is_required(item= item):
      self._response_is_required_required(item= item, *args, **kwargs)
    else:
      self._response_is_required_not_required(item= item, *args, **kwargs)

    self._quit_display_text(allow_quit= allow_quit)

  def _process_type_none(self, item, allow_quit, *args, **kwargs):
    return_value = self._get_user_input_prompt()

    if allow_quit and return_value.lower() in self._quit_options():
      raise quit_exception()

    if not self._response_is_required(item= item):
      return return_value if self._response_is_valid(response_value= return_value, item= item) else self._get_default(item= item)

    while not self._response_is_valid(response_value= return_value, item= item):
      return_value = self._get_user_input_prompt()
      if allow_quit and return_value.lower() in self._quit_options():
        raise quit_exception()
      
      
      if not self._response_is_valid(response_value= return_value, item= item):
        print("-------------------------------------------------------------------------\n")
        print(self._get_validation_message(item= item))
        self._quit_display_text(allow_quit= allow_quit)
    
    return return_value

  def _get_user_input(self, item, allow_quit, *args, **kwargs):
    return_value = None
    
    if self._type() == None:
      try:
        return_value = self._process_type_none(item= item, allow_quit= allow_quit)
      
      
        return {
          "raw": return_value,
          "formated": self._get_formated(return_value= return_value, item= item)
        }
      except quit_exception:
        return {"quit": True}

  def _get_user_input_prompt(self, *args, **kwargs):
    print("-------------------------------------------------------------------------\n")
    return input("$: ")

  def generate(self, attribute_name, item, allow_quit = True, *args, **kwargs):
    self._get_user_input_header(attribute_name= attribute_name, item= item, allow_quit= allow_quit)
    
    return self._get_user_input(item= item, allow_quit= allow_quit)
    

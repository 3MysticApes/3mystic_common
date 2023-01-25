from pathlib import Path
from threemystic_common.base_class.base_common import base
import configparser

class helper_config(base): 
  """This is a set of library wrappers to help general python apps"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_config", *args, **kwargs)

  def _get_known_config_types(self, *args, **kwargs):
    return ["json", "config"]

  def load_defaults_config(self, config_type = "json", *args, **kwargs):
    if self._main_reference.helper_type().string().is_null_or_whitespace(config_type):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "config_type",
        message = f"config_type is either None or an empty string"
      )
    
    if config_type.lower() not in self._get_known_config_types():
      raise self._main_reference.exception().exception(
        exception_type = "generic"
      ).not_implemented(
        logger = self.get_logger(),
        name = "config_type",
        message = f"config_type not known, known values: {self._get_known_config_types()}"
      )

    if config_type.lower() == "json":
      return self._load_defaults_config_json(*args, **kwargs)
    
    if config_type.lower() == "config":
      return self._load_defaults_config_config(*args, **kwargs)
    
    
  def _load_defaults_config_config(self, path_to_config, config_key, config_name, *args, **kwargs):
    config_parser = configparser.ConfigParser()
    if self._main_reference.helper_type().string().is_null_or_whitespace(path_to_config) or self._main_reference.helper_type().string().is_null_or_whitespace(config_key) or self._main_reference.helper_type().string().is_null_or_whitespace(config_name):
      return config_parser
    
    config_path = Path(f'{path_to_config}/{config_key}/{config_name}').resolve()
    if not config_path.exists():
      return config_parser

    with config_path.open("r") as config_stream:
      config_parser.read_file(config_stream)
    
    return config_parser

  def _load_defaults_config_json(self, path_to_config, config_key, config_name, replace_on_merge, path_to_config_override, return_as_config = False, *args, **kwargs):
    defaults_config = self._load_defaults_config_json_data(
      path_to_config = path_to_config, 
      config_key = config_key, 
      config_name = config_name
    )

    if self._main_reference.helper_type().string().is_null_or_whitespace(path_to_config_override):
      path_to_config_override = f"{path_to_config}/override"
    
    override_config = self._load_defaults_config_json_data(
      path_to_config = path_to_config_override, 
      config_key = config_key, 
      config_name = config_name
    )

    if not return_as_config:
      return self._main_reference.helper_type().dictionary().merge_dictionary([ {}, defaults_config, override_config], replace_on_merge= replace_on_merge)
    
    config_parser = configparser.ConfigParser()
    return config_parser.read_dict(self._main_reference.helper_type().dictionary().merge_dictionary([ {}, defaults_config, override_config], replace_on_merge= replace_on_merge))
  
  def _load_defaults_config_json_data(self, path_to_config, config_key, config_name, *args, **kwargs):
    if self._main_reference.helper_type().string().is_null_or_whitespace(path_to_config) or self._main_reference.helper_type().string().is_null_or_whitespace(config_key) or self._main_reference.helper_type().string().is_null_or_whitespace(config_name):
      return {}

    config_path = Path(f'{path_to_config}/{config_key}/{config_name}').resolve()
    if not config_path.exists():
      return {}

    with config_path.open(mode= "r") as config_stream:
      json_data = config_stream.read()
        
    return self._main_reference.helper_json().loads(
      data= json_data,
      return_empty_json_on_null= True
    )
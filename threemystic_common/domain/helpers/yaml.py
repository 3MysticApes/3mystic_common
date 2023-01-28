import yaml

from threemystic_common.base_class.base_common import base


class helper_yaml(base): 
  """This is a set of library wrappers to help around expending json libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"helper_json", *args, **kwargs)
  
  def loads(self, data, return_empty_on_null = True, use_safe = True,  *args, **kwargs):   
    if data is None:
      return {} if return_empty_on_null else None

    if not self._main_reference.helper_type().general().is_type(data, str):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.get_logger(),
        name = "data",
        message = f"attribute is not of type string - {type(data)}"
      )
    from io import StringIO
    stream_data = StringIO(data)
    return yaml.safe_load_all(stream_data) if use_safe else yaml.load_all(stream_data)

  def dumps(self, data, default_encoder_function = None, use_safe = True, *args, **kwargs):   
    return yaml.safe_dump_all(data) if use_safe else yaml.dump_all(data)

  def load_file(self, path_json, return_empty_on_null = True, use_safe = True, *args, **kwargs):
    with open(str(path_json), 'r') as yaml_stream:
      return yaml.safe_load_all(yaml_stream) if use_safe else yaml.load_all(yaml_stream) 
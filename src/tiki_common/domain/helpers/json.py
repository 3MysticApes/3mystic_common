import json
from datetime import datetime
from zoneinfo import ZoneInfo

import dateutil.tz as dateutil_tz


class helper_json: 
  """This is a set of library wrappers to help around expending json libary"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  def __get_offset_from_zoneinfo(cls, zoneinfo, return_as_timedelta = False):   
    if not return_as_timedelta:
      return datetime.now(tz= zoneinfo).strftime('%z')
    
    return datetime.now(tz= zoneinfo).utcoffset()

  # json_dumps_serializable_default
  def serializable_default(self, data, *args, **kwargs):
    if self.is_type(data, datetime) or self.is_type(data, type(datetime.now().time())):
      return data.isoformat()

    if self.is_type(data, [ dateutil_tz.tz.tzutc,  dateutil_tz.tz.tzlocal, ZoneInfo]):
      return self.__get_offset_from_zoneinfo(data)
    try:
      json.dumps(data)
    except:
      if hasattr(data, "__dict__"):
        return data.__dict__
      raise

    return data
  
  def dumps(self, data, default_encoder_function = None, *args, **kwargs):   
    return json.dumps(data, default= self.serializable_default if default_encoder_function is None else default_encoder_function)
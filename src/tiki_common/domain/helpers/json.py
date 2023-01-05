import json
from datetime import datetime
from zoneinfo import ZoneInfo
import dateutil.tz as dateutil_tz

class json: 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, *args, **kwargs) -> None:
    pass
  
  def __get_offset_from_zoneinfo(cls, zoneinfo, return_as_timedelta = False):   
    if not return_as_timedelta:
      return datetime.now(tz= zoneinfo).strftime('%z')
    
    return datetime.now(tz= zoneinfo).utcoffset()

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
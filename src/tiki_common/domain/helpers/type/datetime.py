from datetime import datetime

from dateutil import tz as dateutil_tz


class helper_type_datetime: 
  """This is a set of library wrappers to help around expending datetime libary"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  def convert_datetime_utc(self, custom_datetime, default_utctime = True, *args, **kwargs):   
    if custom_datetime.tzinfo is None:
      custom_datetime = (custom_datetime.replace(tzinfo=dateutil_tz.tzutc() if default_utctime else dateutil_tz.tzlocal()))
          
    return custom_datetime.astimezone(dateutil_tz.tzutc())
    
  def get_utc_datetime(self, *args, **kwargs):    
    return self.convert_datetime_utc(custom_datetime=datetime.utcnow(), default_utctime= True)
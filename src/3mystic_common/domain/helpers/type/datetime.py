from datetime import datetime, timedelta

from dateutil import tz as dateutil_tz
from base_class.base_common import base
from zoneinfo import ZoneInfo
import math



class helper_type_datetime(base): 
  """This is a set of library wrappers to help around expending datetime libary"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
  # get_utc_datetime
  # get_utc
  def get(self, time_zone = "utc", *args, **kwargs):    
    utc = self.convert_to_utc(dt=datetime.utcnow(), default_utctime= True)
    return utc.astimezone()
  
  def get_epoch(self, *args, **kwargs):    
    return datetime.utcfromtimestamp(0)

  # convert_datetime_utc
  def convert_to_utc(self, dt, default_utctime = True, *args, **kwargs):   
    if dt.tzinfo is None:
      dt = (dt.replace(tzinfo=dateutil_tz.tzutc() if default_utctime else dateutil_tz.tzlocal()))
          
    return dt.astimezone(dateutil_tz.tzutc())
  
  def datetime_as_string(self, datetime_format = "%Y%M%d%H%M%S", datetime_to_format = None, *args, **kwargs):    
    if datetime_to_format is None:
      datetime_to_format = self.get()
    
    return datetime_to_format.strftime(datetime_format)
  
  # get_tzinfo_from_datetime
  def get_tzinfo(self, check_datetime, default_tz, *args, **kwargs):
    
    if check_datetime.tzinfo is not None:
      return check_datetime.tzinfo
    
    return self.get_timezone(timezone= default_tz)

  # get_tzinfo
  def get_timezone(self, timezone, default_utc = True, *args, **kwargs):
    if not self._main_reference.helper_type().general().is_type(timezone, str):
      return dateutil_tz.tzutc() if default_utc else dateutil_tz.tzlocal()
      
    if not self._main_reference.helper_string().is_null_or_whitespace(timezone):
      return dateutil_tz.tzutc() if default_utc else dateutil_tz.tzlocal()

    if timezone.lower() == "utc":
      return dateutil_tz.tzutc()
    
    if timezone.lower() == "local":
      return dateutil_tz.tzlocal()

    return ZoneInfo(timezone)
  
  def get_offset_from_zoneinfo(self, zoneinfo, return_as_timedelta = False, *args, **kwargs):   
    if not return_as_timedelta:
      return datetime.now(tz= zoneinfo).strftime('%z')
    
    return datetime.now(tz= zoneinfo).utcoffset()
  
  def convert_time_24hours(self, time_str, error_missing_ampm= False, *args, **kwargs):   
    is_am = False
    if time_str[-2].lower() == "am" or time_str[-1].lower() == "a":
      is_am = True
    
    if not is_am and time_str[-2].lower() != "pm" and time_str[-1].lower() != "p":
      if error_missing_ampm:
        raise Exception("missing am/pm indicator")
      return time_str
    
    time_parts = self._main_reference.helper_type().string().split(string_value=time_str.rstrip(" amp"), split_value=":")
    for idx,part in enumerate(time_parts):
      time_parts[idx]=int(part)
    
    if not is_am:
      time_parts[0] += 12

    for idx,part in enumerate(time_parts):
      time_parts[idx]=str(part) if part>9 else f"0{part}"
    
    if len(time_parts) <3:
      time_parts.append("00")
    
    return ":".join(time_parts)
      
  # get_datetime_nearest_minute
  def get_nearest_minute(self, dt, minute = 15, *args, **kwargs):    
    return datetime(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour,minute=minute*int(math.floor((dt.minute / minute))), tzinfo= dt.tzinfo)

  # get_datetime_nearest_next_minute
  def get_nearest_next_minute(cls, dt, minute = 15, *args, **kwargs):  
    next_nearest_minute = minute*(int(math.floor((dt.minute / minute)))+ 1)
    if next_nearest_minute < 60:
      return datetime(year=dt.year, month=dt.month, day=dt.day, hour=dt.hour,minute=next_nearest_minute, tzinfo= dt.tzinfo)
    
    return dt + timedelta(seconds=((next_nearest_minute - dt.minute) * 60))

  # parse_datetime_iso
  def parse_iso(self, iso_datetime_str, *args, **kwargs):    
    return datetime.fromisoformat(iso_datetime_str.replace('Z', '+00:00'))

  # convert_datetime_utc
  def convert_utc(self, dt, default_utctime = True):   
    if dt.tzinfo is None:
      dt = (dt.replace(tzinfo=dateutil_tz.tzutc() if default_utctime else dateutil_tz.tzlocal()))
          
    return self.convert_timezone(
      dt= dt,
      timezone = "utc"
    )
  
  def set_tzinfo(self, dt, timezone = "utc", force_replace = False, *args, **kwargs):    
    
    if dt.tzinfo is not None and not force_replace:
      dt = dt.astimezone(self.get_timezone(timezone))
      return dt

    dt =  dt.replace(tzinfo=self.get_timezone(timezone))
    return dt


  # convert_datetime
  def convert_timezone(self, dt = None, timezone = None, base_timezone = "utc", *args, **kwargs):    
    if dt is None:
      dt = self.get()
    
    dt_timezone = self.get_tzinfo(check_datetime= dt, default_tz= base_timezone)
    self.set_tzinfo(dt= dt, timezone=dt_timezone, force_replace= True)
    timezone = self.get_timezone(timezone= timezone)
    return dt.astimezone(timezone) 

  # remove_tzinfo_datetime
  def remove_tzinfo(self, dt, default_utctime = True, *args, **kwargs):         
    return self.convert_to_utc(dt= dt, default_utctime= default_utctime).replace(tzinfo=None)

  # convert_datetime_local
  def convert_local(self, dt, *args, **kwargs):
    if dt is None:
      dt = self.get()
    
    dt_timezone = self.get_tzinfo(check_datetime= dt, default_tz= None)
    self.set_tzinfo(dt= dt, timezone=dt_timezone, force_replace= True)
    return self.convert_timezone(
      dt= dt,
      timezone = "local"
    )
  
  # datetime_ticks_as_seconds
  def ticks_as_seconds(self, dt, tick_startdate = datetime(year= 1, month= 1, day= 1, hour= 0, minute= 0, tzinfo= dateutil_tz.tzutc()), *args, **kwargs):
    dt = self.convert_to_utc(dt)
    if tick_startdate is None:
      tick_startdate = datetime(year= 1, month= 1, day= 1, hour= 0, minute= 0, tzinfo= dateutil_tz.tzutc())

    tick_startdate = self.convert_to_utc(tick_startdate)
    return (dt - tick_startdate).total_seconds()

  # datetime_ticks
  def ticks(self, dt, tick_startdate = datetime(year= 1, month= 1, day= 1, hour= 0, minute= 0, tzinfo= dateutil_tz.tzutc()), *args, **kwargs):
    return self.datetime_ticks_as_seconds(dt= dt, tick_startdate= tick_startdate) * 10**7
  
  def isTokenExpired_Now(self, compare_datetime, buffer_delta = timedelta(seconds=300)):   
    return (self.convert_utc(compare_datetime) <= (self.convert_utc(datetime.now()) + buffer_delta))

  # isTokenExpired_Duration
  def is_token_expired(self, token_life_duration, start_time = None, buffer_delta = timedelta(seconds=60), *args, **kwargs):  
    if start_time is None:
      start_time = self.get()
    return (start_time + token_life_duration) <= (self.get() + buffer_delta)
  
  # isTokenExpiredEpoch_Duration
  def is_token_expired_epoch(self, token_life_duration, start_time = None, buffer_delta = timedelta(seconds=300), *args, **kwargs):  
    if start_time is None:
      start_time = self.get_epoch()
    return (start_time + token_life_duration) <= (datetime.utcnow() + buffer_delta)
  
  # GetTokenExpiredEpoch_Duration
  def GetTokenExpiredEpoch_Duration(self, token_life_duration, start_time = None):  
    if start_time is None:
      start_time = self.get_epoch()
    return (start_time + token_life_duration)
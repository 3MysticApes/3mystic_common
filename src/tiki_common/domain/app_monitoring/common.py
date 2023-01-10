
class app_monitoring_common: 
  """This is a common set of methods and libraries"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference
  
  
  def performance(self, *args, **kwargs):
    if not hasattr(self, "_performance"):
      return self._performance
    
    from domain.app_monitoring.performance import \
        app_monitoring_performance as app_monitorin
    self._performance = app_monitorin(
      main_reference= self._main_reference
    )
    return self.performance(*args, **kwargs)
  
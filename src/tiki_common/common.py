class common_main: 
  """This is a common set of methods and libraries"""

  class emptyclass(object):   
    """This is a class designed for dynamic creation""" 
    def __init__(self):
      pass

  def __init__(self) -> None:
    self.default_columns = {}
    self.default_columns_cmdb = {
      "no_region": ["Account ID", "Account Name"],
      "region": ["Account ID", "Account Name", "Region" ]
    }
  
  def performance_monitoring(self, *args, **kwargs):
    if not hasattr(self, "_performance_monitoring"):
      return self._performance_monitoring
    
    from domain.monitor.performance import performance
    self._performance_monitoring = performance()
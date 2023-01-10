class app_monitoring_performance: 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, main_reference, features, *args, **kwargs) -> None:
    self._main_reference= main_reference
    
    if features is None:
      return
    
    self.__enable_feature_memory(
      features= features, **kwargs
    )
  
  def __enable_feature_memory(self, features, **kwargs):
    if features.get("memory") == True:
      import tracemalloc
      if not hasattr(self, "_memory"):
       self._memory = tracemalloc

  def memory_performance(self, raise_exception_not_init = True, **kwargs):
    if hasattr(self, "_memory"):
      return self._memory
    
    if raise_exception_not_init:
      raise Exception("Memory tracing not defined")
    return None

  def startstop_tracemalloc(self, action = None, *args, **kwargs):
    memory_performance = self.memory_performance(raise_exception_not_init= False)
    if memory_performance is None:
      raise Exception("Memory tracing not defined")
    if action is None:
      if memory_performance.is_tracing():
        return memory_performance.stop()
      return memory_performance.start()
    
    if action.lower() == "start":
      return memory_performance.start()
    
    return memory_performance.stop()
  
  def start_performance_monitoring(self, *args, **kwargs):    
    self.startstop_tracemalloc(action= "start")
      
  
  def stop_performance_monitoring(self, *args, **kwargs):
    self.startstop_tracemalloc(action= "stop")
  
  def performance_monitoring_memory_snapshot(self, clear_tracing = False):    
    memory_performance = self.memory_performance(raise_exception_not_init= False)
    if memory_performance is None:
      raise Exception("Memory tracing not defined")

    snapshot = memory_performance.take_snapshot()
    if clear_tracing:
      memory_performance.clear_traces()
    return snapshot
  
  def performance_monitoring_memory(self, *args, **kwargs):
    memory_performance = self.memory_performance(raise_exception_not_init= False)
    if memory_performance is None:
      raise Exception("Memory tracing not defined")

    return {
      "traced_memory": memory_performance.get_traced_memory(),
      "tracemalloc_memory": memory_performance.get_tracemalloc_memory()
    }
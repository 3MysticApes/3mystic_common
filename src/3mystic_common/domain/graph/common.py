from base_class.base_common import base


class graph_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"graph", *args, **kwargs)
  
  def __get_supported_graphs(self):
    return ["msgraph"]
  
  def graph_init(self, graph_method, graph_config, *args, **kwargs):
    graph_method = graph_method.lower() if graph_method is not None else ""
    if not hasattr(self, "_graph_method"):
      if self._graph_method.get(graph_method) is not None:
        return self._graph_method[graph_method]
    
    if graph_method not in self.__get_supported_graphs():
      raise self._main_reference.exception().exception(
        exception_type = "generic"
      ).not_implemented(
        logger = self.logger,
        name = "graph_method",
        message = f"Unknown Graph Provided: {graph_method}.\nSupported Graph Providers{self.__get_supported_graphs()}"
      )

    if not hasattr(self, "_graph_method"):
      self._graph_method = {}

    if graph_method == "msgraph":
      from domain.graph.msgraph import graph_msgraph as graph
      self._graph_method[graph_method] = graph(
        config = graph_config
      )

    if not hasattr(self, "_hash"):
      from domain.encryption.hash import encryption_hash as encryption
      self._hash = encryption
      self._hash_methods = {}
    
    self._hash_methods[hash_method.lower()] = self._hash(
      main_reference= self._main_reference,
      hash_method= hash_method
    )
    return self.hash(*args, **kwargs)

  def graph(self, graph_method, *args, **kwargs):
    graph_method = graph_method.lower() if graph_method is not None else ""
    if not hasattr(self, "_graph_method"):
      if self._graph_method.get(graph_method) is not None:
        return self._graph_method[graph_method]
   
    raise self._main_reference.exception().exception(
      exception_type = "generic"
    ).not_implemented(
      logger = self.logger,
      name = "graph_method",
      message = f"Graph not inited: {graph_method}.\nPlease run graph_init}"
    )

  
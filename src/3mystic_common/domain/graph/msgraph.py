from domain.graph.base_class.base import graph_base as base

class graph_msgraph(base): 
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"graph_msgraph", *args, **kwargs)
   
  # bring in the msgraph helper
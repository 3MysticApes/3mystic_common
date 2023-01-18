from base_class.base_common import base


class cmdb_common(base): 
  """This is a common set of methods and libraries"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= "cmdb", *args, **kwargs)
    self._cmdb = {}
    self.__supported_cloud_source = ["aws", "azure"]
  
  
  def cmdb(self, cloud_source, *args, **kwargs):
    
    if self._main_reference.helper_type().string().is_null_or_whitespace(cloud_source):
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).type_error(
        logger = self.logger,
        name = "cloud_source",
        message = "cloud_source is None"
      )
    
    if cloud_source.lower() not in self.__supported_cloud_source:
      raise self._main_reference.exception().exception(
        exception_type = "argument"
      ).exception(
        logger = self.logger,
        name = "cloud_source",
        message = f"Unknown cloud_source: {cloud_source}"
      )
    
    cloud_source = cloud_source.lower()
    if cloud_source == "aws":
      if self._cmdb.get(cloud_source) is not None:
        return self._cmdb.get(cloud_source)
      from domain.cmdb.aws import cmdb_aws as cmdb
      self._cmdb[cloud_source] = cmdb(
        main_reference= self._main_reference
      )
      return self.cmdb(cloud_source= cloud_source, *args, **kwargs)
    
    
    if cloud_source == "azure":
      if self._cmdb.get(cloud_source) is not None:
        return self._cmdb.get(cloud_source)
      from domain.cmdb.azure import cmdb_azure as cmdb
      self._cmdb[cloud_source] = cmdb(
        main_reference= self._main_reference
      )
      return self.cmdb(cloud_source= cloud_source, *args, **kwargs)
  
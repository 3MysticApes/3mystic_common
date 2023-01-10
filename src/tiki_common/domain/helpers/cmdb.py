import asyncio


class helper_cmdb: 
  """This is a set of library wrappers to help create a cmdb"""

  def __init__(self, main_reference, *args, **kwargs) -> None:
    self._main_reference= main_reference

    self.default_columns = {}
    self.default_columns_cmdb = {
      "no_region": ["Account ID", "Account Name"],
      "region": ["Account ID", "Account Name", "Region" ]
    }

  def get_cmdb_source(self, cloud_client, *args, **kwargs):
    source = cloud_client.source()
    known_cloud_sources = ["aws", "azure"]

    if source.lower() not in known_cloud_sources:
      raise Exception(f"Unknown Cloud Source: {source}") 
    
    return source

  def get_resource_groups(self, cloud_client, *args, **kwargs):    
    source = self.get_cmdb_source(cloud_client= cloud_client)
    if source.lower() == "aws":
      raise Exception("Not Defined") 
    
    if source.lower() == "azure":
      raise Exception("Not Defined") 

  def get_report_default_columns(self, data_item):
    if self._main_reference.helper_type().general().is_type(data_item["default_columns"], dict):
      return data_item["default_columns"]["default"]
    
    return data_item["default_columns"]
  
  def process_report_data(self, InventoryDataSheet, report_data):
    for sheet in InventoryDataSheet:
      for data in (report_data[sheet] if not self._main_reference.helper_type().general().is_type(report_data[sheet], asyncio.Task) else report_data[sheet].result()):
        InventoryDataSheet[sheet]["data"].append(
          (self.get_report_default_columns(data_item= data)) +
          [data_item for _, data_item in data["data"].items()] +
          self.generate_tag_columns(InventoryDataSheet=data["tags_columns"]["InventoryDataSheet"], tags= data["tags_columns"]["tags"])
        )
  
  def generate_cmdb_data(self, inventory_data, InventoryDataSheet, report_data):
    cmdb_data = {
      sheet:[] for sheet in InventoryDataSheet
    }    

    if not inventory_data.config.cmdb.enabled:
      return cmdb_data
    
    for sheet in InventoryDataSheet:
      if report_data.get(sheet) is None:
        continue

      cmdb_data[sheet]+=report_data[sheet] if not self._main_reference.helper_type().general().is_type(report_data[sheet], asyncio.Task) else report_data[sheet].result()     
    
    return cmdb_data
  
  def compare_account_ids(self, cloud_client, account1, account2):
    source = self.get_cmdb_source(cloud_client= cloud_client)
    if source.lower() == "aws":
      raise Exception("Not Defined") 
    
    if source.lower() == "azure":
      raise Exception("Not Defined") 
  
  # compare_cmdb_string_possible_numeric
  def compare_string_possible_numeric(cls, str1, str2):
    str1 = str(str1).strip(" '")
    str2 = str(str2).strip(" '")
    if not str1.lower().startswith("=text("):
      str1 = f'=Text("{str1}", "?")'
    if not str2.lower().startswith("=text("):
      str2 = f'=Text("{str2}", "?")'

    return str1.lower() == str2.lower()
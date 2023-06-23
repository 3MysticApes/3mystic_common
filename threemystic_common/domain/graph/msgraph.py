from threemystic_common.domain.graph.base_class.base import graph_base as base

# This will probably not be included as it looks like MS has a python SDK
# https://github.com/microsoftgraph/msgraph-sdk-python
# so the sdk is still very much in beta. I do not recommend at this time. - 2023-06-22
class graph_msgraph(base):
  """This is a set of library wrappers to help monitor performance"""

  def __init__(self, *args, **kwargs) -> None:
    super().__init__(logger_name= f"graph_msgraph", *args, **kwargs)    

   
  def graph_scope_default(self, *args, **kwargs):
    return 'https://graph.microsoft.com/.default'
    
  def openid_config_default(self, *args, **kwargs):
    return "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration"
  
  def create_folder_data(self, name = "New Folder", *args, **kwargs):
    return {
    "name": name,
    "folder": { }
    }

  def create_file_data(self, name = "New File", mime_type = "text/plain", *args, **kwargs):
    return {
    "name": name,
    "file": { 
      "mimeType": mime_type
    }
  }
  
  def _get_known_session_types(self, *args, **kwargs):
    return {
      "workbook": "Workbook"
    }
  
  def get_known_session_types(self, *args, **kwargs):
    return list(self._get_known_session_types().keys())
  
  def generate_graph_url(self, resource, resource_id = None, base_path= None, *args, **kwargs):
    graph_url = self.get_common().helper_type().string().trim(string_value= f'{resource}')
    if not self.get_common().helper_type().string().is_null_or_whitespace(string_value= resource_id):
      resource_id = self.get_common().helper_type().string().ltrim(string_value= resource_id, trim_chars= "\\/" )
      graph_url = self.get_common().helper_type().string().rtrim(string_value= f'{graph_url}/{resource_id}', trim_chars= "\\/")
    
    if not self.get_common().helper_type().string().is_null_or_whitespace(string_value= base_path):
      base_path = self.get_common().helper_type().string().ltrim(string_value= base_path, trim_chars= "\\/" )
      graph_url = self.get_common().helper_type().string().rtrim(string_value= f'{graph_url}/{base_path}', trim_chars= "\\/")

    return graph_url
  
  def _get_auth_header(self, scope= None, refresh = False, *args, **kwargs):
    if self.get_common().helper_type().string().is_null_or_whitespace(string_value= scope):
      scope = self.graph_scope
    
    scope_hash =self.get_common().encryption().hash(hash_method= "sha1").generate_hash(data= scope)
    if hasattr(self, "_current_graph_token") and not refresh:
      if self._current_graph_token.get(scope_hash) is not None:
        if not self.get_common().helper_type().datetime().is_token_expired_epoch(
          token_life_duration= self.get_common().helper_type().datetime().time_delta(
            seconds= self._current_graph_token.get(scope_hash).get("expires_on")
          )):
          return {
            "Authorization": f'Bearer {self._current_graph_token.get(scope_hash)["token"]}'
          }
    
    if not hasattr(self, "_current_graph_token"):
      self._current_graph_token = {}
    
    auth_token = (self.graph_credentials.get_token(scope)
                  if not self.get_common().helper_type().general().is_type(obj= self.graph_credentials, type_check= dict)
                  else self.graph_credentials.get("get_token"))
    
    self._current_graph_token[scope_hash] = ({
      "token": auth_token.token,
      "expires_on": auth_token.expires_on
    } if not self.get_common().helper_type().general().is_type(obj= auth_token, type_check= dict)
    else auth_token
    )
    return self._get_auth_header(scope= scope, *args, **kwargs)
  
  def _get_session_type(self, session_type, *args, **kwargs):
    if self.get_common().helper_type().string().is_null_or_whitespace(string_value= session_type):
      return None

    session_type= self.get_common().helper_type().string().set_case(string_value= session_type, case= "lower")
    if session_type in self.get_known_session_types():
      return self._get_known_session_types()[session_type]
    
    
    raise self.get_common().exception().exception(
      exception_type = "argument"
    ).type_error(
      logger = self.get_common().get_logger(),
      name = "session_type",
      message = f"session_type is an unknown value ({session_type}): valid options {self.get_known_session_types()}"
    )
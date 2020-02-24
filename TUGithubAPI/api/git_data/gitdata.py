from TUGithubAPI.core.rest_client import RestClient
from TUGithubAPI.api.git_data.references import Refes
class Gitdata(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Gitdata, self).__init__(api_root_url, **kwargs)
        self.refs = Refes(api_root_url,**kwargs)



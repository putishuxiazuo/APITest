from TUGithubAPI.core.rest_client import RestClient

class Refes(RestClient):
    def get_a_reference(self,owner,repo,ref):
        '''获取单个分支的接口'''
        return self.get("/repos/{0}/{1}/git/ref/{2}".format(owner,repo,ref))

    def create_a_reference(self,owner,repo,**kwargs):
        return self.post("/repos/{0}/{1}/git/refs".format(owner,repo),
                         **kwargs )
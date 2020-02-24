from TUGithubAPI.api.repositories.repos import Repos
from TUGithubAPI.api.issues.issues import Issues
from TUGithubAPI.api.git_data.gitdata import  Gitdata


class Github():
    def __init__(self,api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.repos = Repos(self.api_root_url, **kwargs)
        self.gitdata = Gitdata(self.api_root_url,**kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)

if __name__ == '__main__':
    username = "putishuxiazuo"
    password = "xygz1234hao"
    orgname = "TestUpCommunity"
    reponame ="hello2"
    reference = "heads/master"
    # r = Github(api_root_url = "https://api.github.com",
    #            token="fcecbfaf9c630409e569f0e5d551f1fb10eb7fdb")
    r = Github(api_root_url = "https://api.github.com",
               username = username,password = password)
    response = r.repos.list_your_repos()
    print(response.headers)
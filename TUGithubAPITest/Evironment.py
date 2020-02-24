'''使用相对路径调用github.py'''
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path+'\\TUGithubAPI')

from TUGithubAPI.github import Github

class Env:
    def __init__(self,api_root_url,token):
        self.github = Github(api_root_url = api_root_url,token = token)
import pytest
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path+'\\TUGithubAPI')
from TUGithubAPI.operations.repo import create_repo,create_branch
def test_create_repo_and_create_a_branch_success(env):
    result = create_repo(env.github,"hello2")
    assert  result.success == True,result.error
    result = create_branch(env.github,"putishuxiazuo","hello2","refs/heads/thre","heads/master")
    assert result.success == True, result.error

if __name__ == "__main__":
    pytest.main()

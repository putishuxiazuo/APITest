import pytest,os,json
from TUGithubAPITest.Evironment import Env


@pytest.fixture(scope='module',autouse=True)
def env():
    yield Env(api_root_url ="https://api.github.com",
              token = os.environ['token'])      #更改sequence,env的值，切换不同的api_root_url


@pytest.fixture(scope='module',autouse=True)
def just_print():
    print('我只是打印一段文本')





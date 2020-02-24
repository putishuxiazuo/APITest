import pytest,os,json
from TUGithubAPITest.Evironment import Env


@pytest.fixture(scope='module',autouse=True)
def env():
    with open("test_single_api/data.json","r") as f:
        data = f.read()
    data = json.loads(data)             #Json字符串转换为列表
    yield Env(api_root_url =data[int(os.environ["sequence"])][os.environ["env"]]["api_root_url"],
              token = os.environ['token'])      #更改sequence,env的值，切换不同的api_root_url


@pytest.fixture(scope='module',autouse=True)
def just_print():
    print('我只是打印一段文本')





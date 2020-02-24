from TUGithubAPI.github import Github
from TUGithubAPI.operations.repo import delete_repo,create_branch     #导入repo.py，此为关键字封装的文件



if __name__ ==  '__main__':
    github = Github(api_root_url = "https://api.github.com",token = 'fcecbfaf9c630409e569f0e5d551f1fb10eb7fdb')
    #在当前用户下创建一个仓库，除了仓库名字以外，全部采用默认值
    # result = create_repo(github,'simpletest01')
    # #断言收发是否成功，
    # assert  result.success == True,result.error
    # #在当前用户下创建一个repo，使用一些输入值
    # result = create_repo(github,'lenovo',has_issues=False)
    # assert  result.success == True,result.error
    #创建一个名字为testme的repo，其中projects/issues/wiki均为False
    # result = create_repo(github,'testme',has_issues=False,
    #                      has_projects=False,has_wiki = False)
    # assert  result.success == True,result.error
    result = create_branch(github, "putishuxiazuo", "hello2", "refs/heads/thre", "heads/master")
    print(result.response.content)
    assert result.success == True,result.error
    print(result.response)
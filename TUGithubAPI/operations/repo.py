'''关键字的封装'''

from TUGithubAPI.core.base import CommonItem
from TUGithubAPI.api.git_data.gitdata import Gitdata
from TUGithubAPI.api.git_data.references import Refes
#创建仓库
def create_repo(github,name,org = None,description = None,homepage=None,private=False,
                has_issues=True,has_projects=True,has_wiki=True):
    result = CommonItem()
    result.success = False
    payload = {"name":name,"description":description,"homepage":homepage,"private":private,"has_issues":has_issues,
               "has_projects":has_projects,"has_wiki":has_wiki}
    if org:
        response = github.repos.create_organization_repo("yzzorg",json = payload)
    else:
        response = github.repos.create_user_repo(json = payload)
    result.response = response
    if response.status_code == 201:
        result.success = True
    else: result.error = "create repo got {0},should be 201".format(response.status_code)
    return  result

#删除指定的仓库
def delete_repo(github,owner,repo):
    result = CommonItem()
    response = github.repos.delete_repo(owner,repo)
    result.response = response
    if response.status_code == 204:
        result.success = True
    else:
        result.error = 'delete repo got {},should be 204'.format(response.status_code)
    return  result
def create_branch(github,owner,repo,new_branch_name,source_branch_name):
    '''

    :param github: Github对象
    :param owner: 仓库的用户
    :param repo: 指定的仓库
    :param new_branch_name:创建的新分支的名称，格式为refs/heads/分支名
    :param source_branch_name:老分支的名称，获取老分支的url格式为heads/分支名
    :return:创建新分支后返回的对象
    '''
    result = CommonItem()
    response = github.gitdata.refs.get_a_reference(owner,repo,source_branch_name)
    if response.status_code != 200:
        result.error = "Get branch got {},should be 200".format(response.status_code)
        result.response = response
        return result
    response = response.json()
    source_branch_sha = response["object"]["sha"]    #获取master分支的SHA值
    #create_a_reference的post参数
    data = {"ref":new_branch_name,"sha":source_branch_sha}
    response = github.gitdata.refs.create_a_reference(owner,repo,json = data)
    if response.status_code != 201:
        result.error = "Create branch got {},should be 201".format(response.status_code)
        result.response = response
        return  result
    result.success = True
    result.response = response
    return  result




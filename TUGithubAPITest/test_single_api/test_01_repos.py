import pytest

def test_list_all_public_repos(env):
    r = env.github.repos.list_all_public_repos()
    assert  r.status_code == 200,"status_code should be 200 but actually is {0}".format(r.status_code)


if __name__ == "__main__":
    pytest.main()
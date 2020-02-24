# APITest
接口测试框架说明：
使用的库：
python3.7+requests2.21+pytest5.
此接口框架针对的是HTTP/HTTPS协议，返回的数据为json数据格式。
文件说明：
TUGithubAPI/api封装了接口功能（由接口文档得出），在github.py文件可对封装的接口进行调试；
TUGithubAPI/operation实现了关键字的封装（接口的组合），在debug.py文件中可对关键字的封装进行调试；
TUGithubAPITest/test_single_api是对单个接口进行测试；
TUGithubAPITest/scenario是对多个接口组成的场景进行测试。


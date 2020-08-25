import pytest


# 创建一个fixture方法
@pytest.fixture()  # autouse自动所有方法fixtrue
def login(con):
    print('登陆')
    print('获取token')
    name = 'lili'
    passwd = '12322'
    yield [name, passwd]
    print('退出')


# 测试用例,需要提前登陆
# 在用例之前会传入一个fixture方法
def test_1(login):
    print('测试用例')
    print(f"name 和passwd 是{login}")

@pytest.mark.run(order)
def test_2():
    print('测试用例')


def test_3(login):
    print('测试用例')


def test_4():
    print('测试用例')

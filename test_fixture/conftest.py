import pytest


@pytest.fixture(scope='module')
def con():
    print('连接数据库')  # 先连接数据库
    yield
    print('断开数据库')  # 结束断开数据库


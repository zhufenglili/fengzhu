import pytest

from counter.counter import Counter


@pytest.fixture(scope="class")
def get_con():

    print('获取计算器实例')
    con = Counter()
    return con #返回定义的实例

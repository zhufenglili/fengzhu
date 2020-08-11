import pytest

from counter.counter import Counter


class Test_c:
    def setup_class(self):
        self.cou = Counter()
        print('开始计算')

    def teardown_class(self):
        print('计算结束')

    def setup(self):
        print('开始测试')

    def teardown(self):
        print('测试结束')
    @pytest.mark.parametrize("a,b,expect",[(0,1,0),(1,0,0),(1,1,1),(500,500),(0.5,0.5,1)])
    def test_wul(self,a,b,expect):
        mull = self.cou.mul(a,b)
        assert expect == mull
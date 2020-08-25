import pytest


class test_1:
    def test_1(self):
        print('我是一')

    @pytest.mark.run(order=1)
    def test_2(self):
        print("我是二")

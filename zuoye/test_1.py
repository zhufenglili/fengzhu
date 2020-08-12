import pytest
import yaml

from counter.counter import Counter

@pytest.fixture(scope='class')#用例需要传参才能打印
def get_o():
    print('开始计算')
    yield
    print('计算结束')

class Test_con:

    # 调用get_con中add加法,调用get_lo参数
    def test_add(self, get_o,get_con, get_lo):
    #实例调用add方法 ，参数索引获取参数
        summ = get_con.add(get_lo[0], get_lo[1])
    #判断summ是否为FLOAT
        if isinstance(summ, float):
    #取两位
            summ = round(summ, 2)
        assert get_lo[2] == summ

    # d调用get_con   使用get_a参数
    def test_del(self, get_con, get_a):
        # 实例调用del方法
        delo = get_con.del_l(get_a[0], get_a[1])
        if isinstance(delo, float):
            delo == round(delo, 2)
            assert get_a[2] == delo

    def test_mul(self,get_con,get_b):
      mul_m = get_con.mul(get_b[0],get_b[1])
      if isinstance(mul_m,float):
          mul_m == round(mul_m,2)
          assert get_b[2] == mul_m

    def test_div(self,get_con,get_c):
     try:
       divv = get_con.div(get_c[0],get_c[1])

       if isinstance(divv,float):
           divv == round(divv,2)
     except:
       if get_c[1] == 0:
           print('输入有误')
           assert get_c[2]==divv
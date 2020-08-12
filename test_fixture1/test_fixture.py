# 文件类名方法名以test开头
# 先定义一个测试类
import pytest
import yaml
from counter.counter import Counter


# 定义一个类
class Test_c:
    # 类执行前动作
    def setup_class(self):
        self.coun = Counter()  # 类中实例化计算器，可以加self
        print('开始计算')

    # 类执行后动作
    def teardown_class(self):
        print('计算结束')

    # 方法级别
    def setup(self):
        print('开始测试')

    def teardown(self):
        print('测试结束')

    with open('data.yml') as f:  # 打开参数化文件
        datt = yaml.safe_load(f)["add"]  # 获取dd数据 定义变量
        print(datt)
        datt1 = datt["dd"]  # 从datt变量获取dd
        print(datt1)
        datt2 = datt['bb']  # 从datt变量获取bb
        print(datt2)

    # 标签终端可设置先后执行 pytest -m mul -vs
    @pytest.mark.mul
    @pytest.mark.parametrize("a,b,expect", datt1, ids=datt2)  # 导入pytest 参数化
    def test_mul(self, a, b, expect):
        # coun = Counter()  # 实例化计算器类
        summ = self.coun.mul(a, b)  # 调用加法传参给变量
        if isinstance(summ, float):  # 对比是否为小数
            assert expect == round(summ, 2)  # 是小数保留两位
        # elif a == 0 or b == 0:
        #     print('不支持输入0')

    #
    with open('divvv.yml') as f:
        divvvv = yaml.safe_load(f)['div']
        print(divvvv)
        divvvv1 = divvvv['oo']
        print(divvvv1)
        divvvv2 = divvvv['qq']
        print(divvvv2)

    @pytest.mark.parametrize("a,b,expect", divvvv1, ids=divvvv2)
    def test_div(self, a, b, expect):
        try:
            divv = self.coun.div(a, b)
            if isinstance(divv,float):
                assert expect == round(divv,2)
        except:
            if  b == 0:
                print('错误')
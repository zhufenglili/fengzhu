import pytest
#导入PYtest
import yaml

with open('test_data.yml') as f:
   daters = yaml.safe_load(f)['add']#yaml文件只能打开一次  存储变量
   adddatas = daters['daters']#yml文件是字典 拿到key值 就能得到 V值
   print(adddatas)
   myid = daters["myid"]#yml文件是字典 拿到key值 就能得到 V值
   print(myid)
#创建类必须test开头
class Test_001:
    #使用参数化
    @pytest.mark.parametrize("a,b,expect",adddatas,ids=myid)#数据的名称
    def test_01(self,a,b,expect):
        summ = a + b
        if isinstance(summ,float): #判断类型
            print(summ)
            assert expect ==round(summ,2) #断言 四舍五入保留两位
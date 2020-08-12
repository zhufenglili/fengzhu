# 定义实例
import pytest
import yaml

from counter.counter import Counter


# 调用实例
@pytest.fixture(scope="class")
def get_con():
    con = Counter()
    return con


# 使用yaml打开加法参数
with open('data.yml') as f:
    # 获取data中add
    data = yaml.safe_load(f)["add"]
    print(data)
    # 获取myscope
    data_myscope = data["bb"]
    print(data_myscope)
    data_myid = data['dd']
    print(data_myid)

@pytest.fixture(params=data_myscope, ids=data_myid)
# 使用request传递数据
def get_lo(request):
    a = request.param
    print("a")
    return a


# 使用yaml打开减法参数
with open('data1.yaml') as a:
    del_l = yaml.safe_load(a)["dell"]
    del_ll = del_l["a"]  # 获取a参数数据
    del_lll = del_l["b"]  # 获取B=ids数据

    # 使用fixture传递数据


@pytest.fixture(params=del_ll, ids=del_lll)
def get_a(request):
    b = request.param
    print("b")
    return b


# 打开文件乘法
with open('data_c.yml') as b:
    mul_1 = yaml.safe_load(b)["mull"]
    mul_2 = mul_1["c"]
    mul_3 = mul_1["d"]


@pytest.fixture(params=mul_2, ids=mul_3)
def get_b(request):
    return request.param


# 打开文件除法
with open('divv.yml') as c:
    div = yaml.safe_load(c)["div"]
    div1 = div["oo"]
    div2 = div['qq']

#fixture参数化除法
@pytest.fixture(params=div1, ids=div2)
def get_c(request):
    return request.param

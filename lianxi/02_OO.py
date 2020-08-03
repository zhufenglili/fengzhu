#写一个bicycle（自行车）类，有run(骑行）方法，调用时显示骑行里程KM骑行里程为传入的数字：
#再写一个电动自行车类Ebicycle 继承Bicycle,添加电池电量的valume属性通过，传参传入，同时两个方法
#run(km) :
#1/fill_charge(vol)用来充电，vol为电量
#2、run(km）方法用于骑行，通过传入骑行里程数，显示骑行结果
#定义一个类
class Bicycle:


#定义一个方法 ，显示传参
    def run(self,km):#骑行的公里数
        print(f'骑行里程：{km}')
#再写一个电动自行车类Ebicycle 继承Bicycle
class Ebicycle (Bicycle):
#添加电池电量的valume属性通过，传参传入，
    def __init__(self,valume): #电量
        self.valume = valume
 #1/fill_charge(vol)用来充电，vol为电量
    def fill_charge(self,vol): #充电方法
        print(f"电动车已充电，目前充电量{vol}")
        print(f"充电后总电量{vol+self.valume}")
#run(km）方法用于骑行,没骑行10km消耗一度电，当电量消耗尽调用BICYCLE的rum方法骑行

    def run(self,km):
       e_km = self.valume*10


        #类实例化
b = Bicycle()
#使用实例化变量调用方法,传参
b.run(100)
#实例化
e = Ebicycle(100)
e.fill_charge(100)


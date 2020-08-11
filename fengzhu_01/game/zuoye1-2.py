#作业2

#定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
#see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
#fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
#定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
#加入模块化改造
import  os
#定义天山童姥类
class TongLao:
    #初始化参数 blood 血量  force武力值
     def __init__(self,blood,force):
        self.blood = blood #血量
        self.force = force #武力值

     def see_people(self,name):
         self.name = name  #初始化
         if self.name == "WYZ":
            print("师弟！！！！")#如果传入”WYZ”（无崖子），则打印，“师弟！！！！
         elif self.name == "李秋水":#李秋水”，打印“呸，贱人”，
             print("呸，贱人")
         elif self.name == "丁春秋":#如果传入“丁春秋”“叛徒！我杀
             print("叛徒！ 我杀了你")

    #   调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
    # 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    # 天山折梅手E_blood血量,E_force武力值
     def fight_zms(self,hp,power):
         self.blood = self.blood / 2
         self.force = self.force * 10
         self.hp = hp
         self.power = power

         #一回合对打
         self.hp = self.hp - self. force
         self.blood = self.blood - self.power
         if self.hp < self.blood:
             print('童姥赢了')
         elif self.hp > self.blood:
             print("敌人赢了")
         else:
             print("平局")

class Xuzhu(TongLao):



        def read(self):
            print("罪过罪过")


print(os.getcwd())

tianshantonglao = TongLao(10000,200)
tianshantonglao.see_people("WYZ")
tianshantonglao.see_people("李秋水")
tianshantonglao.fight_zms(1500,5)
Xuzhu(100000,500)
Xuzhu.read(1)
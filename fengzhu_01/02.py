class Abc:
    #初始化
    def __init__(self,Houyi,you_hp):
        self. Houyi= Houyi
        self.my_power = 200 #我的攻击值200
        self.you_hp = you_hp
        self.you_power = 200 #你的攻击值200
#定义方法
    def fight(self):
        while True:
            #我的血量= 我的血量- 你的攻击值
            self.Houyi = self.Houyi +self.defnse - self.you_power
            self.you_hp = self.you_hp - self.my_power
            #如果我的血量小于等于0，打印我的你的剩余血量 并退出
            if self.Houyi <= 0:
                print(f"你的血量剩余：{self.you_hp}")
                print(f"后裔血量剩余：{self.Houyi}")
                break
            elif self.you_hp <= 0:
                print(f"你的血量剩余：{self.you_hp}")
                print(f"后裔血量剩余：{self.Houyi}")
                break


class Houyi(Abc):#集成父类
    def __init__(self):
        self.defnse = 100#后裔新增属性 护甲
        super().__init__(1000,1000)#调用父类构造方法,并直接传参


houyi = Houyi()
houyi.fight()

#作业1

#用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
#1.创建一个类人物tian
class Tian:
    #初始化
    def __init__(self,name,age,gender,feature):
        self.name = name
        self.age = age
        self.gender = gender
        self.feature =feature

    #方法
    def sleep(self):
        print(f"{self.name}又睡着了~")
        print('天天睡~')

    def cook(self):
        print(f"{self.name}同学非常喜欢做饭，又非常好吃")

    #实例化
T = Tian("小田",20,"男","胖胖的")
T.sleep()#调用实例化方法
T.cook()

#2.创建一个宠物类
class Mandeng:
    def __init__(self,name,colour,age):#初始化参数
        self.name = name
        self.colour = colour
        self.age = age


    def eat(self):#定义方法
        print(f"{self.name}在肉罐头")

    def lick(self):
        print(f"{self.name}喜欢在他的{self.colour}毛上舔来舔去")

    #实例化
dengdeng  = Mandeng("小满登","灰色","1岁")
dengdeng.eat()
dengdeng.lick()
3
#3.定义一个电视剧人物
class Hafei:
    def __init__(self,name,character): #初始化参数
        self.name = name
        self.character = character #性格

    #方法
    def means(self):
        print(f"{self.name}性子{self.character}手段极其残忍，经常赏奴才一丈红！")

#参数实例化
H = Hafei("华妃","嚣张跋扈")
H.means()
#4.定义一个表
class Watch:
    #参数初始化
    def __init__(self,colour,function):
        self.colour = colour
        self.function = function

    #方法
    def statistics(self):#统计
        print(f"这块运动手表{self.colour}很好看，{self.function}也很多")

    #实例化
w = Watch("黑色","功能")
#实例化调用方法
w.statistics()

#5.定义一个房子
class House:
    def __init__(self,area,floor): #参数初始化 area 面积 floor楼层
        self.area = area
        self.floor = floor

        #方法daily rental 日租

    def daliy(self):
        print(f"这个房子面积有{self.area}，楼层是{self.floor}，日租金额800000元")

    #实例化参数
HOUSE  = House(400,22)
HOUSE.daliy()

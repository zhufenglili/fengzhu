
#建立类
class Cat:
#属性
    name = '满登登'

#初始化
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
 #动作
    @classmethod
    def eat(self):
        print(f"{self.name}吃的很开心")
    def play(self):
        print(f"{self.name}不知道在玩啥")

cat_01 = Cat("崽崽",3,"母")
print(f'今天{cat_01.name}{cat_01.age}岁生日呀')

# cat_01.eat()
# cat_01.play()
Cat.eat()
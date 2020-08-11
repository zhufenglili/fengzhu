def aa():
    print('这是一个方法')

def bb ():
    print('这是第二个方法')

class Cc:
    def __init__(self,name):
        self.name = name
    def dd(self):
        print('我是弟弟')
O = Cc("哦哦")

class Ff(Cc):
    def __init__(self):
        self.ddd = 100
        


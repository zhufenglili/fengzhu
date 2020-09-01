import random
b = random.randint(0,8)
def test_1():
    while True:
        if (b >= 1) or (b <= 5):
            print('周一到周五')
        elif (b >=6) or(b <= 7):
            print('周末')
        elif b == 0:
            break
        else:
            print('输入有误')

test_1()
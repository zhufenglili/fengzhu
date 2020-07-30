def fight():
    my_hp = 1000
    my_power = 200
    you_hp = 1000
    you_power = 180

    while True:
        my_hp = my_hp - you_power
        you_hp = you_hp - my_power
        if my_hp <= 0:
            print('我输了')
            break
        elif you_hp <= 0:
            print('你输了')
            break

fight()


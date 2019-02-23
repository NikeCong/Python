
import random


class Person:
    def __init__(self,name,status):
        self.name = name
        self.life=100
        self.status=status

    def __str__(self):
        return "%s当前状态为%s，当前的生命值为%d"%(self.name, self.status, self.life)


class Hero(Person):
    def fire(self, aim):
        damage = random.randint(10,30)
        print("%s向%s开火，造成了%d的伤害"%(self.name, aim.name, damage))
        aim.life=aim.life-damage

        if aim.life <= 0:
            aim.life = 0

        if aim.life >=60 and aim.life <100:
            aim.status="轻伤"
        elif aim.life >= 20 and aim.life < 60:
            aim.status="重伤"
        elif aim.life > 0 and aim.life <20:
            aim.status = "超重伤,快挂了"
        elif aim.life <= 0:
            aim.status = "挂了"


class IS(Person):
    def fire(self,aim):
        damage=random.randint(1,5)
        print("%s向%s开火，造成了%d的伤害"%(self.name, aim.name, damage))
        aim.life=aim.life-damage

        if aim.life <= 0:
            aim.life=0

        if aim.life >=60 and aim.life <100:
            aim.status="轻伤"
        elif aim.life >= 20 and aim.life < 60:
            aim.status="重伤"
        elif aim.life > 0 and aim.life <20:
            aim.status = "超重伤,快挂了"
        elif aim.life <= 0:
            aim.status = "挂了"

def main():
    h=Hero("【英雄】","满血")
    is1 = IS("【恐怖分子1】","满血")
    is2 = IS("【恐怖分子2】","满血")
    is3 = IS("【恐怖分子3】","满血")

    while True:

        x = random.randint(1, 3)

        if x == 1:
            h.fire(is1)
        elif x == 2:
            h.fire(is2)
        elif x == 3:
            h.fire(is3)

        is1.fire(h)
        is2.fire(h)
        is3.fire(h)
        print(h)
        print(is1)
        print(is2)
        print(is3)

        if h.life<=0:
            print("%s死亡，游戏结束"%h.name)
            break
        if is1.life<=0 and is2.life<=0 and is3.life<=0:
            print("%s全部死亡，游戏结束"%is1.name)
            break

if __name__ == '__main__':
    main()
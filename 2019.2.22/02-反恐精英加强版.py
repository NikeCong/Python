"""
演示反恐精英案例
对一个匪徒
分析：
1.定义人类，描述公共属性 life:100  name:姓名要传参
2.定义出英雄与恐怖分子类
3.定义主函数描述枪战过程 main，创建两个对象
4.定义开枪方法，分成两个方法，Hero Is都有
    定义的方法要传入被射击的对象
    被射击对象的生命值要进行减少
5.主程序中调用开枪操作
6.开枪操作后，要在主程序中显示每个人的状态信息
7.定义Person类的__str__方法，用于显示每个人的状态
8.设置开枪操作为反复操作
    再设置停止条件：一方生命值<=0
    停止循环使用break
"""
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
        damage = 20
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
        damage=2
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
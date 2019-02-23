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


class Person:
    def __init__(self, name):
        self.name = name
        self.life=100

    def __str__(self):
        return "%s当前的生命值为%d"%(self.name, self.life)


class Hero(Person):
    def fire(self, aim):
        damage = 40
        print("%s向%s开火，造成了%d的伤害"%(self.name, aim.name, damage))
        aim.life=aim.life-damage

class IS(Person):
    def fire(self,aim):
        damage=10
        print("%s向%s开火，造成了%d的伤害"%(self.name, aim.name, damage))
        aim.life=aim.life-damage

def main():
    h=Hero("【英雄】")
    is1=IS("【恐怖分子】")

    while True:
        h.fire(is1)
        is1.fire(h)
        print(h)
        print(is1)

        if h.life<=0:
            print("%s死亡，游戏结束"%h.name)
            break
        if is1.life<=0:
            print("%s全部死亡，游戏结束"%is1.name)
            break

if __name__ == '__main__':
    main()
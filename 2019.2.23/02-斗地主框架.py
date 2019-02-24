"""
案例斗地主
分析：
1.扑克牌作为对象呈现
2.创建未发牌的牌堆的列表
3.创建三个玩家牌堆的列表
4.创建底牌的元组
5.最原始的牌堆初始化，将54张牌加入到牌堆
6.创建洗牌操作
7.创建发牌操作
"""

import random

class Poke():
    pokes=[]
    player1=[]
    player2=[]
    player3=[]
    last=[]
    def __init__(self,flower,number):
        self.flower=flower
        self.num=number

    def __repr__(self):
        return "%s%s"%(self.flower,self.num)

    @classmethod
    def init_poke(cls):
        flowers=["♥","♣","♠","■"]
        nums=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        boss={"big":"大王","small":"小王"}

        for flower_ in flowers:
            for num_ in nums:
                p=Poke(flower_, num_)
                cls.pokes.append(p)
        cls.pokes.append(Poke(boss["big"],""))
        cls.pokes.append(Poke(boss["small"], ""))

#洗牌
    @classmethod
    def wash_poke(cls):
        for idx in range(54):
            indx = random.randint(0, 53)
            cls.pokes[idx],cls.pokes[indx] = cls.pokes[indx],cls.pokes[idx]
#发牌
    @classmethod
    def send_poke(cls):
        for _ in range(17):
            cls.player1.append(cls.pokes.pop(0))
            cls.player2.append(cls.pokes.pop(0))
            cls.player3.append(cls.pokes.pop(0))
        cls.last = cls.pokes

    @classmethod
    def show(cls):
        print("玩家1:", end="")
        for poke in cls.player1:
            print(poke, end=" ")
        print()
        print("玩家2:", end="")
        for poke in cls.player2:
            print(poke, end=" ")
        print()
        print("玩家3:", end="")
        for poke in cls.player3:
            print(poke, end=" ")
        print()
        print("底牌:", end="")
        for poke in cls.last:
            print(poke, end=" ")
        print()

def main():
    Poke.init_poke()
    Poke.wash_poke()
    Poke.send_poke()
    Poke.show()

if __name__ == '__main__':
    main()
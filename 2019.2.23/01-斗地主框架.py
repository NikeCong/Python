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


class Poke():
    pokes=[]
    player1=[]
    player2=[]
    player3=[]

    def __init__(self,flower,number):
        self.flower=flower
        self.num=number

    #def __str__(self):
     #   return "%s%s"%(self.flower,self.num)
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
        print(cls.pokes)
        print(cls.pokes[0])

    def wash_poke(self):
        pass

    def send_poke(self):
        pass

    @classmethod
    def show(cls):
        for poke in cls.pokes:
            print(poke, end=" ")


def main():
    Poke.init_poke()
    Poke.show()

if __name__ == '__main__':
    main()
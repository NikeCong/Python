"""
1. 定义一个Person类,类中要有初始化方法,方法中要有人的姓名和年龄属性
2. 将类中的姓名是公有属性，年龄是私有属性.
3. 提供获取私有属性的公有方法 get_age方法.
4. 提供可以设置私有属性的方法 set_age方法，要求如果输入的年龄在 0 -- 100 之间，设置年龄，否则，提示输入不正确，.
5. 重写 __str__ 要求打印对象时，把 姓名和年龄都打印出来。
"""

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return "姓名：%s，年龄：%d"%(self.name,self.__age)

def main():
    name=input("姓名：")
    lao_wang = Person(name)
    age = int(input("年龄："))
    if age >= 0 and age<= 100 :
        lao_wang.set_age(age)
    else:
        print("年龄输入范围错误")
    print(lao_wang)

if __name__ == '__main__':
    main()
"""【代码题】
声明一个列表如：my_list = ["hello","python","itcast","hello"]　,练习 对列表的 增删改查统计的操作
"""
# my_list = ["hello","python","itcast","hello"]
# my_list.append("heihei")
# print(my_list)
# my_list.insert(1,"wa")
# print(my_list)
# my_list.remove("itcast")
# print(my_list)
# temp=my_list.pop(1)
# print(temp)
# print(my_list)
"""
【代码题】
使用 for in 和 while 循环 二种方式 遍历列表["hello","python","itcast","world"]
"""
# my_list=["hello","python","itcast","world"]

# for i in my_list:
#     print(i)

# i=0
# while True:
#     length=len(my_list)
#     if i<length:
#         print(my_list[i])
#         i += 1
#     else:
#         break
"""
【代码题】
声明一个字典，练习字典的常用的操作
"""
# dict1={"name":"hello","age": 20,"address":"beijing"}
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1.popitem())
# print(dict1.pop("name"))
# print(dict1)
"""
【代码题】
手工输入5个学生的名字，存储到列表中，然后随机获得一名学生，打印学生姓名
"""
# import random
# students=[]
# for i in range(5):
#     name=input("输入学生名字:")
#     students.append(name)
#
# length=len(students)
# print(students)
# for i in range(3):
#     print(students[random.randint(0, length-1)])

"""
【代码题】
使用循环 手工输入 5 个整数，并将其存入列表，打印出最大值，和 最小值。
"""
# nums=[]
# for i in range(5):
#     num=int(input("输入数字:"))
#     nums.append(num)
#
# print(max(nums))
# print(min(nums))
"""

【代码题】
在控制台输入 3 组个人信息，每个人有姓名和年龄，将信息存入字典中，将字典存入列表。
遍历列表，打印每个人的信息，打印格式如下：
1 张三 20
2 李四 22
3 王五 23
"""
# list1=[]
# for i in range(3):
#     dict1 = {}
#     No=int(input("输入编号 "))
#     name=input("姓名：")
#     age=int(input("年龄："))
#     info={"姓名":name,"年龄":age}
#     dict1["No"]=No
#     dict1["姓名"]=name
#     dict1["年龄"]=age
#     list1.append(dict1)
#     print(list1)
# for temp in list1:
#     info=temp.values()
#     print(info)
"""
【代码题】
编程实现 把一个元素全为数字的列表中的所有偶数加1
"""
# list1=[0,2,4,6,8,9]
#
# for i in list1:
#     if i%2==0:
#         i_copy=i+1
#         idx=list1.index(i)
#         list1.pop(idx)
#         list1.insert(idx,i_copy)
#
# print(list1)
"""
【代码题】
统计元祖中每个元素出现的次数把最终的结果保存到列表中，例如[('a',1),('b',3),('c',5)]。
"""
# tuple0=("a","b","a","p","p","c","o","c","c","c","a")
# list1=[]
# set1=set()
# for i in tuple0:
#     print(i)
#     num=tuple0.count(i)
#     count=(i,num)
#     set1.add(count)
#
# list1=list(set1)
# print(list1)


"""
【代码题】
同时遍历字典的键和值，打印到终端显示。
"""
dict1={"name":"hello","age": 20,"address":"beijing"}
keys=list(dict1.keys())
values=list(dict1.values())

for (key,value) in zip(keys,values):
    print("%s:%s"%(key,value))


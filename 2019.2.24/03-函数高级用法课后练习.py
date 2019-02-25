# 【代码题】
# 使用不定长参数定义一个函数max_min，接受的参数类型是数值，最终返回这些数中的最大值和最小值
#
# def max_min(*args):
#     list1=args
#     max_num=max(list1)
#     min_num=min(list1)
#
#     print("最大值:%d,最小值:%d"%(max_num,min_num))
#
# max_min(1,2,5,6,8,2,1,2,10,9)




# 【代码题】
# 定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，
#
# 需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)
#
# str_list = "helloworldhellopythonhelloc++hellojava"
# def findall(all_str,key_str):
#     idx = 0
#     idxx = 0
#     idx_list=[]
#     while idx != -1:
#         idx=all_str.find(key_str,idxx,len(all_str))
#         idxx=idx+1
#         if idx != -1:
#             idx_list.append(idx)
#     print(tuple(idx_list))
# findall(str_list,"hello")
# 【代码题】
# 使用递归的方法打印出前n个斐波那契数列1,1,2,3,5,8,13....

# def febo(num):
#     if num <= 1:
#         return 1
#     else:
#         return febo(num-1)+febo(num-2)
#
# for i in range(20):
#     print(febo(i),end=" ")
test = [1,2,3]
def add(a):
    a=a+a

add(test)
print(test)
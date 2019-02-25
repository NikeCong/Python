# 【代码题】
# 输入用户信息：
#
#         提示用户输入姓名，对输入的内容进行判断，如果输入中包含数字或特殊符号，提示用户输入不正确，请重新输入。
#
#         如果输入正确，提示用户"您输入的用户名为：xxx"
#
#         提示用户输入年龄，如果输入是 0--100 岁之间的数字，提示用户，您输入的年龄为XX 岁，否则提示用户，您输入的有误，请重新输入
#
# import re
#
# while True:
#     user_name = input("输入用户名:")
#     flag = re.match(r"[a-zA-Z]+$",user_name)
#     if flag == None:
#         print("输入有误，请重新输入")
#     else:
#         age = int(input("输入年龄:"))
#         if age <= 100 and age >= 0:
#             print("您输入的用户名为:%s" % user_name)
#             print("您输入的年龄为:%d岁" % age)
#         else:
#             print("您年龄输入有误请重新输入")


# 【代码题】
# 字符串处理：
#
#         现有字符串 msg = "hello python ni hao" 将其中所有的空格改为下划线，得到新字符串："hello_python_ni_hao"
#
# msg = "hello python ni hao"
# new_msg=msg.replace(" ","_")
# print(new_msg)
#####################################################################
#         现有字符串 msg = "hello python ni hao" 统计字符串"o" 出现的次数和位置
#
# msg = "hello python ni hao"
# print(len(msg))
# count_num=msg.count("o")
# print("o出现的次数:%d"%count_num)
# idx=0
# idxx=0
# for i in range(count_num):
#     idx=msg.find("o",idxx,len(msg))
#     idxx=idx+1
#     print("o出现的位置:%d"%idx)
#########################################################################
#         现有字符串 msg = "hello python ni hao" 删除字符串中所有的空格，并打印结果："hellopythonnihao"
#
# msg = "hello python ni hao"
# new_msg=msg.split(" ")
# length=len(new_msg)
# new_str=""
# for i in range(length):
#     new_str = new_str+new_msg[i]
# print(new_str)
################################################################################
# 【代码题】
# 现有列表 name_list = ["tom","zhangsan","lisi"]，根据列表内容生成字符串："tomzhangsanlisi"
#
# name_list = ["tom","zhangsan","lisi"]
# length=len(name_list)
# new_str=""
# for i in range(length):
#     new_str = new_str+name_list[i]
# print(new_str)
##################################################################################
# 【代码题】
# 使用字符串切片练习：
#
#         现在有字符串：msg = "0123456789"
#
#             1. 截取从 2 ~ 5 位置 的字符串
#
# msg = "0123456789"
# new_msg=msg[2:5]
# print(new_msg)
#             2. 截取从 2 ~ 末尾 的字符串
# msg = "0123456789"
# new_msg=msg[2:]
# print(new_msg)
#             3. 截取从 开始 ~ 5 位置 的字符串
#
# msg = "0123456789"
# new_msg=msg[:5]
# print(new_msg)
#             4. 截取完整的字符串
# msg = "0123456789"
# new_msg=msg[:]
# print(new_msg)
#             5. 从开始位置，每隔一个字符截取字符串
# msg = "0123456789"
# new_msg=msg[0::2]
# print(new_msg)
#             6. 从索引 1 开始，每隔一个取一个
# msg = "0123456789"
# new_msg=msg[1::2]
# print(new_msg)
#             7. 截取从 2 ~ 末尾 的字符串
# msg = "0123456789"
# new_msg=msg[2::]
# print(new_msg)
#             8. 截取字符串末尾两个字符
# msg = "0123456789"
# new_msg=msg[-2::]
# print(new_msg)
#             9. 字符串的逆序
# msg = "0123456789"
# new_msg=msg[::-1]
# print(new_msg)


# 【代码题】
# 字符串清理：
#
#       现有字符串 msg = "hel@#$lo pyt \nhon ni\t hao%$" ，去掉所有不是英文字母的字符，打印结果："请理以后的结果为：hellopythonnihao"

# import re
# msg = "hel@#$lo pyt \nhon ni\t hao%$"
# ret=re.findall(r"[a-zA-Z]",msg)
# length=len(ret)
# new_str=""
# for i in range(length):
#     new_str=new_str+ret[i]
# print(new_str)
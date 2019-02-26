#要求：用户输入用户名，密码后对信息进行校验
#1.用户长度在3-8个字节
#2.用户名只能出现英文和数字
#3.密码长度必须是6位
#4.密码长度必须由纯数字组成

name = input("输入用户名:")
pwd = input("请输入密码:")

class NameInputError(Exception):
    pass

class PwdInputError(Exception):
    pass

def check_user(name,pwd):
    if len(name) <3 or len(name)>8:
        raise NameInputError("用户长度错误")

    if not name.isalnum():
        raise NameInputError("用户名内容输入错误，不能是非数字或字母外的内容")

    if len(pwd) != 6:
        raise PwdInputError("密码长度错误，必须为6位")

    if not pwd.isdigit():
        raise PwdInputError("密码内容错误，必须为全数字")

try:
    check_user(name, pwd)

except NameInputError as error_name:
    print(error_name)
except PwdInputError as error_pwd:
    print(error_pwd)
else:
    print("登录成功")


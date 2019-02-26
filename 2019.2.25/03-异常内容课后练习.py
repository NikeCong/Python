"""【代码题】
按照如下的要求编写代码：

- 定义 input_password 函数，提示用户输入密码

- 如果用户输入长度 < 8，抛出异常

- 如果用户输入长度 >=8，返回输入的密码"""


pwd = input("输入密码:")

class PwdError(Exception):
    pass

def input_password(pwd):
    if len(pwd) < 8:
        raise PwdError("密码长度少于8位")

try:
    input_password(pwd)

except PwdError as pwderror:
    print(pwderror)

else:
    print("密码:%s"%pwd)


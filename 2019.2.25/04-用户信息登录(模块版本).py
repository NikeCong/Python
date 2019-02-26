from excep import ex
from service.servi import check_user

name = input("输入用户名:")
pwd = input("请输入密码:")

try:
    check_user(name, pwd)

except ex.NameInputError as error_name:
    print(error_name)
except ex.PwdInputError as error_pwd:
    print(error_pwd)
else:
    print("登录成功")

import excep.ex

def check_user(name,pwd):
    if len(name) <3 or len(name)>8:
        raise excep.ex.NameInputError("用户长度错误")

    if not name.isalnum():
        raise excep.ex.NameInputError("用户名内容输入错误，不能是非数字或字母外的内容")

    if len(pwd) != 6:
        raise excep.ex.PwdInputError("密码长度错误，必须为6位")

    if not pwd.isdigit():
        raise excep.ex.PwdInputError("密码内容错误，必须为全数字")
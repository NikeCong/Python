# 【代码题】
# 使用单例模式，创建 Teacher类，然后实例对象仅仅初始化一次。
class Teacher:
    __instance = None
    __is_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(Teacher)
        return cls.__instance

    def __init__(self):
        if Teacher.__is_init == False:
            self.workname_list=[]
            Teacher.__is_init=True

    def worker_name(self,name):
        self.workname_list.append(name)

teacher1=Teacher()
teacher1.worker_name("zhangsan")
teacher2=Teacher()
teacher2.worker_name("wangwu")

print(teacher2.workname_list)

class Printer:
    __instance = None
    __is_init = False
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance=object.__new__(Printer)
        return cls.__instance

    def __init__(self):
        if Printer.__is_init == False:
            self.list_task=[]
            Printer.__is_init=True

    def add_task(self,info):
        self.list_task.append(info)

    def print(self):
        print(self.list_task)

class Manager:
    def use_print(self,info,pr):
        pr.add_task(info)

class Staff:
    def use_print(self,info,pr):
        pr.add_task(info)

pr1=Printer()
man1=Manager()
man1.use_print("haha",pr1)

pr2=Printer()
man2=Staff()
man2.use_print("heihei",pr2)

pr3=Printer()
pr3.print()

print(pr1)
print(pr2)
print(pr3)
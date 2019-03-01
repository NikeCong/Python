class computer():
    def __new__(cls, *args, **kwargs):
         pass
    def __init__(self,name):
        self.name = name

cp =computer("nihao")
print(cp.name)
# 【代码题】
# 把一个文件中的内容，复制到另外一个文件中。

# f = open("readme.txt","rb")
# content = f.read()
# f.close()
#
# f1 = open("readme[副本].txt","wb")
# f1.write(content)
# f1.close()



# 【代码题】
# 使用os模块，把文件夹中的所有文件重命名。例如，当前test目录下所有的文件名开头添加new_这个字符串。

# import os
#
# file_names=os.listdir("./origional/")
#
# for file_name in file_names:
#     os.rename("./origional/"+file_name,"./origional/"+"haha"+file_name)

import os

file_names=os.listdir("./origional/")

for file_name in file_names:
    f0 = open("./origional/"+file_name, "rb")
    info=f0.read()
    f0.close()

    f1=open("./copy/"+"new_"+file_name,"wb")
    f1.write(info)
    f1.close()




import os
path=input('请输入文件路径(结尾加上/)：')       
n=0
#获取该目录下所有文件，存入列表中
f=os.listdir(path)
for i in f:
    #设置旧文件名（路径+文件名）
    oldname=path+f[n]
    #设置新文件名
    newname=path+'america'+f[n]
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    n+=1
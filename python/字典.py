#创建字典
import sys

# print({},dict(),type({}),type(dict()))
import os
_name = input('请输入你想看的漫画:')

try:
    os.mkdir('./{}'.format(_name))
except:
    print('已经存在相同的文件夹了,程序无法在继续进行！')
    sys.exit()
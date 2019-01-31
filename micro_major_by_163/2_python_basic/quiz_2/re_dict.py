#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = input()
#这里仅用到了字典的简单操作，请理解eval()直接获得字典变量的方法
dict_a = eval(a)
print(dict_a)
#type(obj.__name__) can get the type of the object
if type(dict_a).__name__ == 'dict':
    for key, value in dict_a.items():
        print("{}:{}".format(value,key))
else:
    print("输入错误")

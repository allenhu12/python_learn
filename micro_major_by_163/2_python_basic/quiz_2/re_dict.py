#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = input()
#这里仅用到了字典的简单操作，请理解eval()直接获得字典变量的方法
dict_a = eval(a)
dict_b = {}
#type(obj.__name__) can get the type of the object
if type(dict_a).__name__ == 'dict':
    for key, value in dict_a.items():
        dict_b[value] = key
    print(dict_b)
else:
    print("输入错误")

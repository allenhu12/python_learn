#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = input()
dict_a = eval(a)

if type(dict_a).__name__ == 'dict':
    for key, value in dict_a.items():
        print("{}:{}".format(value,key))
else:
    print("输入错误")

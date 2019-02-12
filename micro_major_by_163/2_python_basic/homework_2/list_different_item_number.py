#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
列表非同个数计算

描述

获得用户输入的一个列表元素，输出其包含值不同元素的个数。

输入格式

一个具体的列表值。

输出格式

整数

输入输出示例
'''
raw_user_input = input()
ls_input = eval(raw_user_input)
ls_different_item = []
for i in ls_input:
    if i not in ls_different_item:
        ls_different_item.append(i)

print(len(ls_different_item))

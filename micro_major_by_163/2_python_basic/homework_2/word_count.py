#!/usr/bin/python 
# -*- coding: UTF-8 -*-
'''
文本输入统计
描述

输入一段由空格分隔的文本，统计本文中每个单词出现的次数，并以单词:次数形式打印输出。

输入格式

一段文本

输出格式

单词:次数，其中，次数为整数，所有单词按照字母序排列。
'''
txt = input()
d = {}
for w in txt.split():
    d[w] = d.get(w, 0) + 1 
ls = list(d.items())
ls.sort()
for w, c in ls:
    print("{}:{}".format(w,c))

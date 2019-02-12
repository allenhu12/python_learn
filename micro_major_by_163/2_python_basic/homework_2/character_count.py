#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
描述

分析附件data.txt文件的字符分布，即每个字符对应的数量。

按照 字符:数量 显示，每行一个结果，如果没有出现该字节则不显示输出，字符采用Unicode编码升序排列。

输入格式

data.txt文件

输出格式

字符:数量，其中，字符表示为可打印字符，按照升序。
'''
try:
    fs = open('data_character_count.txt', 'r', encoding='utf-8')
    data = fs.read()
    dict_result = {}
    for char in data:
        #if char.isprintable() == True:
        dict_result[char] = dict_result.get(char,0) + 1
    ls = list(dict_result.items())
    ls.sort()
    for i in ls:
        print("{}:{}".format(i[0],i[1]), end="\n")
    fs.close()
except:
    print("open file fail\n")


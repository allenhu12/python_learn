#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
描述

分析附件data.txt文件的字节分布，即每个字节对应的数量。

按照 字节:数量 显示，每行一个结果，如果没有出现该字节则不显示输出，字节采用Unicode编码升序排列。

输入格式

data.txt文件

输出格式

字节:数量，其中，字节表示为可打印字节，按照升序。
'''
#try:
fs = open('data_character_count.txt', 'rb')
data = fs.read()
dict_result = {}
for char in data:
    #if char.isprintable() == True:
    dict_result[char] = dict_result.get(char,0) + 1
ls = list(dict_result.items())
ls.sort()
for i in ls:
    print("{:02X}:{}".format(i[0],i[1]), end="\n")
fs.close()
#except:
#    print("open file fail\n")


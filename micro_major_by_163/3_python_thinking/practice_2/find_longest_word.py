#!/usr//local/bin/python3 
# -*- coding: UTF-8 -*-

import jieba
dict_char_len = {}
max_len_value = 0
ls_result = []

#try:
f = open("白鹿原.txt","r")
ls = jieba.lcut(f.read())
set_content = set(ls)
for i in set_content:
    dict_char_len[i] = len(i)
for value in dict_char_len.values():
    if max_len_value < value:
        max_len_value = value

for key,value in dict_char_len.items():
    if value == max_len_value:
        ls_result.append(key)

ls_result.sort()
#print(ls_result)
print(ls_result[0])

f.close()
#except:
#    print("cannot open file")

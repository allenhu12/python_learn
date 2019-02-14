
#!/usr//local/bin/python3 
# -*- coding: UTF-8 -*-

import jieba
dict_char_len = {}
max_count_value = 0
ls_result = []
maxw = ""

#try:
f = open("白鹿原.txt","r")
ls = jieba.lcut(f.read())

for i in ls:
    if i not in " \n，":
        dict_char_len[i] = dict_char_len.get(i,0)+1


for key,value in dict_char_len.items():
    if max_count_value < value:
        max_count_value = value
        maxw = key
    if max_count_value == value and key > maxw:
        maxw = key


print(maxw,max_count_value)
f.close()

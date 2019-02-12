#!/usr/bin/python 
# -*- coding: UTF-8 -*-
import random
# a, b = eval(input())
# s = ""
# random.seed(a+b)
# for i in range(20):
    # s += chr(random.randint(32, 127))
# print(s)
input_value = input()
print(input_value)
input_str = str(input_value).strip("()")
output_str=''
input_ls = input_str.split(",")
random_ls = []
sum_v = eval(input_ls[0]) + eval(input_ls[1])

random.seed(sum_v)
for i in range(20):
    random_ls.append(random.randint(32,127))

for i in random_ls:
    output_str += chr(i)

print(output_str)




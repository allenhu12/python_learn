#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
'''
'''
import time
user_input = input()
year_ls = user_input.split(',')
start_year = time.strptime(year_ls[0],"%Y年%m月%d日%H点%M分%S秒")
end_year = time.strptime(year_ls[1],"%Y年%m月%d日%H点%M分%S秒")

mktime_start_date = time.mktime(start_year)
mktime_end_date = time.mktime(end_year)

time_diff_in_seconds = 0
if mktime_end_date >= mktime_end_date:
    time_diff_in_seconds = mktime_end_date - mktime_start_date
else:
    time_diff_in_seconds = mktime_start_date - mktime_end_date

print("{}".format(int(time_diff_in_seconds/(3600*24))))

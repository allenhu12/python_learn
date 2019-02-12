#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
'''
'''
import time
user_input = input()
year_ls = user_input.split(',')
start_year = time.strptime(year_ls[0],"%Y-%m-%d %H:%M:%S")
end_year = time.strptime(year_ls[1],"%Y-%m-%d %H:%M:%S")

mktime_start_date = time.mktime(start_year)
print(mktime_start_date)
mktime_end_date = time.mktime(end_year)
print(mktime_end_date)

time_diff_in_mins = 0
time_diff_in_mins = abs(mktime_end_date - mktime_start_date)
print(time_diff_in_mins)
# if mktime_end_date >= mktime_end_date:
    # time_diff_in_seconds = mktime_end_date - mktime_start_date
# else:
    # time_diff_in_seconds = mktime_start_date - mktime_end_date

print("{}".format(int(time_diff_in_mins//(60))))

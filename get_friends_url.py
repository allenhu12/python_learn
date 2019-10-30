#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import re
if __name__ == '__main__':
    print("the number of parameter is {}".format(len(sys.argv)))
    print("the parameters are {}".format(str(sys.argv)))
    
    input_file_name = sys.argv[1]
    print("the input file is {}".format(input_file_name))
    fi = open(input_file_name, 'r')
    txt = fi.read()
    fi.close()
    rule = r'第\d{1,2}集\$magnet.*?&tr'
    ls = re.findall(rule,txt)
    print(ls)
    output_file_name=input_file_name+"_result.txt"
    print("the output file is {}".format(output_file_name))
    fo = open(output_file_name,"w+")
    for _ in ls:
        n = _.replace('&tr','')
        n = n+'\n'
        fo.write(n)
    fo.close()

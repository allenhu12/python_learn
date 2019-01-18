#!/usr/bin/python 
# -*- coding: UTF-8 -*-

'''
description:
    solve the hanoi problem
    汉诺塔问题：有三个柱子A,B,C，在A柱子上有N个圆盘，按从从大到小依次放置。
    现在要把A柱上的圆盘挪到C柱。每次只能移动一个圆盘，不允许出现大盘在小盘
    上的情况，请问需要怎么挪动？

求解：
    采用递归的解法。
    当N=1时，直接从A移动到C即可。
    当N>1时，先把N-1圆盘从A移动到B（借助C为中介）
             然后把最大圆盘从A移动到C
             最后把N-1个圆盘从B移动到C（借助A为中介)
'''

steps = 0
def hanoi(src, mid, dest, N):
    global steps
    if N==1:
        steps +=1
        print("[STEP{: >4}] {}->{}".format(steps,src,dest))
    else:
        hanoi(src,dest,mid,N-1)
        steps +=1
        print("[STEP{: >4}] {}->{}".format(steps,src,dest))
        hanoi(mid,src,dest,N-1)

def main():
    hanoi('A','B','C',3)

if __name__ == '__main__':
    main()
        


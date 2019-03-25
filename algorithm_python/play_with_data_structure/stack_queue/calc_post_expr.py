#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

##########################################################################
#
# Description:
#      input a math expression, calculate the result
# Input:
#       '9+(3-1)*3+10/2'
# Output:
#       '20'
##########################################################################

# dictionary to keep the calculate priority
dict_priority={'+': 0, '-':0, '*': 1, '/': 1, '(': 0, ')': 2}

lt_input = []
lt_stack = []
lt_post = []

def convert_post_expr(result, src):
    top = ''
    result.clear()
    lt_stack.clear()
    for i in src:
        if i in '+-*/()':
            # if the stack is empty, we should insert the 1st element
            if len(lt_stack) == 0 or i == '(' :
                lt_stack.insert(0,i)
            else:
                # if i is ')' we should pop the stack till we match the '('
                if i == ')':
                    j = lt_stack[0]
                    while j != '(':
                        top = lt_stack.pop(0)
                        lt_post.append(top)
                        j = lt_stack[0]
                    if j == '(':
                        lt_stack.pop(0)
                # if i's priority is lower than top's priority, we should keep popping till i's priority is higher than
                # top's priority
                elif dict_priority[i] < dict_priority[lt_stack[0]]:
                    j = lt_stack[0]
                    # even if the top's priority is equal to i's priority, we should pop top
                    while len(lt_stack) > 0 and dict_priority[j] >= dict_priority[i]:
                        top = lt_stack.pop(0)
                        lt_post.append(top)
                        if len(lt_stack) > 0:
                            j = lt_stack[0]
                    lt_stack.insert(0,i)
                else:
                    lt_stack.insert(0,i)
        elif i.isnumeric() == True:
            lt_post.append(i)

    # if the stack is not empty, we should pop the remaining  elements
    for i in lt_stack:
        lt_post.append(i)

def calc_post_expr(src):
    lt_stack.clear()
    temp_str=''
    for i in src:
        if i.isnumeric() == True:
            lt_stack.insert(0,eval(i))
        elif i in '+-*/':
            if len(lt_stack) > 0:
                oprand1 = lt_stack.pop(0)
            if len(lt_stack) > 0:
                oprand2 = lt_stack.pop(0)
            if i == '+':
                result = oprand2 + oprand1
            elif i == '-':
                result = oprand2 - oprand1
            elif i == '*':
                result = oprand2 * oprand1
            elif i == '/':
                result = oprand2 / oprand1
            lt_stack.insert(0, result)
    return lt_stack[0]




if __name__ == '__main__':
    user_input = input()
    lt_input = list(user_input)
    print(dict_priority)

    convert_post_expr(lt_post, lt_input)

    print(calc_post_expr(lt_post))
    #lt_input = ['9', '+', '(', '3', '-', '1', ')', '*', '3', '+', '10', '/', '2']
    #convert_post_expr(lt_post, lt_input)
    #print(lt_post)
    #print(calc_post_expr(lt_post))
    #lt_input = ['(','(','1','+','1',')',')']

    #lt_post.clear()
    #lt_stack.clear()
    #convert_post_expr(lt_post, lt_input)
    #print(lt_post)
    #print(calc_post_expr(lt_post))

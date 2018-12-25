"""
    version:            1.0
    name:               turtle_v1
    functionality:      drawing with turtle lib
"""

import turtle

"""
    main function
"""
def main():
    step = 50
    i = 0
    while(i < 5) :
        draw_star(step)
        i = i + 1
        step = step + 50
    turtle.exitonclick()


'''
    draw star
'''
def draw_star(step):
    i = 0
    while i < 5 :
        turtle.forward(step)
        turtle.right(144)
        i = i + 1

if __name__ == '__main__':
    '''
    '''
    main()



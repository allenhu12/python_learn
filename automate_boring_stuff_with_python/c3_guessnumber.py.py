# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

eggs = random.randint(1,21)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("I am thinking of a number between 1 and 20.")
    while True:
        print("take a guess")
        try:
            your_guess = int(input())
            if your_guess < eggs:
                print("guess higher")
            elif your_guess > eggs:
                print("guess lower")
            else:
                break
        except ValueError:
            print("please input a number")
            continue
    print(eggs)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

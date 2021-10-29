#!/usr/bin/env python3
"""
version:            
name:               
functionality:
1. record the account's password for query
2. c6_py <account> [password]
    2.1 if password is omitted, then copy the account related password into system clipboard or show a error
    2.1 if password is presented, then save or update the account the password in the database
"""
import pyperclip

def main():
    PasswordDict = {}
    IsSave = False
    Account = ''
    Password = ''
    while True:
        temp = input("please input your choice, 1 for query, 2 for save:")
        try:
            choice = int(temp)
        except ValueError:
            print("please input a number for choice:")
            continue
        print('the choice is {}'.format(choice))
        if  choice == 1:
            Account = input("please input account name for query:")
            if Account in PasswordDict.keys():
                print('Account : {}, password : {}'.format(Account, PasswordDict[Account]))
                pyperclip.copy(PasswordDict[Account])
            else:
                print('No account found!')
            IsSave = False
        elif choice == 2:
            Account,Password = input("please input account name and password:").split()
            IsSave = True
        else:
            print('Parameter error!')
            break
        if IsSave == True:
            print('the account is {}, the password is {}'.format(Account, Password))
            PasswordDict[Account] = Password
        else:
            print('the account is {}'.format(Account))
    print(PasswordDict)


if __name__ == '__main__':
    '''
    '''
    main()
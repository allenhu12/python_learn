"""
name:           currency converter
version:        3.0
description:    implement the functionality with function
"""

import turtle

def main():
    currency_str_value = input("please input the currency value with unit (USD or CNY, Q to quit):")
    while currency_str_value != 'Q' :
        currency_converter(currency_str_value)
        currency_str_value = input("please input the currency value with unit (USD or CNY, Q to quit):")
    print("Thank you for using the program!")

def currency_converter(currency_str_value):
    USD_VS_CNY = 6.77
    currency_unit = currency_str_value[-3:]
    currency_len = len(currency_str_value)
    print("the currency unit is :", currency_unit)
    if (currency_unit == "USD"):
        currency_value = currency_str_value[:currency_len - 3]
        print("the USD value is ", currency_value, "USD")
        converted_currency_value = eval(currency_value) * USD_VS_CNY
        print("The CNY value is ", converted_currency_value, "CNY")
    elif (currency_unit == "CNY"):
        currency_value = currency_str_value[:currency_len - 3]
        print("the CNY value is ", currency_value, "CNY")
        converted_currency_value = eval(currency_value) / USD_VS_CNY
        print("The USD value is ", converted_currency_value, "USD")
    else:
        print("Unsupported input!!")
        converted_currency_value = 0
    return converted_currency_value




if __name__ == "__main__":
    main()


        


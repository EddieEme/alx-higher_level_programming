#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            uppercase_str += chr(ord(str[i]) - 32)
        else:
            uppercase_str += str[i]
    print("{}".format(uppercase_str), end='')
    print()

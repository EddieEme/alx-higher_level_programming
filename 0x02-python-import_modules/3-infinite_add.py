#!/usr/bin/python3
if __name__ == "__main__":
    """addition of all arguments"""
    import sys


arg = sys.argv

count = len(arg) - 1
sum = 0
for i in range(1, len(arg)):
    sum = sum + int(arg[i])
print("{}".format(sum))

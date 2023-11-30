#!/usr/bin/python3
if __name__ == "__main__":
    import sys


arg = sys.argv

count = len(arg) - 1

if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("{} arguments:".format(count))
else:
    print("{}: {}".format(i, arg[i]))

for i in range(1, len(arg)):
    print("{}: {}".format(i, arg[i]))

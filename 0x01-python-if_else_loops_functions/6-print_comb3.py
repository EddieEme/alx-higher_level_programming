#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i < 10 and j < 10:
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
                break
            else:
                print("{}{}, ".format(i, j), end="")

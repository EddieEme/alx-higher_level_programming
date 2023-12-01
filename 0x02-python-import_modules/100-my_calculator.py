#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

args = sys.argv
count = len(sys.argv) - 1
ops_dic = {"+": add, "-": sub, "*": mul, "/": div}

if count != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = args[2]
if operator not in list(ops_dic.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(args[1])
b = int(args[3])
print("{} {} {} = {}".format(a, operator, b, ops_dic[operator](a, b)))

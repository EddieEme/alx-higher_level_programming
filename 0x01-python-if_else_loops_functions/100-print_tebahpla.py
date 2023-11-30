#!/usr/bin/python3
# for i in range(ord('z'), ord('A') - 1, -1):
#   if 91 <= i <= 96:
#     continue
#   print(chr(i) if i % 2 == 0 else chr(i - 32), end="")

for i in range(ord('z'), ord('A') - 1, -1):
    converted_char = chr(i) if i % 2 == 0 else chr(i - 32)
    if 91 <= ord(converted_char) <= 96:
        continue
    print(converted_char, end="")
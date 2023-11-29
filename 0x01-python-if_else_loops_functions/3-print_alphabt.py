#!/usr/bin/python3
for i in range(97, 123):
    if (i == 101) or (i == 113):
        continue
    print(chr(i).format(), end="")
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in ('q', 'e'):
        print(chr(i), end="")

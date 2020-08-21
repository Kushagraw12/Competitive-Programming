# A WORD

import sys
input = sys.stdin.readline


def low(s):
    cl = 0
    for i in s:
        if i.isupper():
            cl += 1
    return cl


def up(s):
    cu = 0
    for i in s:
        if i.islower():
            cu += 1
    return cu


s = input()
cu = up(s)
cl = low(s)
if cu > cl:
    print(s.lower())
elif cu == cl:
    print(s.lower())
else:
    print(s.upper())

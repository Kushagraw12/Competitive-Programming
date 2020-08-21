# STONES ON THE TABLE

import sys
input = sys.stdin.readline

n = int(input())
s = input()
c = 0
for i in range(len(s) - 1):
    if s[i:i + 1] == s[i + 1:i + 2]:
        c += 1
print(c)

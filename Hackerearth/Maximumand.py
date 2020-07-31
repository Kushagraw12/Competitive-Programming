# KUSHAGRA WADHWA
# MAXIMUM AND

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    if a == b - 1:
        print(a & b)
    elif b & 1 == 0:
        print(b - 2)
    else:
        print(b - 1)

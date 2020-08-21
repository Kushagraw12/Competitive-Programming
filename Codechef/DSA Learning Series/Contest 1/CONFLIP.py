# KUSHAGRA WADHWA
# COIN FLIP

import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    g = int(input())
    for p in range(g):
        i, n, q = map(int, input().strip().split())
        if n % 2 == 0 or i == q:
            print(n // 2)
        else:
            print((n // 2) + 1)

# PANORAMIX'S PREDICTION

import sys
input = sys.stdin.readline


def ispr(m):
    c = 0
    for i in range(1, m + 1):
        if m % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False


n, m = map(int, input().strip().split())
flag = 0
c = ispr(m)
if c:
    for i in range(n, m):
        if ispr(i):
            flag += 1
    if flag == 1:
        print('YES')
    else:
        print("NO")
else:
    print('NO')

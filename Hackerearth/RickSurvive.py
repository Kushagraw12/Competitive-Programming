# KUSHAGRA WADHWA
# WILL RICK SURVIVIE OR NOT

import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    r = 0
    f = 0
    count = 0
    n = int(input())
    walkers = list(map(int, input().strip().split()))
    heapq.heapify(walkers)
    f = True
    c = 0
    l = 0
    while len(walkers) > 0:
        temp = heapq.heappop(walkers)
        if temp <= l:
            f = False
            break
        else:
            l += 1
            c += 1
        if c % 6 == 0:
            l += 1

    if f:
        print('Rick now go and save Carl and Judas')
    else:
        print('Goodbye Rick')
        print(c)

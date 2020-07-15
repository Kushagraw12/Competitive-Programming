import sys
from math import ceil, log

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    proxy_x = x
    count_pat = list(map(int, input().split()))[: n]
    count_pat.sort()
    proxy_pat = [a for a in count_pat]
    d1 = 0
    d2 = 0
    src = 0
    uptop = len(count_pat)

    while src < uptop and count_pat[src] < x:
        src += 1
    proxy_src = src

    if src > 0:
        proxy_src = src - 1
    front = src
    back = src - 1

    while front < uptop:
        d1 += 1
        if x >= count_pat[front]:
            x = count_pat[front]
            count_pat[front] = 0
            front += 1
        x = x << 1

    while back >= 0:
        d1 += 1
        if x >= count_pat[back]:
            x = count_pat[back]
            count_pat[back] = 0
            back -= 1
        x = x << 1

    front = proxy_src
    back = proxy_src - 1

    while front < uptop:
        d2 += 1
        if proxy_x >= proxy_pat[front]:
            proxy_x = proxy_pat[front]
            proxy_pat[front] = 0
            front += 1
        proxy_x = proxy_x << 1

    while back >= 0:
        d2 += 1
        if proxy_x >= proxy_pat[back]:
            proxy_x = proxy_pat[back]
            proxy_pat[back] = 0
            back -= 1
        proxy_x = proxy_x << 1

    print(min(d1, d2))

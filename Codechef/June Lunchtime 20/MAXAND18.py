import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = max(a)
    l = len(bin(m)) - 2
    b = []
    for i in range(l):
        s = 0
        for j in a:
            st = bin(j)[2:]
            if len(st) >= i+1:
                s += (2 ** i) * int(st[len(st) - 1 - i])
        b.append(s)
    s = 0
    l = len(b)
    if k >= l:
        print(2 ** k - 1)
        continue
    for i in range(k):
        ind = b.index(max(b))
        s += 2 ** ind
        b[ind] = -1
    print(s)

import sys
input = sys.stdin.readline


def check(n):
    p = 1
    for i in range(1, len(n)):
        if n[i - 1] > n[i] or n[i - 1] < n[i]:
            p += 1
    if p == len(n):
        return 1
    else:
        return 0


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = a
    b.sort()
    count = 0
    c = []
    k = []
    ans = []
    c.append(min(b))
    for i in range(1, len(b)):
        if b[i] > b[i-1]:
            c.append(b[i])
        else:
            k.append(b[i])
    k.sort(reverse=True)
    ans = c + k
    if check(ans):
        print('YES')
        print(' '.join(map(str, ans)))

    else:
        print('NO')

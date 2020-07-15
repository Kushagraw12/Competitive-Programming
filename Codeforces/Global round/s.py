# cook your dish here
import sys
input = sys.stdin.readline


def MEX(a, m):
    counter = 0
    for i in range(1, len(a)):
        if m in a:
            continue
        else:
            if i < max(a):
                counter += 1
    if counter == 0:
        return 0, counter
    else:
        return 1, counter


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ne = -1
    count = 0
    e = 0
    for i in range(1, n):
        e, count = MEX(a, m)

    if e:
        print(count)
    else:
        print(ne)

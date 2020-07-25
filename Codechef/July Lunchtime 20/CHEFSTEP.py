import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    d = list(map(int, input().strip().split()))[:n]
    a = [][:n]
    for i in range(n):
        if ((d[i] % k) == 0):
            a.append("1") 
        else:
            a.append("0")
    for j in range(n):
        print(a[j], end="")
    print()
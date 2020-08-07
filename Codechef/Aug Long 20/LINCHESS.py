import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -1
    m = (10 ** 9 + 7)
    for i in range(n):
        if k % a[i] == 0:
            if (k // a[i]) < m:
                m = a[i]
                ans = a[i]
                
    print(ans)
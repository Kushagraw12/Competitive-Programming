import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i < (n - 1):
            temp = abs(abs(s[i]) - abs(s[i+1])) - 1
            count += temp
    print(count)

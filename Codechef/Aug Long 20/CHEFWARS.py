import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    h, p = map(int, input().strip().split())
    while p > 0 and h > 0:
        h -= p 
        p //= 2 
        
    if h <= 0:
        print("1")
    else:
        print("0")
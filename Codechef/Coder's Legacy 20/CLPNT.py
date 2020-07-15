import sys
input = sys.stdin.readline

def bin_search(a, l, r, x):
    while l <=r:
        c1 = 0
        mid = l + (r - l) // 2 
        if a[mid] == x:
            return -2 
        elif a[mid] < x:
            l = mid + 1 
        else:
            r = mid - 1 
    
    return (l - 1)
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split())
        ans = bin_search(a, 0, len(a) - 1, x + y)
        print(ans + 1)
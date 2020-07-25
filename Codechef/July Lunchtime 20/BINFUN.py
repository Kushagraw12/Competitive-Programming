import sys
input = sys.stdin.readline
def BinaryConcatenation(X, Y):
        bx = bin(X)[2:]
        by = bin(Y)[2:]
        bxy = bx + by
        byx = by + bx
        return (int(bxy, 2) - int(byx, 2))
        
t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().strip().split()))
    #ans = []
    #k.sort()
    if n < 500:
        max_v = 0 
        for i in range(n):
            for j in range(n):
                tmp = abs(BinaryConcatenation(k[i], k[j]))
                if tmp > max_v:
                    max_v = tmp
    else:
        x = max(k)
        max_v = 0
        for i in range(n):
            tmp = abs(BinaryConcatenation(x, k[i]))
            if tmp > max_v:
                max_v = tmp
    
    print(max_v)
    
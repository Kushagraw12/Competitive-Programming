import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip()))
    c = 0
    for i in range(len(a)+1):

        for j in range(i+1, len(a)+1):
            s = a[i:j]
            
            if sum(s) == len(s):
                c += 1 
    
    print(c)
    print()
    



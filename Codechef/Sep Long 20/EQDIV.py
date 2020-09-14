#KUSHAGRA WADHWA
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(int(19))
k = int(input())
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    if n == 0:
        print(0)

    a2 = [int(math.pow((i + 1), k)) for i in range(n)]
    ma = 0
    mi = 0
    a = []

    for j in range(n - 1, -1, -1):
        if ma > mi:
            mi += a2[j]
        else:
            ma += a2[j]
            a.append(j)
    
    s = ["0" for i in range(n)]
    for y in range(len(a)):
        tmp = a[y]
        s[tmp] = "1"
    
    print(int(abs(ma - mi)))
    for u in s:
        print(int(u), end='')
        
    print()
    
    
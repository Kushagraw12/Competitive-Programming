import sys
from collections import Counter
#input = sys.stdin.readline
t = int(input())
for _ in range(t):
    #n = int(input())
    #a = list(map(int, input().strip()))
    C = Counter([0])
    k = -1
    count = 0
    input()
    for i, x in enumerate(map(int, input())):
        k += x
        count += C[k-i]
        C[k-i] += 1 
    
    print(count)
    print()
    



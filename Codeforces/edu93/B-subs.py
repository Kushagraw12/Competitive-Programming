import sys
input = sys.stdin.readline
from collections import deque
from heapq import *

t = int(input())
for _ in range(t):
    s = list(map(int, input().strip()))
    a = deque(s)
    ans = []
    i = 0
    while i < len(s):
        if s[i] == 1:
                h = i
                while i < len(s) and s[i] == 1:
                    i += 1 
                hh = i-1 
                ans.append(hh-h+1)
        i += 1 

    ans.sort(reverse = True)
    print(sum(ans[::2]))
    

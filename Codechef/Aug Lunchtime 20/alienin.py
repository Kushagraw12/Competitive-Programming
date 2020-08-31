import sys
from collections import defaultdict, Counter, deque, OrderedDict
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
t = int(input())
for _ in range(t):
        N, D = map(int, input().split())
        A = list(map(int, input().split()))
        low, high = 0, max(A) + D
        A.sort()
        for i in range(100):
                mid = (low + high) / 2
                te, f = mid + A[0], 0
                for i in range(1, N):
                        if te > A[i] + D:
                                f = 1
                                break
                        te = max(A[i] + mid, te + mid)
                if f == 0:
                        low = mid
                else:
                        high = mid
        print(low)

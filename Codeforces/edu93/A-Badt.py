import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
        n = int(input())
       # flag = False

        #store = []
        a = list(map(int, input().split()))

        if a[0] + a[1] <= a[n-1]:
            print(1, " ", 2, " ", n)
        else:
            print('-1')


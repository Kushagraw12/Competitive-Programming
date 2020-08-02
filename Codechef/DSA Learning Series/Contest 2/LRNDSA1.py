# KUSHAGRA WADHWA
# CHEF AND STREET FOOD

import sys
import math
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    top = 0
    if n > 1:
        while n > 0:
            x = [int(i) for i in input().split(' ')]
            a = math.floor(x[1] / (x[0] + 1)) * x[2]
            if a > top:
                top = a
            n -= 1
        print(top)
    else:
        print('0')

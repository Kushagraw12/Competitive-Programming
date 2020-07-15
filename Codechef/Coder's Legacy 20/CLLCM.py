import sys
import math
input = sys.stdin.readline

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

t = int(input())
for _ in range(t):
   # flag = True
    #count = 0
    n = int(input())
    a = list(map(int, input().split()))
    ans = LCMofArray(a)
    if ans % 2 != 0:
        print('YES')
    else:
        print('NO')
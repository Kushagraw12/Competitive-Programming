import sys
from math import gcd
input = sys.stdin.readline

def compute_lcm(x, y):
        if x > y:
                greater = x
        else:
                greater = y
        while(True):
                if((greater % x == 0) and (greater % y == 0)):
                        lcm = greater
                        break
                greater += 1
        return lcm

t = int(input())
for _ in range(t):
        n, m = map(int, input().split())
        print(n * m // gcd(n, m))

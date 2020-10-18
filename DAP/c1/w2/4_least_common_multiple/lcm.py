# Uses python3
import sys
from math import gcd
input = sys.stdin.readline

def solve(a, b):
        lcm = (a * b) // gcd(a, b)
        return lcm

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

a, b = map(int, input().split())
print(solve(a, b))

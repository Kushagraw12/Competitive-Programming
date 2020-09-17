import sys
import math
input = sys.stdin.readline

def helper(n):
        prev= 0
        cur = 1
        for i in range(n * n + 1):
                prev, cur = cur, (prev + cur) % n
                if prev == 0 and cur == 1:
                        return i + 1

def helper2(n):
        if n <= 1:
                return n
        p = 0
        c = 1
        for _ in range(n - 1):
                p, c = c, p + c
        return c

def solve(n, m):
          rem = n % helper(m)
          return helper2(rem) % m

a, b = map(int, input().split())
print(solve(a, b))

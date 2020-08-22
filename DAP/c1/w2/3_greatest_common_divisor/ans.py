import sys
input = sys.stdin.readline

def solve(a, b):
    if b == 0:
        return a
    a_ = a % b
    return solve(b, a_)

a, b = map(int, input().split())

print(solve(a, b))


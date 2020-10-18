# Uses python3
import sys
input = sys.stdin.readline

def helper(n):
        if n <= 1:
                return n
        p = 0
        c = 1
        for i in range(n - 1):
                p, c = c % 10, (p + c) % 10
        return c


def solve(n):
        nn = (n + 2) % 60
        nl = helper(nn)
        if nl == 0:
                return 9
        else:
                return (nl - 1)

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

n = int(input())
print(solve(n))

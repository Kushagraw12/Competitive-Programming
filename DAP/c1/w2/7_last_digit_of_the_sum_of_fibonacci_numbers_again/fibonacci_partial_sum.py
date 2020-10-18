# Uses python3
# KUSHAGRA WADHWA
import sys

def helper0(n):
        if n <= 1:
                return n
        p = 0
        c = 1
        for _ in range(n - 1):
                p, c = c, p + c
        return c

def helper1(m):
        p = 0
        c = 1
        for i in range(m * m + 1):
                p, c = c, (p + c) % m
                if p == 0 and c == 1:
                        return i + 1


def helper3(n, m):
        rem = n % helper1(m)
        return helper0(rem) % m


def helper4(n):
        if n <= 1:
                return n
        p = 0
        c = 1
        for u in range(n - 1):
                p, c = c % 10, (p + c) % 10
        return c

def solve(n, m):
        if n == m:
                return helper4(n % 60)
        else:
                n %= 60
                m %= 60
                nn = helper3(n + 1, 10) -1
                mm = helper3(m + 2, 10) -1

        return ((mm - nn) % 10)


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline
    from_, to = map(int, input().split())
    print(solve(from_, to))

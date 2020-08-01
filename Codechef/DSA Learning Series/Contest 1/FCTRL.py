# KUSHAGRA WADHWA
# FACTORIAL

import sys
input = sys.stdin.readline


def solve(n):
    count = 0
    k = 5
    while n / k >= 1:
        count += int(n / k)
        k *= 5
    return int(count)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))

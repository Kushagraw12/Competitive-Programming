# KUSHAGRA WADHWA
# FOUR SQUARES

import sys
import math
input = sys.stdin.readline


def solve(n):
    ans = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n and i % 4 != 0:
                ans += i
                break
            if i % 4 != 0:
                ans += i
            if (n / i) % 4 != 0:
                ans += (n / i)
    return int(ans)


t = int(input())
while t > 0:
    t -= 1
    x = int(input())
    a = (8 * solve(x))
    print(a)

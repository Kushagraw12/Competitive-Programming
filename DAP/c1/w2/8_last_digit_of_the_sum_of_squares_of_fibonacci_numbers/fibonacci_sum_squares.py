# Uses python3
# KUSHAGRA WADHWA
from sys import stdin
input = stdin.readline

def solve(n):
        if n <= 1:
                return n
        p = 0
        c = 1
        a = []
        for i in range(n - 1):
                a.append(p + c)
                p, c = c, p + c
#                print("C", c)
        for j in range(len(a)):
                a[j] *= a[j]

        ans = sum(a) + 1
 #       print(ans, "ANS")
        return ans % 10

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum_      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
  #      print("CUR", current)
        sum_ += current * current
   #     print("SUM", sum_)
    return sum_ % 10

n = int(input())
#print(fibonacci_sum_squares_naive(n), "NAIVE")
print(solve(n))

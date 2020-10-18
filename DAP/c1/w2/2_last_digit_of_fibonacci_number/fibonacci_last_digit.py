# Uses python3
import sys
input = sys.stdin.readline

def solve(n):
        n1 = 0
        n2 = 1
        a = []
        for i in range(n - 1):
                a.append(n1 + n2)
                n1, n2 = n2, n1 + n2
        if len(a) != 0:
                return (max(a) % 10)
        else:
                return 0


n = int(input())
print(solve(n))

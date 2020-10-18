import sys

input = sys.stdin.readline

def solve(n):
        n1 = 0
        n2 = 1
        arr = []
        for i in range(n-1):
            arr.append(n1 + n2)
            n1, n2 = n2, n1 + n2
        if len(arr) != 0:
                return max(arr)
        else:
                return 0

n = int(input())
print(solve(n))


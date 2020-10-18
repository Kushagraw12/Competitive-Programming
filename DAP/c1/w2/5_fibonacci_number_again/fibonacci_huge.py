# Uses python3
import sys

def solve(n, m):
        n1 = 0
        n2 = 1
        a = []
        for i in range(n - 1):
                a.append(n1 + n2)
                n1, n2 = n2, n1 + n2
        if len(a) != 0:
                return (max(a) % m)
        else:
                return 0

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(solve(n, m))

import sys
input = sys.stdin.readline


def add(a, b):
    a += b
    return a, b


def addb(a, b):
    b += a
    return a, b


t = int(input())
for _ in range(t):
    a, b, n = list(map(int, input().split()))
    counter = 0
    while True:
        if a < b and b <= n:
            a, b = add(a, b)
        elif b < a and a <= n:
            a, b = addb(a, b)
        counter += 1
        if a > n or b > n:
            break
    print(counter)

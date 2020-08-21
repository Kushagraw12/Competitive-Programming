# KUSHAGRA WADHWA
# PENALTY SHOOT-OUT 2

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = b = 0
    c1 = c2 = 0
    for i in range(2 * n):
        if i % 2 == 0:
            c1 += 1
            if s[i] == '1':
                a += 1
        else:
            c2 += 1
            if s[i] == '1':
                b += 1
        if a > b + n - c2:
            print(i + 1)
            break
        if b > a + n - c1:
            print(i + 1)
            break
    else:
        print(2 * n)

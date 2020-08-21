# PERFECT PERMUTATIONS

import sys
input = sys.stdin.readline

n = int(input())
if n % 2 == 1:
    print('-1')
else:
    print("2 1 ", end="")

    for i in range(3, n, 2):
        print(str(i + 1) + " " + str(i), end=" ")

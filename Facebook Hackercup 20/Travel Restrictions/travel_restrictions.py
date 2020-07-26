# AUTHOR: KUSHAGRA WADHWA

import sys
input = sys.stdin.readline
with open('travel_restrictions_input.txt', 'r') as inp:
    input = inp.readline
    with open('travel_restrictions_output.txt', 'w') as f:
        t = int(input())
        for test in range(1, t + 1):
            n = int(input())
            I = input()
            O = input()
            counter = 1
            ans = [[0 for w in range(n)] for j in range(n)]
            for w in range(n):
                ans[w][w] = 3
            print('Case #' + str(test) + ": ", end="", file=f)
            for w in range(n):
                if I[w:w + 1] == 'Y':
                    if w - 1 >= 0:
                        ans[w - 1][w] |= 1
                    if w + 1 < n:
                        ans[w + 1][w] |= 1

            for w in range(n):
                if O[w:w + 1] == 'Y':
                    if w - 1 >= 0:
                        ans[w][w - 1] |= 2
                    if w + 1 < n:
                        ans[w][w + 1] |= 2

            for w in range(n):
                for j in range(n):
                    ans[w][j] //= 3

            for k in range(n):
                for j in range(n):
                    for h in range(n):
                        ans[j][h] |= ans[j][k] & ans[k][h]

            for w in range(n):
                print(file=f)
                for j in range(n):
                    if ans[w][j] == 1:
                        print('Y', end="", file=f)
                    else:
                        print("N", end="", file=f)
            print(file=f)

# KUSHAGRA WADHWA
# 04-09-2020

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(19))
testcase = int(input())
for _ in range(testcase):
        n = int(input())
        m = []
        for i in range(n):
                a = list(map(int, input().split()))
                m.append(a)
#        m.sort(reverse = True)
        print(m)

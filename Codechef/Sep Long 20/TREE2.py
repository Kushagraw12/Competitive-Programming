# KUSHAGRA WADHWA
# 04-09-2020

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(19))
testcase = int(input())
for _ in range(testcase):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse = True)
        ans = 0
        for c, num in enumerate(a):
                if c != 0:
                        if num < num2:
                                ans += 1
                else:
                        num2 = num
                num2 = num
        if a[-1] != 0:
                ans += 1
        print(ans)

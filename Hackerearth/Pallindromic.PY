# KUSHAGRA WADHWA
# PALLINDROMIC NUMBERS

import sys
input = sys.stdin.readline


def isPalindrome(x):
    for i in range(0, int(len(x) / 2)):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


t = int(input())
for _ in range(t):
    a, b = map(int, input().strip().split())
    ans = 0
    c = 0
    for i in range(a, b + 1):
        if isPalindrome(str(i)):
            c += 1
    print(c)

import sys
input = sys.stdin.readline
import math
test = int(input())
for _ in range(test):
        n = int(input())
        ans = 2 * int(math.sqrt(n / 2))
        print(int(ans))

# KUSHAGRA WADHWA
# BATTLE OF STALINGARD

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().strip().split())
    a = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    b = abs(x4 * (y2 - y3) + x2 * (y3 - y4) + x3 * (y4 - y2))
    c = abs(x1 * (y4 - y3) + x4 * (y3 - y1) + x3 * (y1 - y4))
    d = abs(x1 * (y2 - y4) + x2 * (y4 - y1) + x4 * (y1 - y2))
    s = b + c + d
    if a == s:
        print('INSIDE')
    else:
        print('OUTSIDE')

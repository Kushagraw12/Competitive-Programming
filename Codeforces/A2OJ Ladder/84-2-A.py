# NEARLY LUCKY NUMBER

import sys
input = sys.stdin.readline
n = input()
count = 0
for i in n:
    if i == '7' or i == '4':
        count += 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')

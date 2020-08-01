# KUSHAGRA WADHWA
# CARVANS

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    count = 1
    top = arr[0]

    for i in arr:

        if i < top:
            count += 1
            top = i

    print(count)

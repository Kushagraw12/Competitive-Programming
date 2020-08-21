# KUSHAGRA WADHWA
# MULTIPLE OF THREE

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k, d0, d1 = map(int, input().split())
    tmp = (d0 + d1) % 10
    ans = tmp + d1 + d0
    i = k - 3
    while i > 0:
        tmp = (tmp * 2) % 10
        if tmp == 0:
            break
        elif tmp == 2:
            r = (i // 4) * 20
            if i % 4 == 3:
                ans += r + 14
            elif i % 4 == 2:
                ans += r + 6
            elif i % 4 == 1:
                ans += r + 2
            else:
                ans += r
            break
        else:
            ans += tmp
        i -= 1

    if ans % 3 == 0:
        print('YES')
    else:
        print("NO")

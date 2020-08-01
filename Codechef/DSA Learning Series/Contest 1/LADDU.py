# KUSHAGRA WADHWA
# LADDU

import sys
t = int(input())
for _ in range(t):
    s = input().split()
    n = int(s[0])
    total = 0
    while n > 0:
        act = input().split()
        if act[0] == 'CONTEST_WON':
            if int(act[1]) <= 20:
                total += (300 + (20 - int(act[1])))
            else:
                total += 300
        elif act[0] == 'TOP_CONTRIBUTOR':
            total += 300
        elif act[0] == 'BUG_FOUND':
            total += int(act[1])
        elif act[0] == 'CONTEST_HOSTED':
            total += 50
        n -= 1
    months = 0
    if s[1] == 'INDIAN':
        months = total // 200
    elif s[1] == "NON_INDIAN":
        months = total // 400
    print(months)

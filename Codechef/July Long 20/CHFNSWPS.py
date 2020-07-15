import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    db_t = {}
    db_a = {}
    db_b = {}
    for x in a:
        if x in db_t:
            db_t[x] += 1
        else:
            db_t[x] = 1
        if x in db_a:
            db_a[x] += 1
        else:
            db_a[x] = 1
    for y in b:
        if y in db_t:
            db_t[y] += 1
        else:
            db_t[y] = 1
        if y in db_b:
            db_b[y] += 1
        else:
            db_b[y] = 1

    flag = True
    for check in db_t:
        if db_t[check] % 2 == 1:
            flag = False
    if not flag:
        print(-1)
    else:
        change = {}
        for i in db_t:
            ca = 0
            cb = 0
            if i in db_a:
                ca = db_a[i]
            if i in db_b:
                cb = db_b[i]
            if ca != cb:
                change[i] = int(abs(ca - cb) // 2)
        if len(change) == 0:
            print(0)
        else:
            helper = []
            for temp in change:
                for j in range(change[temp]):
                    helper.append(temp)
            helper.sort()
            ans = 0
            for k in range(int(len(helper) / 2)):
                ans += helper[k]
            print(ans)

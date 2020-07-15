import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    chef = 0
    morty = 0

    a = []
    b = []
    for h in range(n):
        k, l = map(int, input().split())
        a.append(k)
        b.append(l)
    for i in range(n):
        sa = 0
        sb = 0
        lx = str(a[i])
        for j in range(len(lx)):
            x = a[i] % 10
            a[i] //= 10
            sa += x
        ly = str(b[i])
        for u in range(len(ly)):
            y = b[i] % 10
            b[i] //= 10
            sb += y
        if sa > sb:
            chef += 1
        elif sb > sa:
            morty += 1
        else:
            chef += 1
            morty += 1

    if chef > morty:
        print('0', chef)

    elif morty > chef:
        print('1', morty)
    else:
        print('2', chef)

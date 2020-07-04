import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    N = int(input())
    db_x = {}
    db_y = {}
    for i in range(4 * N - 1):
        x, y = map(int, input().split())
        if x in db_x:
            db_x[x] += 1
        else:
            db_x[x] = 1
        if y in db_y:
            db_y[y] += 1
        else:
            db_y[y] = 1
    vertex = []
    for x in db_x:
        if db_x[x] % 2 == 1:
            vertex.append(x)
            break
    for y in db_y:
        if db_y[y] % 2 == 1:
            vertex.append(y)
            break
    print(vertex[0], vertex[1])

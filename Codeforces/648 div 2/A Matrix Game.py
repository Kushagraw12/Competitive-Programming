def solve(a):
    row = len(a) - sum([1 if sum(row) > 0 else 0 for row in a])
    col = len(a[0]) - sum([1 if sum([row[i] for row in a])
                           > 0 else 0 for i in range(len(a[0]))])
    minrc = min(row, col)
    if minrc % 2:
        return "Ashish"
    return "Vivek"


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = solve(a)
    print(ans)

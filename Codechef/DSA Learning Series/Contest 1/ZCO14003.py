# KUSHAGRA WADHW
# SMARTPHONE

try:
    n = int(input())
    bud = list()
    rev = list()
    for i in range(n):
        bud.append(int(input()))
    bud.sort()

    for j in range(n):
        rev.append((bud[n - 1 - j] * (j + 1)))
    print(max(rev))

except:
    pass

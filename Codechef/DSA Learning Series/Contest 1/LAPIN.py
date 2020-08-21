# KUSHAGRA WADHWA
# LAPINDROMES

n = int(input())
for i in range(0, n):
    a = input()
    k = 0
    if len(a) % 2 != 0:
        k = 1
    a1 = a[:len(a) // 2]
    a2 = a[len(a) // 2 + k:]
    if sorted(a1) == sorted(a2):
        print('YES')
    else:
        print('NO')

matrix = list()

for i in range(5):
    num = list(map(int, input().split(" ")))
    matrix.append(num)

for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            count = abs((r-2)) + abs((c-2))
print(count)

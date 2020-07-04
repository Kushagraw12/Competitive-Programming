import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    print("O", end='')
    k -= 1
    for x in range(1, 9):
        for y in range(1, 9):
            if x == 1 and y == 1:
                continue
            elif k:
                k -= 1
                print(".", end="")
            else:
                print("X", end="")
        print()
    print('\n')

import sys
input = sys.stdin.readline
n, x = map(int, input().strip().split())
x *= 60
count = 0
flag = True
for i in range(1, n + 1):
    for j in range(2, n):
        count += 30

# print(count)
if count > x:
    flag = False

if flag:
    print("1")
else:
    print("0")

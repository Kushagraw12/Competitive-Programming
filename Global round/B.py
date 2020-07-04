import sys
input = sys.stdin.readline

k = int(input())
ans = ["c", "o", "d", "e", "f", "o", "r", "c", "e", "s"]
if k > 1:
    for i in range(1, k):
        ans.append('s')
print(''.join(ans))

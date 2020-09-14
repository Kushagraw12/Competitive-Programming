# KUSHAGRA WADHWA
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(19))
testcase = int(input())
for _ in range(testcase):
    N = int(input())
    matrix = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)
    ans = 0
    for j in range(N - 1, -1, -1):
        if ans % 2 == 0 and matrix[j][0] == (N * j + 1):
                continue
        elif ans % 2 == 1 and matrix[0][j] == (N * j + 1):
                continue
        ans += 1
    print(ans)

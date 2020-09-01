import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
        ans = "Yes"
        n = int(input())
        s = list(map(int, input().split()))
        d = {}
        for i in s:
                try:
                        d[i] = d[i] + 1
                        ans = "No"
                        break
                except:
                        d[i] = 1
        print(ans)

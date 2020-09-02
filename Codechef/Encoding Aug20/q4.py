import sys
#input = sys.stdin.readline

def solve(l, h):
        if l > h: return None
        mid = (l + h) >> 1
        if not helper(mid):
                return solve(l, mid - 1)
        ans = solve(mid + 1, h)
        return mid if ans is None else ans

def helper(q):
        c = 0
        for x in a:
                c += x // q
        return c >= k


test = int(input())
for _ in range(test):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(1, int(1e9)) or 0)

#KUSHAGRA WADHWA

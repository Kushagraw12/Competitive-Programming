import sys
import resource
input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

def solve(u):
        global graph, vis
        vis.add(u)
        for i in graph[u]:
                if i not in vis:
                        solve(i)

test = int(input())
for _ in range(test):
        #n, m = map(int, input().split())
        n, m = ip()
        graph = {i: [] for i in range(n)}
        for i in range(m):
                a, b = ip()
                graph[a].append(b)
                graph[b].append(a)
        ans = 0
        vis = set()
        for i in range(n):
                if i not in vis:
                        solve(i)
                        ans += 1
        print(ans)

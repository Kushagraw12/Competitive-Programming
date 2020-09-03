# KUSHAGRA WADHWA 
# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(u = 1, p = 0):
        pp[u] = p
        for v in graph[u]:
                if v != p:
                        d[u] += dfs(v, u)
        return d[u]


t = int(input())
for _ in range(t):
        n = int(input())
        graph = [list() for i in range(n + 1)]
        d = [1] * (n + 1)
        pp = [0] * (n + 1)
        for i in range(n - 1):
               u, v = map(int, input().split())
               graph[u].append(v)
               graph[v].append(u)
        dfs()
        w = float('inf')
        x = 0
        for k in range(1, n + 1):
                y = n - d[k]
                for v in graph[k]:
                        if pp[k] != v:
                                y = max(y, d[v])
                if y < w:
                        w = y
                        x = k
        print(x, w)

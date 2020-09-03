import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

def df(v, vis, w, s):
        global a, graph
        vis[v] = 1
        #su = 0
        #print(v)
        s += a[v]

        if s > w:
                print("S", s)
                print("S-", s - a[v])
                return a[v]
        for i in graph:
                if vis[v] == 0:
                        df(i, vis, w, s)
def dfs(x, y, z, s):
        global a, araph
        ans = []
        V = len(graph)
        vis = [0] * (V)
        for i in range(x, y):
                if vis[i] == 0:
                        ans.append(df(i, vis, z, s))
        try:
                print(max(ans))
        except Exception:
                print(ans[len(ans) - 1])


N, Q = map(int, input().split())
graph = [list() for i in range(N + 1)]

for i in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

a = list(map(int, input().split()))
print("A", a)
#print("GRAPH:", graph)

for i in range(Q):
        a_, b_, w_ = map(int, input().split())
        s = 0
        dfs(a_, b_, w_, s)


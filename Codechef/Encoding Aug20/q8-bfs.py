import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))


def bfs(x, y, z):
        global graph
        vis = [0] * (len(graph))

        qu = []
        qu.append(x)
        vis[x] = 1

        while qu:
                n = qu.pop(0)
                if n == y:
                        print("REACHED!")

        for i in graph[n]:
                if vis[i] == 0:
                        qu.append(i)
                        vis[i] = 1
        print("NO")

N, Q = map(int, input().split())
graph = [list() for i in range(N + 1)]
#s = 0
for i in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

a = list(map(int, input().split()))
                        #print("A", a)
                        #print("GRAPH:", graph)

for i in range(Q):
        a_, b_, w_ = map(int, input().split())
        bfs(a_, b_, w_)

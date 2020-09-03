import sys
input = sys.stdin.readline
inp, ip = lambda :int(input()), lambda :[int(w) for w in input().split()]

def get_next(e, m):
        global graph
        nad = graph[e]
        d = len(nad) + nad.count(e)
        if d < m:
                return d

def solve(o):
        global graph
        adj = graph[o]
        deg = len(adj) + adj.count(o)
        return deg

for _ in range(int(input())):
        n = int(input())
        graph = {i: [] for i in range(1, n + 1)}
        for i in range(n - 1):
                u, v = ip()
                graph[u].append(v)
                graph[v].append(u)
        print("GRAPH:", graph)
        m = 0
        y = 0
        vis = set()
        for i in graph:
                deg = solve(i)
                if deg > m:
                        m = deg
                        y = graph[i]
                        vis.add(i)
        e = 0
        for i in graph:
                if i not in vis:
                        d = solve(i)
                        if d > e:
                                e = d

        print(list(graph.keys())[list(graph.values()).index(y)], e)


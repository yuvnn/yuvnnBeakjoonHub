import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,n+1):
    g[i].sort()

def dfs(g,v): #재귀
    res=[]
    vis=set()

    def dfs_func(cur):
        res.append(cur)
        vis.add(cur)
        for n in g[cur]: 
            if n not in vis: 
                dfs_func(n)
    dfs_func(v)

    return res

def bfs(g,v):
    res = [v]
    queue = [v]
    vis = {v}
    while queue:
        cur = queue.pop(0)
        for i in g[cur]:
            if i not in vis:
                queue.append(i)
                vis.add(i)
                res.append(i)
    return res

print(*dfs(g,v))
print(*bfs(g,v))


n,m = map(int, input().split())
link = [[] for _ in range(n)]
for _ in range(m):
    i,j = map(int, input().split())
    link[i].append(j)
    link[j].append(i)


def dfs(now,dep):
    if dep == 4:
        print('1')
        exit()
    for ch in link[now]:
        if ch not in vis:
            vis.add(ch)
            dfs(ch,dep+1)
            vis.remove(ch)
    return 0


vis = set()
for i in range(n):
    vis.add(i)
    dfs(i,0)
    vis.remove(i)

print(0)
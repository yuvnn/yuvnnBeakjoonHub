import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int,input().split())
p = [i for i in range(n+1)]

def find(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        p[x] = y
    else:
        p[y] = x

for i in range(m):
    cmd, a, b = map(int,input().split())
    if cmd == 1:
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a,b)
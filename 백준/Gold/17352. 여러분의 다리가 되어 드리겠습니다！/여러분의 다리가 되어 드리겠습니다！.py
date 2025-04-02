import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
p = list(range(n+1))

def find(x):
    if p[x] != x: 
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        p[y] = x
    else:
        p[x] = y

for i in range(n-2):
    a,b = map(int,input().split())
    union(a,b)

for i in range(2,n+1):
    if find(1) != find(i):
        print(1,i)
        break
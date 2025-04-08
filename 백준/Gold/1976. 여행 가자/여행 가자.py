import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
p = [i for i in range(n+1)]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        p[b] = a
    else:
        p[a] = b

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if(tmp[j]):
            union(i+1,j+1)

tmp = list(map(int,input().split()))
tmp2 = p[tmp[0]]
ans = 1
for i in tmp:
    if tmp2!=p[i]:
        ans = 0
        break
print("YES" if ans else "NO")
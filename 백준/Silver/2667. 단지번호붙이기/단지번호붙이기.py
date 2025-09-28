import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(int,str(input().strip()))) for _ in range(n)]
dir = (1,0),(-1,0),(0,1),(0,-1)
ans = 0
cnt = []

def dfs(x,y):
    arr[x][y] = 0 
    cnt[ans] += 1
    for dx, dy in dir:
        nx, ny = dx + x, dy + y
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            cnt.append(0)
            dfs(i,j)
            ans+=1

print(ans)
cnt.sort()
print('\n'.join(map(str,cnt)))

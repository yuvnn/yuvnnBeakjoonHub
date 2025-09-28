import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
tmp = [[0]*n for _ in range(n)]
dir= (1,0),(-1,0),(0,1),(0,-1)

cnt_li = []
for th in range(1,101):
    cnt = 0
    tmp = [[1 if arr[i][j] >= th else 0 for j in range(n)] for i in range(n)]

    def dfs(x,y):
        stack = [(x,y)]
        while stack:
            x,y = stack.pop()
            for dx, dy in dir:
                nx, ny = x+dx, y+dy
                if -1<nx<n and -1<ny<n and tmp[nx][ny]:
                    tmp[nx][ny] = 0
                    stack.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if tmp[i][j]:
                cnt += 1
                dfs(i,j)

    cnt_li.append(cnt)

print(max(cnt_li))
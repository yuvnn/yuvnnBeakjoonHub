from collections import deque

m,n = map(int, input().split())
arr = []
apple = 0
que = deque()
for i in range(n):
    arr.append(list((map(int,input().split()))))
    for j in range(m):
        if  arr[i][j]== 1:
            que.append((i,j))
            apple+=1
        if arr[i][j]==0:
            apple+=1
ans = 0
cnt = len(que)
while que:
    ans+=1
    l = len(que)
    for _ in range(l):
        nx, ny = que.popleft()
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in dir:
            x,y = nx+dx, ny+dy
            if 0<=x<n and 0<=y<m and arr[x][y] == 0:
                arr[x][y] = 1
                que.append((x,y))
                cnt += 1

print(ans-1 if cnt == apple else -1)
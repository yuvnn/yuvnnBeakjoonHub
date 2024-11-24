from collections import deque
from sys import stdin
input = stdin.readline

arr = []
house = []
estate = 0

n = int(input())
for i in range(n):
    arr.append(list(input()))
    if arr[i][-1] != '0' and arr[i][-1] != '1':
        arr[i].pop()
    arr[i]=list(map(int,arr[i]))

for i in range(n):
    if any(arr[i]):
        for j in range(n):
            if arr[i][j]==1:
                dir = [(1,0),(-1,0),(0,1),(0,-1)]
                stack = [(i,j)]
                arr[i][j]=0
                cnt = 0
                while stack:
                    cur = stack.pop()
                    for nx, ny in dir:
                        x,y = nx + cur[0], ny+cur[1]
                        if -1<x<n and -1<y<n and arr[x][y]==1:
                            arr[x][y] = 0
                            stack.append((x,y))
                            cnt +=1
                house.append(cnt+1)
                estate+=1

house.sort()
print(estate)
print(*house,sep='\n')
                        
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
MAP = [[0]*m]

for i in range(1,n+1):
    MAP.append(list(map(int,input().split())))
    for j in range(m):
        MAP[i][j] = MAP[i][j] + MAP[i-1][j]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    print(sum(MAP[x2+1][y1:y2+1])-sum(MAP[x1][y1:y2+1]))

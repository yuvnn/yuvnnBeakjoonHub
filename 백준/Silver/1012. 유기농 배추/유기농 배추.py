from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    ans = 0
    vis = []
    Cabbage = []
    m,n,k = map(int,input().split())
    for _ in range(k):
        i,j = map(int,input().split())
        Cabbage.append((j,i))
    
    def find(start):
        global ans
        vis.append(start)
        stack = [start]
        
        while stack:
            cur = stack.pop()
            diff_x,diff_y= [0,0,1,-1],[1,-1,0,0]
            for i in range(4):
                diff_cur = (cur[0]+diff_x[i], cur[1]+diff_y[i])
                if diff_cur in Cabbage and diff_cur not in vis:
                    stack.append(diff_cur)
                    vis.append(diff_cur)
        
        ans += 1
                
    for c in Cabbage:
        if c not in vis:
            find(c)

    print(ans)
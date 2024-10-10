from collections import deque
from sys import stdin
input = stdin.readline

k,n = (map(int,input().split()))
line = sorted([int(input()) for _ in range(k)])

left, right = 1,line[k-1]

while(left<=right):
    mid = (left+right)//2
    cur = sum(l//mid for l in line)
    if (n <= cur):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(int(ans))





    
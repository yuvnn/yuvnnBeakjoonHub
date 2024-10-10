from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())

left, right = 1,k

while(left<right):
    mid = (left+right)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    if(cnt<k):
        left = mid + 1
    else:
        right = mid

print(right)





    
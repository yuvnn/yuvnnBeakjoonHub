import sys
input = sys.stdin.readline

n= int(input())
li  = sorted([int(input()) for _ in range(n)],reverse=True)
ans = 0
for i, r in enumerate(li,start=1):
    tmp = r - (i-1)
    if tmp>0:
        ans += tmp 

print(ans)
import sys
input = sys.stdin.readline

N = int(input())
rope =sorted([int(input()) for _ in range(N)],reverse=True)
ans = 0
for i in range(N):
    ans =  max(ans,rope[i]*(i+1))
print(ans)
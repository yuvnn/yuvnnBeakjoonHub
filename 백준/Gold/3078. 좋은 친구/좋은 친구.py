from collections import deque
from sys import stdin
input = stdin.readline 

n,k = map(int,(input().split()))
ans = 0
cnt = [0] * 21
que = deque()

for _ in range(k):
    tmp = input().strip()
    ans += cnt[len(tmp)]
    cnt[len(tmp)]+=1
    que.append(len(tmp))

for _ in range(n-k):
    tmp = input().strip()
    ans += cnt[len(tmp)]

    cnt[que.popleft()]-=1
    
    cnt[len(tmp)]+=1
    que.append(len(tmp))

print(ans)
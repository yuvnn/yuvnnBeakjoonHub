import sys
input = sys.stdin.readline
from operator import itemgetter

n = int(input())
li = sorted([tuple(map(int, input().split())) for _ in range(n)], key=itemgetter(1,0))
ans, start, end = 0,0,0
for s,e in li:
    if end<=s:
        start, end = s,e
        ans +=1 
print(ans)

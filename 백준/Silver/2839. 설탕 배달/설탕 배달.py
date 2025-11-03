import sys
input = sys.stdin.readline

n = int(input())

ans = n // 5

for i in range(n,-1,-5):
    tmp = n-(ans*5)
    if tmp%3 == 0:
        ans+=tmp//3
        print(ans)
        exit(0)
    ans -= 1

print(-1)
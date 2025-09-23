import sys
input = sys.stdin.readline

n = int(input())
comb = list(map(int,input().split()))

ans1 = ans2 = ans3 = 0

sum1 = sum2 = sum(comb) - comb[0]
for i in range(1,n-1):
    sum2 -= comb[i]
    ans1 = max(ans1, sum1 + sum2 - comb[i])

sum1 = sum2 = sum(comb) - comb[n-1]
for i in range(n-2,0,-1):
    sum2 -= comb[i]
    ans2 = max(ans2, sum1 + sum2 - comb[i])

ans3 = sum(comb) - comb[0] - comb[n-1] + max(comb[1:-1])


print(max(ans1,ans2,ans3))
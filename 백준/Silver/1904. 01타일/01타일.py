import sys
input = sys.stdin.readline
MOD = 15746

n = int(input())
m=[2,3,0]

for i in range(2,n):
    m[i%3] = (m[(i-1)%3] + m[(i-2)%3]) % MOD

print(m[(n+1)%3] if n!=1 else 1)


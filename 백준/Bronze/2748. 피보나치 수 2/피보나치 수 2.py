import sys
input = sys.stdin.readline

n = int(input())
li = [1]*(n+1)

for i in range(3,n+1):
    li[i] = li[i-1] + li[i-2]

print(li[n])
    
    


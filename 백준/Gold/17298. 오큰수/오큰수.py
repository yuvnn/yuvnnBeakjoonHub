n = int(input())
A = list(map(int, input().split()))

stack = []
ans = [-1] * n

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i] 
    stack.append(i)
    
print(*ans)

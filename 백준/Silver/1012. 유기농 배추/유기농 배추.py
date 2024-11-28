t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    arr = set()
    ans = 0
    for _ in range(k):
        i,j = map(int,input().split())
        arr.add((i,j))

    def find(cur):
        global ans
        stack = [cur]
        while stack:
            nx,ny = stack.pop()
            dir = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in dir:
                x,y = nx+dx,ny+dy
                if (x,y) in arr:
                    arr.remove((x,y))
                    stack.append((x,y))
        ans +=1
    
    while arr:
        find(arr.pop())
    
    print(ans)

        




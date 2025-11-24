import sys
input = sys.stdin.readline

R,C,N = map(int, input().split())
M = [list(input().strip()) for _ in range(R)]


if N % 2 == 0:
    for _ in range(R):
        print('O'*C)
elif N+2 % 4 == 0:
    _ = [print(''.join(i)) for i in M]
else:
    dirs = ((0,0),(0,1),(0,-1),(1,0),(-1,0))
    cnt = 0
    t = 1
    bombs = []
    while (t<N):
        for i in range(R):
            for j in range(C):
                if M[i][j] == 'O':
                    bombs.append((i,j))
        M=[['O' for _ in range(C)] for _ in range(R)]
        t += 1
        while(bombs):
            x,y = bombs.pop()
            for dx,dy in dirs:
                cx ,cy = x+dx, y+dy
                if 0 <= cx < R and 0 <= cy < C:
                    M[cx][cy] = '.'
        t+=1
    _ = [print(''.join(i)) for i in M]
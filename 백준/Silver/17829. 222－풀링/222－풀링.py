import sys
input = sys.stdin.readline

n= int(input())
li = [list(map(int,input().split())) for _ in range(n)]

def f(li,m):
    m = m//2
    if m == 1:
        li = sorted([li[i][j] for i in range(len(li)) for j in range(len(li))])
        return li[-2]
    a1 = f([l[:m] for l in li[:m]],m)
    a2 = f([l[m:] for l in li[m:]],m)
    a3 = f([l[m:] for l in li[:m]],m)
    a4 = f([l[:m] for l in li[m:]],m)
    return f([[a1,a2],[a3,a4]],2)
    

print(f(li,n))
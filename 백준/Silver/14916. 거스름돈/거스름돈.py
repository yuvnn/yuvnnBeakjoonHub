import sys
input = sys.stdin.readline

n= int(input())
a1 = 0
for i in range(n,0,-2):
    if(i%5==0):
        print(a1+i//5)
        exit()
    a1+=1
    
print(-1 if i%2 else a1)   
import sys
input = sys.stdin.readline

from collections import deque
MAX = 100000

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
global blue
global white
blue, white  = 0, 0

def r(m, paper):
    global blue
    global white

    if m == 0:
        return 0
    if all([all(l) for l in paper]):
        blue += 1
        return 0
    if all([not any(l) for l in paper]):
        white += 1
        return 0

    m = int(m/2)
     
    r(m,[row[m:] for row in paper[:m]]) #1
    r(m,[row[m:] for row in paper[m:]]) #2
    r(m,[row[:m] for row in paper[m:]]) #3
    r(m,[row[:m] for row in paper[:m]]) #4

r(n,paper)
print(white)
print(blue)

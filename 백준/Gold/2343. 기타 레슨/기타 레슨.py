import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

s, e = 1, sum(li)
result = 0

def ok(mid):
    cnt = 1
    tmp = mid
    for l in li:
        if l > mid: return 0
        
        tmp = tmp-l
        if tmp < 0:
            cnt +=1
            if cnt > m: return 0
            tmp = mid - l
    return 1
        
    
while s <= e:
    mid = (s + e) // 2
    if ok(mid):
        result = mid
        e = mid - 1
    else:
        s = mid + 1

print(result)
        

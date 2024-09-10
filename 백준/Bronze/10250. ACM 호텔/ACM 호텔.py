T = int(input())
H=[0] * T
W=[0] * T
N=[0] * T
for i in range(T):
    H[i],W[i],N[i] = map(int,(input().split(' ')))

ans = [0] * T
for i in range(T):
    floor = N[i] % H[i]
    floor = H[i] if floor == 0 else floor
    room = (N[i]-1) // H[i] + 1
    if room < 10:
        room = '0' + str(room) 
    ans[i] = str(floor) + str(room)

for i in ans:
    print(i)
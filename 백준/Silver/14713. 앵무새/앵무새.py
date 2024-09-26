n = int(input())
str = []
for i in range(n):
    str.append(list(input().split()))
str2 = list(input().split())

while str2:
    for i in range(n):
        exist = False
        if str[i] and str[i][-1] == str2[-1]:
            exist = True
            str[i].pop()
            str2.pop()
            break
    if not exist:
        break
    
print("Impossible" if str2 or any(str) else "Possible")
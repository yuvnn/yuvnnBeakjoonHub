note = list(map(int,input().split(' ')))
align = [0] * (len(note)-1)
for i in range(len(note)-1):
    align[i] = 1 if note[i] < note[i+1] else 0

if all(align):
    print("ascending")
else:
    m=1
    for i in range(len(align)-1):
        if align[i] != align[i+1]:
            print("mixed")
            break
        m+=1
    if m==len(align):
        print("descending")

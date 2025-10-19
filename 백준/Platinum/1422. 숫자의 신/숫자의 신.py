import sys
input = sys.stdin.readline
from functools import cmp_to_key
def cmp(a : int, b: int)->int:
    sa, sb = str(a), str(b)
    la, lb = len(str(a)),len(str(b))
    for i in range(la + lb):
        na, nb = sa[i%la], sb[i%lb]
        if na != nb:
            return 1 if na < nb else -1
    return 0

k, n  = map(int,input().split())
nums = [int(input()) for _ in range(k)]

nums.sort(key=lambda x: (-len(str(x)), cmp_to_key(cmp)(x)))
nums += [str(nums[0])] * (n - k)

nums.sort(key=cmp_to_key(cmp))
print(''.join(''.join(str(n) for n in nums)))


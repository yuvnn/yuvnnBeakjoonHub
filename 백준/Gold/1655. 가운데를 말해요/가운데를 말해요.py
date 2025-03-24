import sys
import heapq

input = sys.stdin.readline

left_heap = []  #최대힙
right_heap = []  #최소힙

n = int(input())
for _ in range(n):
    tmp = int(input())

    if len(left_heap) == 0:
        heapq.heappush(left_heap, -tmp)
    else:
        if tmp <= -left_heap[0]:
            heapq.heappush(left_heap, -tmp)
        else:
            heapq.heappush(right_heap, tmp)

        if len(left_heap) > len(right_heap) + 1:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
        elif len(left_heap) < len(right_heap):
            heapq.heappush(left_heap, -heapq.heappop(right_heap))

    print(-left_heap[0])

import sys
import heapq
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[0], x[1]))

heap = [arr[0][1]]

for i in range(1, n):
    if heap[0] <= arr[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, arr[i][1])

    
print(len(heap))
n = int(input())

arr = []

for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for s, e in arr:
    if s >= end_time:
        cnt += 1
        end_time = e
    
print(cnt)
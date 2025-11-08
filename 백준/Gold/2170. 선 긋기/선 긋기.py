import sys
input = sys.stdin.readline

N = int(input())

lines = []

result = 0

for i in range(N):
    x,y = map(int,input().split())
    lines.append((x,y))

lines.sort()

start, end = lines[0]

for i in range(1,N):
    x,y = lines[i]

    if x <= end :
        end = max(y, end)
        
    else :
        result += (end - start)
        start, end = x, y
    
result += (end - start)
print(result)
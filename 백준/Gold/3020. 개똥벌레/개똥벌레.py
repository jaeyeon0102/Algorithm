import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# 인덱스: 높이
bottom = [0] * (H + 1)
top = [0] * (H + 1)

for i in range(N):
    size = int(input())
    if i % 2 == 0:
        bottom[size] += 1  # 석순
    else:
        top[size] += 1     # 종유석

# 누적합
for i in range(H - 1, 0, -1):
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]


min_obstacles = N  # 최소 파괴 개수
count = 0          # 최소값이 나타나는 구간

for i in range(1, H + 1):
    total = bottom[i] + top[H - i + 1]
    
    if total < min_obstacles:
        min_obstacles = total
        count = 1
    elif total == min_obstacles:
        count += 1

print(min_obstacles, count)
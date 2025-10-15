'''
강을 가로지르는 다리 
n개의 트럭이 건너려고 함
트럭의 순서 못바꿈
무게 다름
w대의 트럭만 동시에 올라갈 수 있고 무게 함은 L보다 작거나 같아야 함


'''
from collections import deque

# 트럭 개수, 다리 길이, 다리 최대 하중
n, w, l = map(int,input().split())

n_list = list(map(int,input().split()))

bridge = deque([0]*w)

cur = 0                  # 다리 위 총 무게
time = 0
i = 0                    # 다음에 올릴 트럭 인덱스

while (i < n):
    time += 1
    cur -= bridge.popleft()

    if cur + n_list[i] <= l:
        bridge.append((n_list[i]))
        cur += n_list[i]
        i += 1
    else:
        bridge.append(0)

time += w

print(time)
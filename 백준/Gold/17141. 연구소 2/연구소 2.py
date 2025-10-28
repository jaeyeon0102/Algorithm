'''
연구소
바이러스 M개 놓을 거임
NxN 사각형
빈칸 : 0, 벽 : 1, 바이러스 : 2

bfs -> 빈칸 확인해서 현재 값과 기존 값 중 최솟값 넣기 (0제외)
'''

from collections import deque
from itertools import combinations

pos = [(0,1),(0,-1),(1,0),(-1,0)]

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus_list = [(i, j) for i in range(N) for j in range(N) if lab[i][j] == 2]

# 감염 대상: 0(빈칸) + (비활성 바이러스)
zero_cnt = sum(cell == 0 for row in lab for cell in row)
virus_cnt = len(virus_list)

def bfs(active):
    active_set = set(active)
    # 남은 감염 대상: 0 개수 + (전체 바이러스 - 활성 바이러스)
    remain = zero_cnt + (virus_cnt - len(active_set))
    if remain == 0:
        return 0

    visited = [[-1]*N for _ in range(N)]
    q = deque()

    for x, y in active:
        q.append((x, y, 0))
        visited[x][y] = 0

    while q:
        x, y, t = q.popleft()
        for dx, dy in pos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))

                    # 감염 대상이면 카운트 감소
                    if lab[nx][ny] == 0 or (lab[nx][ny] == 2 and (nx, ny) not in active_set):
                        remain -= 1
                        if remain == 0:
                            return t + 1

    return float('inf')

answer = float('inf')
for comb in combinations(virus_list, M):
    answer = min(answer, bfs(comb))

print(-1 if answer == float('inf') else answer)
'''
보물은 서로 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있음

값이 L이면 BFS -> 순회를 돌고 나왔을 때, 

'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(si,sj):
    dist = [[-1] * W for _ in range(H)]
    q = deque([(si,sj)])
    dist[si][sj] = 0
    max_dist = 0

    while q:
        x, y = q.popleft()

        max_dist = max(max_dist, dist[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny] =='L' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    return max_dist                    



# 가로 세로
H, W = map(int, input().split())


board = [list(input()) for _ in range(H)]
result = 0

for i in range(H):
    for j in range(W):
        if board[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
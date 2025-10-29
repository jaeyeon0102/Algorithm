'''
5종류의 cctv 
감시 방향에 있는 칸 전체 감시 가능
감시 x영역은 사각지대
cctv 회전 가능
90도 방향으로 해야 함
cctv는 벽 통과 불가
0은 빈칸, 6은 벽
1~5는 cctv
cctv끼리 만나면 그냥 지나갈 수 있음
'''
import copy 

def watch(x,y,direction, board):
    n,m = len(board), len(board[0])
    dx, dy = pos[direction]
    while True:
        x += dx
        y += dy
        if not (0 <= x < n and 0 <= y < m):
            return
        if board[x][y] == 6:  # 벽이면 stop
            return
        if board[x][y] == 0:  # 빈 칸이면 감시 처리
            board[x][y] = '#'
    

def dfs(depth, board):
    global min_blind

    if depth == len(cctvs):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1
        min_blind = min(min_blind, cnt)
        return

    x,y,t = cctvs[depth]
    for dirs in cctv_dirs[t]:
        temp = [row[:] for row in board]
        for d in dirs:
            watch(x,y,d, temp)
        dfs(depth +1, temp)

                    

pos = [(-1,0),(0,1),(1,0),(0,-1)]
N, M = map(int,input().split())

map_list = [list(map(int,input().split())) for _ in range(N)]

cctv_dirs = {
    1: [[0], [1], [2], [3]],               # 한 방향
    2: [[0, 2], [1, 3]],                   # 서로 반대 방향
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],   # 직각 두 방향
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 세 방향
    5: [[0, 1, 2, 3]]                      # 네 방향 (고정)
}
cctvs = []

for i in range(N):
    for j in range(M):
        if 1<= map_list[i][j] <=5:
            cctvs.append((i,j,map_list[i][j]))

min_blind = int(1e9)
dfs(0,map_list)


print(min_blind)
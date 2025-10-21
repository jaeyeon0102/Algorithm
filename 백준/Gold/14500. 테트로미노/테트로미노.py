'''
테트로미노

폴리오미노 
- 정사각형은 서로 겹치면 안됨
- 도형은 모두 연결되어 있어야 함
- 정사각형의 변끼리 연결되어 있어야 함. 꼭짓점과 꼭짓점만 맞닿아 있으면 안됨

NxM크기
dfs 정사각형 4개 선택 
ㅗ 모양은 따로 함수 만들기

해당 좌표별 값 더해서 max값 저장하기 

최종 max값 출력
'''

# ㅗ 모양 아닌 모든 것
def sol(x,y,depth, current):
    global max_num

    if depth == 4:
        max_num = max(max_num, current)
        return
    
    for i in range(4):
        dx, dy = x + pos[i][0], y + pos[i][1]

        if 0 <= dx <N and 0 <= dy < M and not visited[dx][dy]:
            visited[dx][dy] = 1
            sol(dx,dy,depth+1, current + matrix[dx][dy])
            visited[dx][dy] = 0

    

# ㅗ 모양
def check(x,y):
    global max_num

    center = matrix[x][y]
    neighbor = []

    for i in range(4):
        dx, dy = x + pos[i][0], y + pos[i][1]
        if 0 <= dx <N and 0 <= dy < M:
            neighbor.append(matrix[dx][dy])

    neighbor.sort(reverse=True)

    if len(neighbor) >= 3:
        max_num = max(max_num, center+sum(neighbor[:3]))

    return 


pos = [(0,1),(0,-1),(1,0),(-1,0)]

N,M = map(int,input().split())
max_num = 0

matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        sol(i,j,1,matrix[i][j])
        visited[i][j] = 0

        check(i,j)

print(max_num)
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(maps):
    q = deque()
    n = len(maps)
    m = len(maps[0])
    
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        if (x == n-1) and (y == m -1) and maps[x][y] != 1:
            return maps[n-1][m-1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx,ny))
    
    return -1     
    

def solution(maps):
    return bfs(maps)
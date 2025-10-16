def bfs(x,y,current):
    global check
    q = []
    q.append((x,y,current))
    same_thing = []
    same_thing.append((x,y))
    visited = set()
    visited.add((x,y))
    num = 1
    while q:
        dx,dy, cur = q.pop(0)

        for i in range(4):
            nx, ny = dx + pos[i][0], dy + pos[i][1]
            if 0 <= nx < 12 and 0 <= ny < 6 and puyo_list[nx][ny] == cur and (nx,ny) not in visited:
                num += 1
                same_thing.append((nx,ny))
                q.append((nx,ny,cur))
                visited.add((nx,ny))
    if num >= 4:
        for a,b in same_thing:
            puyo_list[a][b] = '.'
        check = False
    return


def puyo_down():
    while True:
        check = True
        for i in range(11,0,-1):
            for j in range(5,-1,-1):
                if puyo_list[i][j] == '.':
                    if puyo_list[i-1][j] != '.':
                        puyo_list[i][j] = puyo_list[i-1][j]
                        puyo_list[i-1][j] = '.'
                        # print(i,j)
                        # for i in range(12):
                        #     for j in range(6):
                        #         print(puyo_list[i][j],end='')
                        #     print() 
                        check = False
                        break
        if check:
            break  



pos = [(0,1),(0,-1),(1,0),(-1,0)]
puyo_list = [list(map(str,input().strip())) for _ in range(12)]

result = 0
while True:
    check = True
    for i in range(12):
        for j in range(6):
            if puyo_list[i][j] != '.':
                bfs(i,j,puyo_list[i][j])
    puyo_down()
    # for i in range(12):
    #     for j in range(6):
    #         print(puyo_list[i][j],end='')
    #     print("\n") 
    if check:
        break
    else:
        result += 1

print(result)
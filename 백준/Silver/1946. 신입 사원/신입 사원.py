T = int(input())

for i in range(T):
    n = int(input())

    num_list = [list(map(int,input().split())) for _ in range(n)]

    num_list.sort()
    cnt = 1
    max_num = num_list[0][1]
    for i in range(1,n):
        if max_num > num_list[i][1]:
            cnt += 1
            max_num = num_list[i][1]

    print(cnt)
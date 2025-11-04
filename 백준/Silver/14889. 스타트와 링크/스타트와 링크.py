from itertools import combinations

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]
n_list = range(N)

comb = list(combinations(n_list,N//2))

min_num = float("inf")

for num in comb:
    team = set(num)
    other = set(n_list) - team
    
    start_score = sum(matrix[i][j] + matrix[j][i] for i, j in combinations(team, 2))
    link_score  = sum(matrix[i][j] + matrix[j][i] for i, j in combinations(other, 2))

    min_num = min(min_num, abs(start_score - link_score))
print(min_num)
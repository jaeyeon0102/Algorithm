'''
1 이상 N 이하인 정수가 있음
 
정수의 개수가 최대인 집합 숫자 구하기

'''
def dfs(v, i):
    visited[v] = 1

    for k in arr[v]:
        if not visited[k]:
            dfs(k, i)
        elif visited[k] and k == i:
            result.append(k)


n = int(input())

arr = [[] for _ in range(n+1)]

for i in range(1, n+1):
    arr[int(input())].append(i)

result = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)

print(len(result))
for i in result:
    print(i)
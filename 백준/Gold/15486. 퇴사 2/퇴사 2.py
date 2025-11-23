import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

dp = [0]*(N+1)

for day in range(N):
    # 기간, 금액
    t,p = arr[day]
    dp[day+1] = max(dp[day+1], dp[day])
     
    if day+t <= N:
        dp[day+t] = max(dp[day+t], dp[day]+p)

print(dp[N])
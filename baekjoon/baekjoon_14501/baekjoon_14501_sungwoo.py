n = int(input())
day = []
cost = []
dp = []

for i in range(n):
    x, y = map(int, input().split())
    day.append(x)
    cost.append(y)
    dp.append(y)
dp.append(0)

for i in range(n-1, -1, -1):
    if day[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], cost[i] + dp[i + day[i]])
print(dp[0])
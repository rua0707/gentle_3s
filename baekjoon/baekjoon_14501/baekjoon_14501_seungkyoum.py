import sys

N = int(input())

table = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if i + table[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(table[i][1] + (i + table[i][0]), dp[i+1])
        
print(dp[0])
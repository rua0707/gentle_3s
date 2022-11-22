import sys

N = int(sys.stdin.readline())
dp = [-1]*1001

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+1, dp[i-3]+1)

if dp[N] % 2 == 0:
    print("CY")
else:
    print("SK")


# N = int(sys.stdin.readline())
# if N % 2 == 0:
#     print("CY")
# else:
#     print("SK")
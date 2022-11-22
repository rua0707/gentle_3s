import sys
input = sys.stdin.readline

day, k = map(int, input().split())
temperature = list(map(int, input().split()))

res = []
res.append(sum(temperature[:k]))
for i in range(day - k):
    res.append(res[i] - temperature[i] + temperature[k+i])

print(max(res))

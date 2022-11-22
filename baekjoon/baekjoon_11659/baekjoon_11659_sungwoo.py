import sys
input = sys.stdin.readline
a, b = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
temp = 0
for i in num:
    temp += i
    sum.append(temp)
for j in range(b):
    c, d = map(int, input().split())
    print(sum[d] - sum[c-1])
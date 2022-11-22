import sys

n = int(sys.stdin.readline())
list_ = []

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    list_.append((w, h))

for i in list_:
    res = 1
    for j in list_:
        if i[0] < j[0] and i[1] < j[1]:
            res += 1
    print(res, end=" ")
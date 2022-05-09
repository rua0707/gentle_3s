import sys

N = int(sys.stdin.readline())

for i in range(N):
    lines = sys.stdin.readline()
    total = 0
    cnt = 0
    for j in lines:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        total += cnt
    print(total)

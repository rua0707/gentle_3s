import sys

N, M = map(int, sys.stdin.readline().split())
board = []

for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

cnt = 0

for i in range(N):
    pre = "/"
    for j in range(M):
        if board[i][j] == "-":
            if board[i][j] != pre:
                cnt += 1
        pre = board[i][j]

for j in range(M):
    pre = "/"
    for i in range(N):
        if board[i][j] == "|":
            if board[i][j] != pre:
                cnt += 1
        pre = board[i][j]

print(cnt)

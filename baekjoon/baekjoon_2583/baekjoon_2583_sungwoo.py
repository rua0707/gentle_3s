import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []

def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)
    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 1))
print(len(res))
print(*sorted(res))
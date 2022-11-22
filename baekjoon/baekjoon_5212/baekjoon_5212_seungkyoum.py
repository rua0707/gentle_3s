import copy
import sys

R, C = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]
new_graph = copy.deepcopy(graph)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(R):
    for y in range(C):
        if graph[x][y] == ".":
            continue
        sea_count = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                sea_count += 1
                continue
            elif graph[nx][ny] == ".":
                sea_count += 1
        
        if sea_count >= 3:
            new_graph[x][y] = "."

start_row, start_col, end_row, end_col = 0, 0, 0, 0
min_idx = C-1
max_idx = 0

for i in range(R):
    if "X" in new_graph[i]:
        start_row = i
        break

for i in range(R-1, -1, -1):
    if "X" in new_graph[i]:
        end_row = i
        break

for i in range(start_row, end_row+1):
    tmp = [i for i, value in enumerate(new_graph[i]) if value == "X"]
    if not tmp:
        continue
    min_tmp = tmp[0]
    max_tmp = tmp[-1]
    min_idx = min(min_idx, min_tmp)
    max_idx = max(max_idx, max_tmp)

for i in range(start_row, end_row+1):
    for j in range(min_idx, max_idx+1):
        print(new_graph[i][j], end="")
    print()
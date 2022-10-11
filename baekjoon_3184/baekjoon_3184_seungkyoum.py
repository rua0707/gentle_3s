from collections import deque
import sys

parallel = [0, 0, 1, -1]
vertical = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())
MAP_ = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

def bfs(x, y):
    dq = deque()
    dq.append([x,y])
    wolf = 0
    sheep = 0
    if MAP_[x][y] == "v":
        wolf += 1
    elif MAP_[x][y] == "o":
        sheep += 1
    visited[x][y] = True
    
    while dq:
        X, Y = dq.popleft()
        for i in range(4):
            mx, my = X + vertical[i], Y + parallel[i]
            if 0 <= mx < R and 0 <= my < C:
                if visited[mx][my] == False:
                    if MAP_[mx][my] == ".":
                        dq.append([mx, my])
                        visited[mx][my] = True
                    elif MAP_[mx][my] == "v":
                        wolf += 1
                        dq.append([mx, my])
                        visited[mx][my] = True
                    elif MAP_[mx][my] == "o":
                        sheep += 1
                        dq.append([mx, my])
                        visited[mx][my] = True
    if sheep == 0 and wolf == 0:
        return ["None", 0]
    elif sheep > wolf:
        return ["sheep", sheep]
    else:
        return ["wolf", wolf]

answer = [0, 0]
for i in range(R):
    for j in range(C):
        if visited[i][j] == False:
            if MAP_[i][j] != "#":
                result = bfs(i, j)
                if result[0] == "sheep":
                    answer[0] += result[1]
                elif result[0] == "wolf":
                    answer[1] += result[1]
print(*answer)
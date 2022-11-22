n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False] * n

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, depth):
    if depth == 4:
        print(1)
        exit()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)
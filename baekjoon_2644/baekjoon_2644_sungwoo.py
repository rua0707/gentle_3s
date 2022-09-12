n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result[i] = result[v] + 1
            dfs(i)
dfs(a)
print(result[b] if result[b] > 0 else -1)
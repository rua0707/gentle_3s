import sys

n, m = map(int, sys.stdin.readline().split())

relation = [[] for _ in range(n)]
visited = [False] * n
res = False

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(cnt, idx):
    global res
    if cnt == 4:
        res = True
        return
    
    for i in relation[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, i)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if res:
        break

if res:
    print(1)
else:
    print(0)
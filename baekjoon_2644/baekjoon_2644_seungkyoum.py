import sys

# 입력 값
N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)] # 그래프 초기화(2차원 리스트)
visited = [False]* (N+1) # 방문 내역
res = [] # 결과 값 저장

# 그래프 생성
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS (재귀)
def dfs(v, num):
    num += 1
    visited[v] = True

    if v == B:
        res.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

# DFS 호출 (비교대상 값 중 앞에꺼 입력)
dfs(A, 0)
if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
res = []

while q:
    idx, num = q.popleft()
    res.append(idx+1)

    if num > 0:
        # 양수, 이미 pop한거 포함해서 num만큼 왼쪽으로 회전
        q.rotate(-(num-1))
    elif num < 0:
        q.rotate(-num)

print(' '.join(map(str, res)))
import sys

king, stone, move_cnt = map(str, sys.stdin.readline().split())

# king 과 stone위치를 숫자 좌표로 변경
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))

# 움직이는 모든 방향 저장(8개)
move = {'R':[1,0], 'L':[-1,0], 'B':[0,-1], 'T':[0,1], 'RT':[1,1], 'LT':[-1,1], 'RB':[1,-1], 'LB':[-1,-1]}

for _ in range(int(move_cnt)):
    # king을 움직일 방향 입력
    locate = sys.stdin.readline().strip()
    # 이동 후 위치 저장
    nx = k[0] + move[locate][0]
    ny = k[1] + move[locate][1]

    # 이동 후 위치가 체스판 크기보다 작은 경우 king, stone 이동
    if 0 < nx <= 8 and 0 < ny <= 8:
        if nx == s[0] and ny == s[1]:
            sx = s[0] + move[locate][0]
            sy = s[1] + move[locate][1]
            # 이동 후 king의 위치와 stone의 위치가 같은경우 stone위치를 king의 이동방향으로 이동
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
        else:
            k = [nx, ny]

# 출력
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')
def get_pos(chess_pos):
    x = ord(chess_pos[0]) - ord('A')
    y = 8 - int(chess_pos[1])
    return x, y

def get_chess_pos(x_pos, y_pos):
    x = chr(x_pos + ord('A'))
    y = str(8 - y_pos)
    return x+y

king_pos, stone_pos, N = input().split()
kingx, kingy = get_pos(king_pos)
stonex, stoney = get_pos(stone_pos)

move_dir = {'R': (1, 0), 'L': (-1, 0), 'B': (0, 1), 'T': (0, -1), 'RT': (1, -1),
            'LT': (-1, -1), 'RB': (1, 1), 'LB': (-1, 1)}
for _ in range(int(N)):
    cmd = input()
    dx, dy = move_dir[cmd]
    king_nx, king_ny = kingx + dx, kingy + dy
    if 0 <= king_nx < 8 and 0 <= king_ny < 8:
        if stonex == king_nx and stoney == king_ny:
            stone_nx, stone_ny = stonex + dx, stoney + dy
            if 0 <= stone_nx < 8 and 0 <= stone_ny < 8:
                stonex, stoney = stone_nx, stone_ny
                kingx, kingy = king_nx, king_ny
        else:
            kingx, kingy = king_nx, king_ny
print(get_chess_pos(kingx, kingy))
print(get_chess_pos(stonex, stoney))
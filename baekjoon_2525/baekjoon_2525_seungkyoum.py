H, M = map(int, input().split())
r_time = int(input())

if (M + r_time) >= 60:
    H += ((M + r_time) // 60)
    M = (M + r_time) - ((M + r_time) // 60 * 60)
else:
    M += r_time
import sys

E, S, M = map(int, sys.stdin.readline().split()) # 준규나라 시간 입력 값
current_e, current_s, current_m = 1, 1, 1 # 준규나라 현재 시간
y = 1 # 연도

# 준규 나라 시간 1씩 증가시키면서 탐색
while 1:
    if E == current_e and S == current_s and M == current_m:
        print(y)
        break

    current_e += 1
    current_s += 1
    current_m += 1

# 각 E S M 값이 맥스값이 넘으면 1로 초기화
    if current_e == 16:
        current_e = 1
    if current_s == 29:
        current_s = 1
    if current_m == 20:
        current_m = 1
    
    y += 1


# 다른사람 코드
# E, S, M = map(int, sys.stdin.readline().split())
# y = 1

# while 1:
#     if (y - E) % 15 == 0 and (y - S) % 28 == 0 and (y - M) % 19 == 0:
#         break
#     y += 1

# print(y)
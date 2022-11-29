# 하노이탑 이동순서
import sys


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)  # 1단계
        print(a, c)
        hanoi(n - 1, b, a, c)  # 3단계


n = int(sys.stdin.readline())
print((2**n)-1)
hanoi(n, 1, 2, 3)

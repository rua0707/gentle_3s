import sys

N = int(sys.stdin.readline())

i = 1
while i * (i + 1) / 2 <= N:
    i += 1


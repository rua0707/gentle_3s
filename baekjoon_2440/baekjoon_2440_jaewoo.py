import sys

N = int(sys.stdin.readline())

for x in range(N,0,-1):
    for y in range(x):
        print("*",end='')
    print()


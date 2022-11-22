import sys

N, M = map(int, sys.stdin.readline().split())

noListen = set()
noLook = set()

for _ in range(N):
    noListen.add(sys.stdin.readline().strip())

for _ in range(M):
    noLook.add(sys.stdin.readline().strip())

print(len(sorted(noListen & noLook)))
for i in sorted(noListen & noLook):
    print(i)
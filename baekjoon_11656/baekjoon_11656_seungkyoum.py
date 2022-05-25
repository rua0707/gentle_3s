import sys

S = str(sys.stdin.readline().strip()).lower()

res = []
for i in range(len(S)):
    res.append(S[i:])

res.sort()
for i in res:
    print(i)
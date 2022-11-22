N, M = map(int, input().split())
print(0 if N*M == 1 else (N*M)-1)
if N*M == 1:
    print(0)
else:
    print((N*M)-1)
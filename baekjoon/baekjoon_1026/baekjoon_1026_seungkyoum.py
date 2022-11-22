import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

S = 0
A.sort()
for i in range(N):
    x = A[i]
    y = B.pop(B.index(max(B)))
    S += (x*y)
    
print(S)

# N = int(sys.stdin.readline())
# A = sorted(list(map(int, sys.stdin.readline().strip().split())))
# B = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse=True)

# S = 0
# for i in range(N):
#     S = S + (A[i] * B[i])
# print(S)
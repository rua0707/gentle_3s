import sys

A, B = map(str, sys.stdin.readline().split())

res_list = []
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] == B[j+i]:
            cnt += 1
    res_list.append(len(A) - cnt)

print(min(res_list))
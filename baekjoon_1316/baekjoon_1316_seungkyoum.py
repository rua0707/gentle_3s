import sys
from tkinter import N

N = int(sys.stdin.readline())
res = N

for _ in range(N):
    word = sys.stdin.readline().strip()
    for i in range(len(word) - 1):
        if word[i] == word[i+1]: # 먼저 같은지 체크
            pass
        elif word[i] in word[i+1:]: # 다음 문자와 같지 않은 상태에서, 이후에 문자에 같은게 있는지 체크
            res -= 1
            break

print(res)
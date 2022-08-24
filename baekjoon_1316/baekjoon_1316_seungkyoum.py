import sys
from tkinter import N

N = int(sys.stdin.readline())
res = N

for _ in range(N):
    word = sys.stdin.readline().strip()
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            res -= 1
            break

print(res)
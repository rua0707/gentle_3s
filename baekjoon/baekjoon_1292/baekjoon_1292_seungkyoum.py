import sys

init_, last_ = map(int, sys.stdin.readline().split())
seq = []

for i in range(last_+1):
    for j in range(i):
        seq.append(i)
print(sum(seq[init_-1:last_]))
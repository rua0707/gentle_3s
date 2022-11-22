import sys

N = int(sys.stdin.readline)

word_list = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.append(word)

for i in word_list:
    for j in i:
        print()
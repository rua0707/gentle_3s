import sys

N = int(sys.stdin.readline())

word_list = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.append(word)

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)
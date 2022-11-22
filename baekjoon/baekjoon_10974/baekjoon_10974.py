import sys

n = int(sys.stdin.readline())
temp = []


def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()


dfs()

# import sys
# import itertools

# n = int(sys.stdin.readline())

# arr = [str(i) for i in range(1, n+1)]
# npr = itertools.permutations(arr, n)

# for i in list(npr):
#     print(' '.join(i))

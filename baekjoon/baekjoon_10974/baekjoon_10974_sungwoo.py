from itertools import permutations
n = int(input())
list1 = [i for i in range(1, n+1)]
for i in list(permutations(list1)):
    for j in i:
        print(j, end=' ')
    print()
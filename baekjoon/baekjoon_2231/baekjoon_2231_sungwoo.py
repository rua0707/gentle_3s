n = int(input())
for i in range(n+1):
    list1 = []
    list1.extend(str(i))
    list2 = list(map(int, list1))
    if (i + sum(list2)) == n:
        print(i)
        break
    if i == n:
        print(0)
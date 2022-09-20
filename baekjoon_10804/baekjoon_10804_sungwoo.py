list1 = [i for i in range(21)]
for i in range(10):
    a, b = map(int, input().split())
    while a <= b:
        list1[a], list1[b] = list1[b], list1[a]
        a += 1
        b -= 1
list1.remove(0)
for i in list1:
    print(i, end=' ')
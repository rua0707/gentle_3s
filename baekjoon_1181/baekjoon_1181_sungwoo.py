T = int(input())
list1 = []
for i in range(T):
    list1.append(input())
list2 = list(set(list1))
list2.sort()
list2.sort(key=len)
for i in list2:
    print(i)
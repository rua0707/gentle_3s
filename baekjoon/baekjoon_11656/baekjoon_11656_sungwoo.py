a = input()
list1 = []
for i in range(len(a)):
    list1.append(a[i:])
list1.sort()
for i in list1:
    print(i)
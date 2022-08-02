n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
for j in range(n):
    print(min(list1))
    list1.remove(min(list1))
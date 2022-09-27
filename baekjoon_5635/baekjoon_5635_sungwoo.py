n = int(input())
list1 = []
for i in range(n):
    name, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    list1.append((y, m, d, name))
list1.sort()
print(list1[-1][3])
print(list1[0][3])
a, b = map(int, input().split())
list1 = []
sum = 0
for i in range(1, b+1):
    for j in range(i):
        list1.append(i)
for i in range(a, b+1):
    sum += list1[i-1]
print(sum)
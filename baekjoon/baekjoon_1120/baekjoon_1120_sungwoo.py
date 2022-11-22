a, b = input().split()
list1 = []
for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1
    list1.append(count)
print(min(list1))
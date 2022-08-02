a = int(input())
b = int(input())
list1 = []
for i in range(a, b+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        list1.append(i)
if len(list1) == 0:
    print(-1)
else:
    print(sum(list1))
    print(min(list1))
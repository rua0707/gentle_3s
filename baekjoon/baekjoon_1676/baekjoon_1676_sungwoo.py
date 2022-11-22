N = int(input())
factorial = 1
for i in range(1, N + 1):
    factorial *= i
list1 = []
list1.extend(str(factorial))
list1.reverse()
count = 0
for i in list1:
    if i == "0":
        count += 1
    else:
        break
print(count)
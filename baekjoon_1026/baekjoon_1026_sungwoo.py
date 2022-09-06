N = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
Sum = 0
for i in range(N):
    Sum += min(list1) * max(list2)
    list1.remove(min(list1))
    list2.remove(max(list2))
print(Sum)
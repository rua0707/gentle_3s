T = int(input())
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
for i in range(T):
    list1 = list(map(int, input().split()))
    n = list1.pop(0)
    list1.sort()
    sum = 0
    for i in range(len(list1)-1):
        for j in range(i+1, len(list1)):
            sum += gcd(list1[i], list1[j])
    print(sum)
import sys

t = int(sys.stdin.readline())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(int(t)):
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    first_ = num_list.pop(0)
    sum_ = 0

    for i in range(first_):
        for j in range(first_):
            if i < j:
                sum_ += gcd(num_list[i], num_list[j])
    print(sum_)
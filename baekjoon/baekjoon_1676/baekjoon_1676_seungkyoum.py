from math import factorial

n = int(input())

fact = str(factorial(n))
cnt = 0
for i in fact[::-1]:
    if i != "0":
        break
    cnt += 1
print(cnt)


# import sys

# n = int(sys.stdin.readline())

# cnt = 0

# while n >= 5:
#     cnt += n//5
#     n //= 5

# print(cnt)
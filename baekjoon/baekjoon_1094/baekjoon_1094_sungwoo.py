x = int(input())
cnt = 0
while x != 0:
    if x % 2 == 1:
        cnt += 1
    x //= 2
print(cnt)
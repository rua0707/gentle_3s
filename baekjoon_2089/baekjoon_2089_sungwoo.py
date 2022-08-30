n = int(input())
ans = ''
if n == 0:
    print(0)
    exit()
else:
    while n!= 0:
        if n % (-2) == 0:
            n = n // (-2)
            ans = '0' + ans
        else:
            n = n // (-2) + 1
            ans = '1' + ans
print(int(ans))
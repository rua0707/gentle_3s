T = int(input())
for i in range(T):
    r = input()
    s = list(r)
    sum = 0
    for i in s:
        if i == '(':
            sum = sum + 1
        elif i == ')':
            sum = sum - 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
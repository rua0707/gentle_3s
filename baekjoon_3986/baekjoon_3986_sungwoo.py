T = int(input())
cnt = 0
for i in range(T):
    a = input()
    stack = []
    for i in range(len(a)):
        if stack and a[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(a[i])
    if not stack:
        cnt += 1
print(cnt)
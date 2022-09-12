n = input()
stack = []
temp = 1
result = 0
for i in range(len(n)):
    if n[i] == "(":
        temp *= 2
        stack.append("(")
    elif n[i] == "[":
        temp *= 3
        stack.append("[")
    elif n[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if n[i-1] == "(":
            result += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if n[i-1] == "[":
            result += temp
        temp //= 3
        stack.pop()
if stack:
    result = 0
print(result)
import sys

N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline()
    stack = []
    flag = True
    for j in line:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack)>0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                flag = False
                break
    if flag and len(stack) == 0:
        print("YES")
    else:
        print("NO")
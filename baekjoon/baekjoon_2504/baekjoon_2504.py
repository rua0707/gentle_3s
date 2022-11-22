import sys

# 입력 값
bracket = list(sys.stdin.readline().strip())

# 값 초기화
stack = list()  # 여는 괄호 저장
res = 0  # 최종 계산 값
tmp = 1  # 각 괄호의 현재 값

for i in range(len(bracket)):
    # 여는 소괄호, 값에 2를 곱함
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2
    # 여는 대괄호, 값에 3를 곱함
    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3
    # 닫는 괄호, 결과 값에 더한 후 스택에서 여는 괄호 지움
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if bracket[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            res = 0
            break
        if bracket[i-1] == "[":
            res += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(res)

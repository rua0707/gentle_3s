def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        s += s[0]
        s = s[1:]
        result = True
        for j in s:
            if j == "{" or j == "(" or j == "[":규
                stack.append(j)
            else:
                if stack == []:
                    result = False
                    break
                if stack[-1] == "{" and j == "}" or stack[-1] == "(" and j == ")" or stack[-1] == "[" and j == "]":
                    stack.pop()
                else:
                    result = False
                    break
        if stack == [] and result == True:
            answer += 1
    return answer
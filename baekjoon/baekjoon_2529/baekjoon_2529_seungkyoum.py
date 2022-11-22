import sys
n = int(sys.stdin.readline())
sign = list(map(str, sys.stdin.readline().split()))

visited = [0] * 10
max_num, min_num = "", ""

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j

def solve(cnt, s):
    global max_num, min_num

    if cnt == n+1:
        if len(min_num) == 0:
            min_num = s
        else:
            max_num = s
        return
    
    for i in range(10):
        if visited[i] == 0:
            if cnt == 0 or check(s[-1], str(i), sign[cnt-1]):
                visited[i] = True
                solve(cnt+1, s+str(i))
                visited[i] = False

solve(0, "")
print(max_num)
print(min_num)

# n = int(input())
# sign = list(map(str,input().split()))

# visited = [0] * 10
# max_ans, min_ans = "", ""

# def check(i, j, k):
#     if k == '<':
#         return i < j
#     else:
#         return i > j

# def solve(cnt, s):
#     global max_ans, min_ans

#     if(cnt == n + 1):
#         if(len(min_ans) == 0):
#             min_ans = s
#         else:
#             max_ans = s
#         return
#     for i in range(10):
#         if(visited[i] == 0):
#             if(cnt == 0 or check(s[-1], str(i), sign[cnt - 1])):
#                 visited[i] = True
#                 solve(cnt + 1, s + str(i))
#                 visited[i] = False


# solve(0,"")
# print(max_ans)
# print(min_ans)
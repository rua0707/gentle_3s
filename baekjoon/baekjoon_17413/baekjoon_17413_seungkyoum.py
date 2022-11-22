import sys
S = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(S):
    if S[i] == "<":
        i += 1
        while S[i] != ">":
            i += 1
        i += 1
    elif S[i].isalnum():
        start = i
        while i < len(S) and S[i].isalnum():
            i += 1
        tmp = S[start:i]
        tmp.reverse()
        S[start:i] = tmp
    else:
        i += 1

print("".join(S))
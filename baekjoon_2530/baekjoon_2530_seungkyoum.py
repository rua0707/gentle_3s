H, M, S = map(int, input().split())
r_time = int(input())

S += (r_time % 60)
r_time = (r_time // 60)
if S >= 60:
    S -= 60
    M += 1

M += (r_time % 60)
r_time = (r_time // 60)
if M >= 60:
    M -= 60
    H += 1

H += (r_time % 24)
if H >= 24:
    H -= 24
    
print(H, M, S)
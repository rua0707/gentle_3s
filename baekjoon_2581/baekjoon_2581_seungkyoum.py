S = int(input())
L = int(input())

res = []
for i in range(S, L+1):
    cnt = 0
    if i > 1:
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        
        if cnt == 2:
            res.append(i)

if len(res) >= 1:
    print(sum(res))
    print(min(res))
else:
    print(-1)
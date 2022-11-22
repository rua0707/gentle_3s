t = int(input())

for _ in range(t):
    bracket = input()
    vps = []
    res = ""

    for i in bracket:
        if i == "(":
            vps.append(i)
        elif i == ")":
            if len(vps) > 0:
                vps.pop()
            else:
                res = "NO"
                break
            
    if res == "" and len(vps) == 0:
        res = "YES"
    else:
        res = "NO"
    print(res)
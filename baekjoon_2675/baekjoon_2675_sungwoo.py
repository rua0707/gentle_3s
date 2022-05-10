t = int(input())

for i in range(t):
    r, s = input().split()
    for j in range(len(s)):
        print(int(r)*s[j],end='')
    print()
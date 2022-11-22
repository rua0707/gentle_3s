N, M = map(int, input().split())
set1 = set()
set2 = set()
for i in range(N):
    set1.add(input())
for i in range(M):
    set2.add(input())
result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)